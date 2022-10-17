from django.urls import path
from main.views import S3metadata
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
]