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
