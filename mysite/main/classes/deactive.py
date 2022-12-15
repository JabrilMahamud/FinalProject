
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

    deactiveList=list(activeDict.items())
    deactiveResponse = deactiveList[0][1]
    deactiveAccounts =[]
    for i in range(len(deactiveResponse)):
        deactiveAccounts.append([deactiveResponse[i].get('account-name'),deactiveResponse[i].get('account'),deactiveResponse[i].get('status')])

    return deactiveAccounts


