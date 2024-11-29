from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import FinishedChapterData


class FinishedChapterDataViewSet(SnippetViewSet):
    model = FinishedChapterData
    list_display = ["id", "user_guid", "chapter", "finished_at"]


register_snippet(FinishedChapterDataViewSet)
