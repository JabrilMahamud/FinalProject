import boto3
from boto3.dynamodb.conditions import Attr

status="Active" or "Deactive"

def s3creator(status):
    dynamodb = boto3.resource("dynamodb", region_name='eu-west-2')
    table = dynamodb.Table('MetadataJson')

    tableDict = table.scan(
        FilterExpression= Attr('status').eq(status),
        ProjectionExpression='#AN, account, #S',
        ExpressionAttributeNames={
            '#AN': 'account-name',
            '#S':'status',
        },
    )
    
    tableList = list(tableDict.items())
    tableResponse = tableList[0][1]
    tableData = []
    for i in range(len(tableResponse)):
        tableData.append(
            [tableResponse[i].get('account-name'), tableResponse[i].get('account')]) 
    # print(tableData)
    print(type(tableData))

s3creator(status)

