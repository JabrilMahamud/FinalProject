from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('active/',views.S3active, name='active'),
    path('deactive/',views.S3Deactive, name='Deactive')
]