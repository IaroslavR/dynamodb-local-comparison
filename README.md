## DynamoDB local emulators tests

#### Target
Choose fastest standalone DynamoDB emulator

#### [Moto](https://github.com/spulec/moto)

- No `An error occurred (ValidationException) when calling the CreateTable operation: No provisioned throughput specified for the table` error support.  This code passed without error.
```python
r = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=f"http://{HOST}:{PORT}",
)

table = r.create_table(
    AttributeDefinitions=[{"AttributeName": "string", "AttributeType": "S"}],
    TableName="table",
    KeySchema=[{"AttributeName": "string", "KeyType": "HASH"}],
)           
```

- not working at all with current setup
#### [DynamoDB local](https://hub.docker.com/r/amazon/dynamodb-local/)
- Works as expected, but tables created with the help of boto2 invisible in `dynamodb-admin`
- Test suit execution time - approx. 17 min
 
 #### [dynalite](https://github.com/mhart/dynalite)
 - Works as expected
 - Test suit execution time - approx. 12 min
 