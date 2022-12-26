
from django.shortcuts import render
<<<<<<< HEAD
from .classes.active import S3activeResponder
from .classes.deactive import S3deactiveResponder
from .classes.s3creator import s3creatorResponder
# Create your views here.#


def OldHome(request):
    return render(request, "../templates/mytemplates/s3metadata.html")

def NewHome(request):
    return render(request,'../templates/mytemplates/index.html',{
        'Name': "Jabril",
    })
=======
import boto3
from boto3.dynamodb.conditions import Attr
from mysite.main.classes.active import *

S3activeResponder

# Create your views here.#


##HOME PAGE###


def index(request):
    return render(request, "../templates/s3metadata.html")
>>>>>>> parent of cb071021 (moved from /s3 /)




#############ACTIVE ACCOUNTS#####



def S3active(request):
    return render(request, '../templates/mytemplates/active.html', {
        'Active': S3activeResponder,
        })




#######DEACTIVE ACCOUNTS#####


def S3Deactive(request):
<<<<<<< HEAD
    return render(request, '../templates/mytemplates/deactive.html', {
        'Deactive': S3deactiveResponder,
=======
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
>>>>>>> parent of cb071021 (moved from /s3 /)
        })


                       ###DOWNLOADER###
def s3creator(request):
<<<<<<< HEAD
    return render(request,"../templates/mytemplates/downloadPage.html",{
        'Accounts' : s3creatorResponder,
=======
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
>>>>>>> parent of cb071021 (moved from /s3 /)
    })

