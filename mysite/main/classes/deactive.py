import boto3
from boto3.dynamodb.conditions import Attr

def S3deactiveResponder():
    dynamodb = boto3.resource("dynamodb", region_name='eu-west-2')
    table = dynamodb.Table('MetadataJson')

    activeDict = table.scan(
        FilterExpression= Attr('status').ne("Active"),
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

    return activeAccounts


