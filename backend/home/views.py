import json
from collections import defaultdict

from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from wagtail.images import get_image_model
from wagtail.models import Page, Site
from wagtail.rich_text import extract_references_from_rich_text
from wagtail.templatetags.wagtailcore_tags import richtext

from .image_formats import (
    ICON_RENDITION_NAME,
    REGULAR_RENDITION_NAME,
    THUMBNAIL_RENDITION_NAME,
)
from .models import (
    ChapterPage,
    ChapterQuizSubPage,
    ChapterTextSubPage,
    FinishedChapterData,
    HomePage,
    PageAnswerData,
)

ImageModel = get_image_model()


def custom_404_handler(request, exception):
    return JsonResponse(
        {
            "status": 404,
            "error": "Not found",
        },
        status=404,
    )


def serialize_image_url(image, is_icon=False):
    if image is None:
        return None

    obj = {
        "alt": image.title,
        "width": image.width,
        "height": image.height,
    }

    # don't generate renditions for SVG images
    if image.is_svg():
        obj["svg"] = True
        obj["original_url"] = image.file.url
        obj["url"] = image.file.url

    # other images have renditions for thumbnail and regular sizes
    else:
        RENDITION_NAME = REGULAR_RENDITION_NAME if not is_icon else ICON_RENDITION_NAME
        renditions = image.get_renditions(THUMBNAIL_RENDITION_NAME, RENDITION_NAME)

        obj["thumbnail_url"] = renditions[THUMBNAIL_RENDITION_NAME].file.url
        obj["original_url"] = image.file.url
        obj["url"] = renditions[RENDITION_NAME].file.url

    return obj


def serialize_rich_text_images(rich_text):
    ids = []
    for reference in extract_references_from_rich_text(rich_text):
        if reference[0] == ImageModel:
            ids.append(reference[1])

    images = ImageModel.objects.filter(id__in=ids).prefetch_renditions()
    return [serialize_image_url(image) for image in images]


def serialize_answer(answer):
    value = answer.value
    return {"text": value["text"], "correct": value["correct"]}


def serialize_chapter_sub_page(page):
    data = {
        "id": page.id,
        "title": page.title,
    }
    page = page.specific
    if isinstance(page, ChapterTextSubPage):
        data.update(
            {
                "type": "text",
                "text": richtext(page.text),
                "text_images": serialize_rich_text_images(page.text),
                "button_text": page.button_text,
            }
        )
    elif isinstance(page, ChapterQuizSubPage):
        data.update(
            {
                "type": "quiz",
                "image": serialize_image_url(page.image),
                "image_answer": serialize_image_url(page.image_answer),
                "question": page.question,
                "answers": [serialize_answer(answer) for answer in page.answers],
                "points": page.points,
                "answer_description": richtext(page.answer_description),
                "answer_description_images": serialize_rich_text_images(
                    page.answer_description
                ),
                "button_text": page.button_text,
            }
        )
    return data


class HomeView(View):
    def get(self, request, id=None):
        if id is None:
            site = Site.find_for_request(request)
            root_page = site.root_page.specific
        else:
            root_page = get_object_or_404(HomePage, id=id)

        chapters = ChapterPage.objects.filter(live=True).child_of(root_page)

        return JsonResponse(
            {
                "id": root_page.id,
                "title": root_page.title,
                "description": richtext(root_page.description),
                "description_images": serialize_rich_text_images(root_page.description),
                "button_text": root_page.button_text,
                "chapters": [
                    {
                        "id": chapter.id,
                        "title": chapter.title,
                        "description": chapter.description,
                        "image": serialize_image_url(chapter.image, is_icon=True),
                        "locked_by_default": chapter.locked_by_default,
                        "is_feedback": chapter.is_feedback,
                    }
                    for chapter in chapters
                ],
            }
        )


class ChapterView(View):
    def get(self, request, id):
        chapter = get_object_or_404(ChapterPage, id=id)

        pages = Page.objects.filter(live=True).child_of(chapter)

        return JsonResponse(
            {
                "id": chapter.id,
                "title": chapter.title,
                "pages": [serialize_chapter_sub_page(page) for page in pages],
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class FinishedChapterView(View):
    def post(self, request, id):
        chapter = get_object_or_404(ChapterPage, id=id)
        json_body = json.loads(request.body)
        json_data = json.loads(json_body["data"])

        finished_data = FinishedChapterData.objects.create(
            user_guid=json_body["userGUID"],
            chapter=chapter,
            score=json_data["score"],
        )

        for answer in json_data["answers"]["entries"]:
            answer_data = PageAnswerData.objects.create(
                page=ChapterQuizSubPage.objects.get(id=answer[0]),
                answer_index=answer[1]["answerIndex"],
                correct=answer[1]["correct"],
            )
            finished_data.answers.add(answer_data)

        return JsonResponse({"status": "ok"})


def admin_answer_analytics(request):
    page_data_count_correct = (
        PageAnswerData.objects.all()
        .prefetch_related("page", "finishedchapterdata__chapter")
        .values("finishedchapterdata__chapter__title", "page__title", "page__question")
        .annotate(
            correct_count=Count("correct", filter=Q(correct=True)),
            incorrect_count=Count("correct", filter=Q(correct=False)),
        )
    )

    page_data_count_answers = (
        PageAnswerData.objects.all()
        .prefetch_related("page", "finishedchapterdata__chapter")
        .values(
            "finishedchapterdata__chapter__title",
            "page",
            "page__title",
            "page__question",
            "answer_index",
        )
        .annotate(count=Count("answer_index"))
    )

    grouped_data = defaultdict(dict)

    for d in page_data_count_correct:
        chapter_title = d["finishedchapterdata__chapter__title"]
        page_title = d["page__title"]
        page_question = d["page__question"]
        correct_count = d["correct_count"]
        incorrect_count = d["incorrect_count"]
        percentage = correct_count / (correct_count + incorrect_count) * 100

        grouped_data[chapter_title][page_title] = {
            "question": page_question,
            "correct_count": correct_count,
            "incorrect_count": incorrect_count,
            "percentage": percentage,
            "answers": [],
        }

    for d in page_data_count_answers:
        chapter_title = d["finishedchapterdata__chapter__title"]
        page_title = d["page__title"]
        answer_index = d["answer_index"]
        count = d["count"]

        page_id = d["page"]
        page = ChapterQuizSubPage.objects.get(id=page_id)
        answer_values = [a["value"] for a in page.answers.raw_data]

        answers = grouped_data[chapter_title][page_title]["answers"]
        answers.append((answer_values[answer_index], count))
        answers.sort(key=lambda x: x[1], reverse=True)

    # disable default factory to fix template looping
    grouped_data.default_factory = None

    return render(
        request,
        "admin/answer_analytics.html",
        {"grouped_data": grouped_data},
    )
