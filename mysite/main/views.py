from django.shortcuts import render
from django.http import HttpResponse
from .s3creator import *
# Create your views here.

def index(response):
    return HttpResponse("First View")

# class S3metadata():
#     template_name = "/mysite/templates/active.html"

#     def get_context_data(self,**kwargs):
#          context = super().get_context_data(**kwargs)
#          context["dictionary"] = s3creator("Active")
#          return context


def active(response):
    return render(response,"mysite/templates/active.html")