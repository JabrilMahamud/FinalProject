from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("s3", views.s3View, name="MetaPath"),
]