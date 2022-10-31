from django.shortcuts import render
from django.http import HttpResponse
from .s3creator import *
# Create your views here.

def index(response):
    return HttpResponse("First View")

# class S3metadata(TemplateView):
#     template_name = "/mysite/templates/s3metadata.html"

#     def get_context_data(self,**kwargs):
#          context = super().get_context_data(**kwargs)
#          context["dictionary"] = tableDict
#          return context


def active(response):
    return render(response,"/templates/active.html",s3creator("Active"))