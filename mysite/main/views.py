from django.shortcuts import render
from django.http import HttpResponse
from.models import *
from .s3creator import tableData,tableDict,tableResponse
# Create your views here.

def index(response):
    return HttpResponse("First View")

def s3View(response):
    return render(response, "/mysite/templates/s3metadata.html", {})