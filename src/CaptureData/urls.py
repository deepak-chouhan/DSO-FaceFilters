from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("video", views.sendVideo, name='video-stream'),
    path("set-filter", views.setFilter, name="set-filter"),
]

