from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.OldHome, name="OldHome"),
    path('active/',views.S3active, name='active'),
    path('deactive/',views.S3Deactive, name='Deactive'),
    path('downloads/',views.s3creator, name="S3"),
    path('newpage/',views.NewHome, name="New Page")

]