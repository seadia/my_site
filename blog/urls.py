from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("individual_post", views.individual_post, name="individual_post")
]