from django.urls import path

from .views import ChapterView, FinishedChapterView, HomeView, ProgressChapterView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("home/<int:id>/", HomeView.as_view(), name="home"),
    path("chapter/<int:id>/", ChapterView.as_view(), name="chapter"),
    path(
        "chapter/<int:id>/finished/",
        FinishedChapterView.as_view(),
        name="finished_chapter",
    ),
    path(
        "chapter/<int:id>/progress/",
        ProgressChapterView.as_view(),
        name="progress_chapter",
    ),
]
