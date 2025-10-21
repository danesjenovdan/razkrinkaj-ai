from django.urls import path

from .views import (
    ChapterView,
    EnsureFinishedChapterScoresView,
    FinishedChapterView,
    HomeView,
    LeaderboardNicknameView,
    LeaderboardView,
    PageStatsView,
    ProgressChapterView,
)

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
    path(
        "chapter/<int:chapter_id>/page/<int:page_id>/stats/",
        PageStatsView.as_view(),
        name="page_stats",
    ),
    path(
        "leaderboard/",
        LeaderboardView.as_view(),
        name="leaderboard",
    ),
    path(
        "leaderboard/nickname/",
        LeaderboardNicknameView.as_view(),
        name="leaderboard_nickname",
    ),
    path(
        "ensure-finished-chapter-scores/",
        EnsureFinishedChapterScoresView.as_view(),
        name="ensure_finished_chapter_scores",
    ),
]
