
from django.shortcuts import render
import boto3
from boto3.dynamodb.conditions import Attr
from .classes.active import S3activeResponder
from .classes.deactive import S3deactiveResponder
from .classes.s3creator import s3creatorResponder
import csv
# Create your views here.#


def index(request):
    return render(request, "../templates/s3metadata.html")

def S3active(request):
    return render(request, '../templates/active.html', {
        'Active': S3activeResponder,
        })

def S3Deactive(request):
    return render(request, '../templates/deactive.html', {
        'Deactive': S3deactiveResponder,
        })

def s3creator(request):
    return render(request,"../templates/downloadPage.html",{
        'Accounts' : s3creatorResponder,
    })

