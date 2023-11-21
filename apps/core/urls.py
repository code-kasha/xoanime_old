from django.urls import path

from apps.core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clear", views.clear, name="clear"),
    path("details", views.details, name="details"),
    path("popular", views.popular, name="popular"),
    path("recent", views.recent, name="recent"),
    path("search", views.search, name="search"),
    path("top", views.top, name="top"),
    path("trending", views.trending, name="trending"),
    path("watch", views.watch, name="watch"),
    path("watch_episode", views.watch_episode, name="watch_episode"),
]
