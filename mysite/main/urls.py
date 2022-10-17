from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("s3", views.S3metadata, name="s3"),
]