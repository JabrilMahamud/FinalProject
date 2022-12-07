from django.shortcuts import render
from django.http import HttpResponse
import boto3
from boto3.dynamodb.conditions import Attr
import datetime

# Create your views here.

def index(request):
    return render(request, "../templates/s3metadata.html")

def S3active(request):
    dynamodb = boto3.resource("dynamodb", region_name='eu-west-2')
    table = dynamodb.Table('MetadataJson')

    activeDict = table.scan(
        FilterExpression= Attr('status').eq("Active"),
        ProjectionExpression='#AN, account, #S',
        ExpressionAttributeNames={
            '#AN': 'account-name',
            '#S': 'status'
        },
    )

    activeList=list(activeDict.items())

    activeResponse = activeList[0][1]

    activeAccounts =[]

    for i in range(len(activeResponse)):
        activeAccounts.append([activeResponse[i].get('account-name'),activeResponse[i].get('account'),activeResponse[i].get('status')])

    return render(request, '../templates/active.html', {
        'Active': activeAccounts,
        })

def S3Deactive(request):
    dynamodb = boto3.resource("dynamodb", region_name='eu-west-2')
    table = dynamodb.Table('MetadataJson')

    deactiveDict = table.scan(
        FilterExpression=Attr('status').ne(("Active")),
        ProjectionExpression='#AN, account, #S',
        ExpressionAttributeNames={
            '#AN': 'account-name',
            '#S': 'status'
        }
    )

    DeactiveList=list(deactiveDict.items())

    DeactiveResponse = DeactiveList[0][1]

    DeactiveAccounts =[]

    for i in range(len(DeactiveResponse)):
        DeactiveAccounts.append([DeactiveResponse[i].get('account-name'),DeactiveResponse[i].get('account'), DeactiveResponse[i].get('status')])

    return render(request, '../templates/deactive.html', {
        'Deactive': DeactiveAccounts,
        })


def s3creator(request):
    import csv
    import boto3

    dynamodb = boto3.resource("dynamodb", region_name='eu-west-2')
    table = dynamodb.Table('MetadataJson')

    tableDict = table.scan(
        ProjectionExpression='#AN, account, #S',
        ExpressionAttributeNames={
            '#AN': 'account-name',
            '#S': 'status'
        },
    )

    tableList=list(tableDict.items())

    tableResponse = tableList[0][1]

    tableAccounts =[]
    for i in range(len(tableResponse)):
        tableAccounts.append([tableResponse[i].get('account-name'),tableResponse[i].get('account'),tableResponse[i].get('status')])

    print(tableAccounts)

    with open('test.csv', 'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tableAccounts)
    return render(request,"../templates/downloadPage.html",{
        'Accounts' : tableAccounts
    })