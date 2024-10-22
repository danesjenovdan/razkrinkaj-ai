from django.urls import path

from .views import ChapterView, HomeView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("home/<int:id>/", HomeView.as_view(), name="home"),
    path("chapter/<int:id>/", ChapterView.as_view(), name="chapter"),
]
