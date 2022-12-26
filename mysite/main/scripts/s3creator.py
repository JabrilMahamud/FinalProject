import csv
import boto3
from boto3.dynamodb.conditions import Attr

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