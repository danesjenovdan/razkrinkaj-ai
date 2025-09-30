import json
from collections import defaultdict

from django.db.models import Count, F, OuterRef, Q, Subquery, Sum, Window
from django.db.models.functions import DenseRank
from django.http import Http404, JsonResponse
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
    ManipulationExplanation,
    NicknameEntry,
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
                "button_text": "",  # DISABLED page.button_text,
            }
        )
    elif isinstance(page, ChapterQuizSubPage):
        data.update(
            {
                "type": "quiz",
                "image": serialize_image_url(page.image),
                "image_answer": None,  # DISABLED serialize_image_url(page.image_answer),
                "question": page.question,
                "source_text": richtext(page.source_text),
                "answers": [serialize_answer(answer) for answer in page.answers],
                "points": page.points,
                "answer_description": richtext(page.answer_description),
                "answer_description_images": serialize_rich_text_images(
                    page.answer_description
                ),
                "button_text": "",  # DISABLED page.button_text,
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
        explanations = ManipulationExplanation.objects.all().order_by("order")

        return JsonResponse(
            {
                "id": root_page.id,
                "title": root_page.title,
                "description": richtext(root_page.description),
                "description_images": serialize_rich_text_images(root_page.description),
                "button_text": root_page.button_text,
                "button_text_secondary": root_page.button_text_secondary,
                "chapters": [
                    {
                        "id": chapter.id,
                        "title": chapter.title,
                        "description": "",  # DISABLED chapter.description,
                        "image": None,  # DISABLED serialize_image_url(chapter.image, is_icon=True),
                        "locked_by_default": False,  # DISABLED chapter.locked_by_default,
                        "is_feedback": False,  # DISABLED chapter.is_feedback,
                    }
                    for chapter in chapters
                ],
                "explanations": [
                    {
                        "id": explanation.id,
                        "name": explanation.name,
                        "description": explanation.description,
                        "image": serialize_image_url(explanation.image),
                        "content": richtext(explanation.content),
                        "content_images": serialize_rich_text_images(
                            explanation.content
                        ),
                        "order": explanation.order,
                    }
                    for explanation in explanations
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


def get_or_create_finished_data(chapter, json_body):
    finished_data, created = FinishedChapterData.objects.get_or_create(
        user_guid=json_body["userGUID"],
        chapter=chapter,
        attempt_guid=json_body["attemptGUID"],
        defaults={"score": 0},
    )
    return finished_data


def update_or_create_page_answer_data(finished_data, json_data):
    for answer in json_data["answers"]["entries"]:
        page = ChapterQuizSubPage.objects.get(id=answer[0])

        if answer_data := finished_data.answers.filter(page=page).first():
            answer_data.answer_index = answer[1]["answerIndex"]
            answer_data.answer_text = answer[1].get("answerText", "")
            answer_data.correct = answer[1]["correct"]
            answer_data.save()

        else:
            answer_data = PageAnswerData.objects.create(
                page=page,
                answer_index=answer[1]["answerIndex"],
                answer_text=answer[1].get("answerText", ""),
                correct=answer[1]["correct"],
            )
            finished_data.answers.add(answer_data)


@method_decorator(csrf_exempt, name="dispatch")
class ProgressChapterView(View):
    def post(self, request, id):
        chapter = get_object_or_404(ChapterPage, id=id)
        json_body = json.loads(request.body)
        json_data = json.loads(json_body["data"])

        finished_data = get_or_create_finished_data(chapter, json_body)

        update_or_create_page_answer_data(finished_data, json_data)

        finished_data.save()

        return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name="dispatch")
class FinishedChapterView(View):
    def post(self, request, id):
        chapter = get_object_or_404(ChapterPage, id=id)
        json_body = json.loads(request.body)
        json_data = json.loads(json_body["data"])

        finished_data = get_or_create_finished_data(chapter, json_body)

        update_or_create_page_answer_data(finished_data, json_data)

        finished_data.score = json_data["score"]
        finished_data.is_finished = True
        finished_data.save()

        return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name="dispatch")
class PageStatsView(View):
    def get(self, request, chapter_id, page_id):
        chapter = get_object_or_404(ChapterPage, id=chapter_id)
        page = get_object_or_404(ChapterQuizSubPage, id=page_id)

        total_answers = PageAnswerData.objects.filter(page=page).count()
        if total_answers == 0:
            percent_correct = None
        else:
            correct_answers = PageAnswerData.objects.filter(
                page=page, correct=True
            ).count()
            percent_correct = round((correct_answers / total_answers) * 100)

        return JsonResponse(
            {
                "chapter_id": chapter.id,
                "page_id": page.id,
                "total_answers": total_answers,
                "percent_correct": percent_correct,
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class LeaderboardView(View):
    def get(self, request):
        attempt_guid = request.GET.get("attempt_guid", None)
        if not attempt_guid:
            raise Http404("No guid provided")

        my_score = (
            FinishedChapterData.objects.filter(attempt_guid=attempt_guid)
            .aggregate(total_score=Sum("score"))
            .get("total_score", 0)
        )

        my_rank = (
            FinishedChapterData.objects.values("attempt_guid")
            .annotate(total_score=Sum("score"))
            .filter(total_score__gt=my_score)
            .values("total_score")
            .distinct()
            .count()
            + 1
        )

        my_nickname = (
            NicknameEntry.objects.filter(attempt_guid=attempt_guid)
            .order_by("-created_at")
            .values_list("nickname", flat=True)
            .first()
        )

        top_scores = (
            FinishedChapterData.objects.values("attempt_guid")
            .annotate(total_score=Sum("score"))
            .order_by("-total_score")
            .values_list("total_score", flat=True)
            .distinct()[:3]
        )

        guids_in_top_places = (
            FinishedChapterData.objects.values("attempt_guid")
            .annotate(total_score=Sum("score"))
            .filter(total_score__in=top_scores)
        )

        ranked_guids = guids_in_top_places.annotate(
            rank=Window(
                expression=DenseRank(),
                order_by=F("total_score").desc(),
            )
        ).order_by("rank")

        # annotate with nickname if exists
        ranked_guids = ranked_guids.annotate(
            nickname=Subquery(
                NicknameEntry.objects.filter(attempt_guid=OuterRef("attempt_guid"))
                .order_by("-created_at")
                .values("nickname")[:1]
            )
        )

        # limit to 3 entries per each rank
        limited_ranked_guids = []
        current_rank = None
        current_rank_count = 0
        for entry in ranked_guids:
            if entry["rank"] != current_rank:
                current_rank = entry["rank"]
                current_rank_count = 1
                limited_ranked_guids.append(entry)
            else:
                if current_rank_count < 3:
                    current_rank_count += 1
                    limited_ranked_guids.append(entry)

        ranked_near_me = []
        if my_rank > 1:
            score_above_me = (
                FinishedChapterData.objects.values("attempt_guid")
                .annotate(total_score=Sum("score"))
                .annotate(
                    nickname=Subquery(
                        NicknameEntry.objects.filter(
                            attempt_guid=OuterRef("attempt_guid")
                        )
                        .order_by("-created_at")
                        .values("nickname")[:1]
                    )
                )
                .filter(total_score__gt=my_score)
                .order_by("total_score")
                .first()
            )
            if score_above_me:
                ranked_near_me.append(
                    {
                        "attempt_guid": score_above_me["attempt_guid"],
                        "total_score": score_above_me["total_score"],
                        "rank": my_rank - 1,
                        "nickname": score_above_me["nickname"],
                    }
                )
            ranked_near_me.append(
                {
                    "attempt_guid": attempt_guid,
                    "total_score": my_score,
                    "rank": my_rank,
                    "nickname": my_nickname,
                }
            )
            score_below_me = (
                FinishedChapterData.objects.values("attempt_guid")
                .annotate(total_score=Sum("score"))
                .annotate(
                    nickname=Subquery(
                        NicknameEntry.objects.filter(
                            attempt_guid=OuterRef("attempt_guid")
                        )
                        .order_by("-created_at")
                        .values("nickname")[:1]
                    )
                )
                .filter(total_score__lt=my_score)
                .order_by("-total_score")
                .first()
            )
            if score_below_me:
                ranked_near_me.append(
                    {
                        "attempt_guid": score_below_me["attempt_guid"],
                        "total_score": score_below_me["total_score"],
                        "rank": my_rank + 1,
                        "nickname": score_below_me["nickname"],
                    }
                )

        return JsonResponse(
            {
                "attempt_guid": attempt_guid,
                "my_score": my_score,
                "my_rank": my_rank,
                "my_nickname": my_nickname,
                "top_leaderboard": list(limited_ranked_guids),
                "ranked_near_me": ranked_near_me,
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class LeaderboardNicknameView(View):
    def post(self, request):
        json_body = json.loads(request.body)
        attempt_guid = json_body.get("attemptGUID", None)
        user_guid = json_body.get("userGUID", None)
        nickname = json_body.get("nickname", None)

        if not attempt_guid or not user_guid or not nickname:
            return JsonResponse(
                {
                    "status": 400,
                    "error": "Missing data",
                },
                status=400,
            )

        if len(nickname) > 20:
            return JsonResponse(
                {
                    "status": 400,
                    "error": "Nickname too long",
                },
                status=400,
            )

        finished_data = FinishedChapterData.objects.filter(
            attempt_guid=attempt_guid, user_guid=user_guid
        )
        if not finished_data.exists():
            return JsonResponse(
                {
                    "status": 400,
                    "error": "Wrong GUIDs",
                },
                status=400,
            )

        nickname_entry, created = NicknameEntry.objects.get_or_create(
            attempt_guid=attempt_guid,
            user_guid=user_guid,
            nickname=nickname,
        )

        if created:
            return JsonResponse({"status": "ok", "created": True})
        return JsonResponse({"status": "ok", "created": False})


def admin_answer_analytics(request):
    dangling_empty_page_answer_data_count = (
        PageAnswerData.objects.all().filter(finishedchapterdata=None).count()
    )

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

    finished_chapter_data_is_finished = (
        FinishedChapterData.objects.all()
        .values(
            "chapter__title",
        )
        .annotate(
            finished_count=Count("is_finished", filter=Q(is_finished=True)),
            unfinished_count=Count("is_finished", filter=Q(is_finished=False)),
        )
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

    for d in finished_chapter_data_is_finished:
        chapter_title = d["chapter__title"]
        finished_count = d["finished_count"]
        unfinished_count = d["unfinished_count"]
        percentage = finished_count / (finished_count + unfinished_count) * 100

        grouped_data[chapter_title]["XXX__is_finished"] = {
            "finished_count": finished_count,
            "unfinished_count": unfinished_count,
            "percentage": percentage,
        }

    # disable default factory to fix template looping
    grouped_data.default_factory = None

    return render(
        request,
        "admin/answer_analytics.html",
        {
            "grouped_data": grouped_data,
            "dangling_empty_page_answer_data_count": dangling_empty_page_answer_data_count,
        },
    )
