from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from wagtail.models import Page, Site
from wagtail.templatetags.wagtailcore_tags import richtext

from .models import ChapterPage, ChapterQuizSubPage, ChapterTextSubPage, HomePage


def custom_404_handler(request, exception):
    return JsonResponse(
        {
            "status": 404,
            "error": "Not found",
        },
        status=404,
    )


def serialize_image_url(image):
    # TODO: add image alt text
    # TODO: add image width and height
    # return {
    #     "url": image.file.url if image else None,
    # }
    return image.file.url if image else None


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
                "button_text": page.button_text,
            }
        )
    elif isinstance(page, ChapterQuizSubPage):
        data.update(
            {
                "type": "quiz",
                "image": serialize_image_url(page.image),
                "image_answer": serialize_image_url(page.image_answer),
                "answers": [serialize_answer(answer) for answer in page.answers],
                "points": page.points,
                "answer_description": richtext(page.answer_description),
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
                "button_text": root_page.button_text,
                "chapters": [
                    {
                        "id": chapter.id,
                        "title": chapter.title,
                        "description": chapter.description,
                        "image": serialize_image_url(chapter.image),
                        "locked_by_default": chapter.locked_by_default,
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
