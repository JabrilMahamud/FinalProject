from multiprocessing import connection
import boto3
import sqlite3


dynamodb = boto3.resource("dynamodb", region_name='eu-west-2')
table = dynamodb.Table('MetadataJson')

tableDict = table.scan(
    ProjectionExpression='#AN, account, #S',
    ExpressionAttributeNames={
        '#AN': 'account-name',
        '#S': 'status',
    },
)
tableList = list(tableDict.items())
tableResponse = tableList[0][1]
tableData = []
for i in range(len(tableResponse)):
    tableData.append([tableResponse[i].get('account-name'), 
    tableResponse[i].get('account'), 
    tableResponse[i].get('status')])
print(tableData)