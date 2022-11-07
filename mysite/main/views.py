from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
import boto3
from boto3.dynamodb.conditions import Attr

# Create your views here.

def index(response):
    return HttpResponse("First View")

# class S3metadata():
#     template_name = "/mysite/templates/active.html"

#     def get_context_data(self,**kwargs):
#          context = super().get_context_data(**kwargs)
#          context["dictionary"] = s3creator("Active")
#          return context

def S3active(request):
    dynamodb = boto3.resource("dynamodb", region_name='eu-west-2')
    table = dynamodb.Table('MetadataJson')

    activeDict = table.scan(
        FilterExpression= Attr('status').eq("Active"),
        ProjectionExpression='#AN, account',
        ExpressionAttributeNames={
            '#AN': 'account-name',
        },
    )

    activeList=list(activeDict.items())

    activeResponse = activeList[0][1]

    activeAccounts =[]

    for i in range(len(activeResponse)):
        activeAccounts.append([activeResponse[i].get('account-name'),activeResponse[i].get('account')])

    return render(request, '../templates/active.html', {
        'Active': activeAccounts,
        })

def S3Deactive(request):
    dynamodb = boto3.resource("dynamodb", region_name='eu-west-2')
    table = dynamodb.Table('MetadataJson')

    activeDict = table.scan(
        FilterExpression= (Attr('status').eq("Closed") or Attr('status').eq("Terminated")),
        ProjectionExpression='#AN, account',
        ExpressionAttributeNames={
            '#AN': 'account-name',
        }
    )

    DeactiveList=list(activeDict.items())

    DeactiveResponse = DeactiveList[0][1]

    DeactiveAccounts =[]

    for i in range(len(DeactiveResponse)):
        DeactiveAccounts.append([DeactiveResponse[i].get('account-name'),DeactiveResponse[i].get('account')])

    return render(request, '../templates/deactive.html', {
        'Deactive': DeactiveAccounts,
        })
