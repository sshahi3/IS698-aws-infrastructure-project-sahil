import boto3
import uuid

s3 = boto3.client("s3")

bucket_name = "sahil-bucket-" + str(uuid.uuid4())[:8]

# Create bucket (NO LocationConstraint for us-east-1)
s3.create_bucket(Bucket=bucket_name)

print(f"Created bucket: {bucket_name}")

# Upload file
s3.upload_file("testfile.txt", bucket_name, "uploaded_via_boto3.txt")

print("Uploaded file uploaded_via_boto3.txt to bucket.")
