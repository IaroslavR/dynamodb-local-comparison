"""

"""
import os
import logging

from boto.dynamodb2 import connect_to_region
from boto.dynamodb2.fields import HashKey, RangeKey
from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.table import Table
import boto3

logging.basicConfig(level="DEBUG")

os.environ["AWS_REGION"] = "us-east-1"
os.environ["AWS_ACCESS_KEY_ID"] = "local"
os.environ["AWS_SECRET_ACCESS_KEY"] = "local"

HOST = "localhost"
PORT = "8000"
AWS_REGION = "us-east-1"
AWS_ACCESS_KEY_ID = "local"
AWS_SECRET_ACCESS_KEY = "local"

r = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION,
    # aws_access_key_id=AWS_ACCESS_KEY_ID,
    # aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=f"http://{HOST}:{PORT}",
)

try:
    table = r.create_table(
        AttributeDefinitions=[{"AttributeName": "string", "AttributeType": "S"}],
        TableName="tableboto3",
        KeySchema=[{"AttributeName": "string", "KeyType": "HASH"}],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )
except Exception as e:
    print(e)
print(list(r.tables.all()))

c = connect_to_region(
    AWS_REGION,
    host=HOST,
    port=PORT,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    is_secure=False
)


try:
    table2 = Table.create('tableboto22', schema=[
        HashKey('string'),
    ], throughput={
        'read': 1,
        'write': 1,
    }, connection=c)
except Exception as e:
    print(e)
print(c.list_tables())

c2 = DynamoDBConnection(
    host=HOST,
    port=PORT,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    is_secure=False,
    debug=True
)

print(c2.list_tables())
z = 1
