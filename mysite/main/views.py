from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("First View")

def s3View(response):
    return HttpResponse("<h1>Metadata placeholder</h1>")