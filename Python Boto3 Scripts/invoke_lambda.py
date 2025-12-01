import boto3
import json

lambda_client = boto3.client("lambda")

# Sample S3 event structure
event = {
    "Records": [
        {
            "s3": {
                "bucket": {"name": "test-bucket"},
                "object": {"key": "dummy.txt"}
            }
        }
    ]
}

response = lambda_client.invoke(
    FunctionName="project-stack1-S3UploadLoggerLambda-WgfNh9FZjRun",
    InvocationType="RequestResponse",
    Payload=json.dumps(event)
)

print("Lambda invoke response:")
print(response["Payload"].read().decode())
