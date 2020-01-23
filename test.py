import os

from boto.dynamodb2 import connect_to_region
from boto.dynamodb2.fields import HashKey
from boto.dynamodb2.table import Table
import boto3

HOST = "localhost"
PORT = "8000"

os.environ["AWS_REGION"] = "us-east-1"
os.environ["AWS_ACCESS_KEY_ID"] = "local"
os.environ["AWS_SECRET_ACCESS_KEY"] = "local"


def create_boto3_table(name):
    r = boto3.resource(
        "dynamodb", region_name=os.getenv("AWS_REGION"), endpoint_url=f"http://{HOST}:{PORT}"
    )
    r.create_table(
        AttributeDefinitions=[{"AttributeName": "string", "AttributeType": "S"}],
        TableName=name,
        KeySchema=[{"AttributeName": "string", "KeyType": "HASH"}],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )
    print(list(r.tables.all()))


def create_boto2_table(name):
    c = connect_to_region(os.getenv("AWS_REGION"), host=HOST, port=PORT, is_secure=False)
    Table.create(name, schema=[HashKey("string")], throughput={"read": 1, "write": 1}, connection=c)
    print(c.list_tables())


create_boto3_table("table-boto3-us-east-1")
create_boto2_table("table-boto2-us-east-1")
os.environ["AWS_REGION"] = "us-west-1"
create_boto3_table("table-boto3-us-west-1")
