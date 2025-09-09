from django.urls import path
from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import FinishedChapterData, ManipulationExplanation
from .views import admin_answer_analytics


class FinishedChapterDataViewSet(SnippetViewSet):
    model = FinishedChapterData
    list_display = ["id", "user_guid", "chapter", "finished_at"]


class ManipulationExplanationViewSet(SnippetViewSet):
    model = ManipulationExplanation
    list_display = ["name", "description", "order"]


register_snippet(FinishedChapterDataViewSet)
register_snippet(ManipulationExplanationViewSet)


@hooks.register("register_admin_urls")
def register_admin_answer_analytics_url():
    return [
        path("answer-analytics/", admin_answer_analytics, name="answer-analytics"),
    ]
