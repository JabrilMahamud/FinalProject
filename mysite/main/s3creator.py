
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource("dynamodb", region_name='eu-west-2')
table = dynamodb.Table('MetadataJson')

activeDict = table.scan(
    FilterExpression= Attr('status').eq('Active'),
    ProjectionExpression='#AN, account',
    ExpressionAttributeNames={
        '#AN': 'account-name',
    },
)

activeList=list(activeDict.items())

activeResponse = activeList[0][1]


activeAccounts =[]
for i in range(len(activeResponse)):
    activeAccounts.append([activeResponse[i].get('account-name'),activeResponse[i].get('account'),activeResponse[i].get('status')])

print(type(activeAccounts))