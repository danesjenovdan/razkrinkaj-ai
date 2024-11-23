from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from wagtail.images import get_image_model
from wagtail.models import Page, Site
from wagtail.rich_text import extract_references_from_rich_text
from wagtail.templatetags.wagtailcore_tags import richtext

from .image_formats import (
    ICON_RENDITION_NAME,
    REGULAR_RENDITION_NAME,
    THUMBNAIL_RENDITION_NAME,
)
from .models import ChapterPage, ChapterQuizSubPage, ChapterTextSubPage, HomePage

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

    RENDITION_NAME = REGULAR_RENDITION_NAME if not is_icon else ICON_RENDITION_NAME
    renditions = image.get_renditions(THUMBNAIL_RENDITION_NAME, RENDITION_NAME)

    return {
        "original_url": image.file.url,
        "thumbnail_url": renditions[THUMBNAIL_RENDITION_NAME].file.url,
        "url": renditions[RENDITION_NAME].file.url,
        "alt": image.title,
        "width": image.width,
        "height": image.height,
    }


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
