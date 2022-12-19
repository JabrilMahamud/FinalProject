
from django.shortcuts import render
import boto3
from boto3.dynamodb.conditions import Attr
from .classes.active import S3activeResponder
from .classes.deactive import S3deactiveResponder
from .classes.s3creator import s3creatorResponder
import csv
# Create your views here.#


def OldHome(request):
    return render(request, "../templates/mytemplates/s3metadata.html")

def NewHome(request):
    return render(request,'../templates/bootstrap/simplebootstrap.html',{
        'Name': "Jabril",
    })

def S3active(request):
    return render(request, '../templates/mytemplates/active.html', {
        'Active': S3activeResponder,
        })

def S3Deactive(request):
    return render(request, '../templates/mytemplates/deactive.html', {
        'Deactive': S3deactiveResponder,
        })

def s3creator(request):
    return render(request,"../templates//mytemplates/downloadPage.html",{
        'Accounts' : s3creatorResponder,
    })

