from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('metadata/',views.s3View, name='Metadata')
]