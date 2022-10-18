from django.urls import path
from main.views import S3metadata
from . import views

urlpatterns = [
    path("s3/", S3metadata.as_view(template_name="/mysite/main/templates/s3.html"), name="S3metadata"),
    path("", views.index, name="index"),
    
]