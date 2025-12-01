import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
)

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print("Instance ID:", instance["InstanceId"])
        print("Type:", instance["InstanceType"])
        print("Private IP:", instance.get("PrivateIpAddress"))
        print("Public IP:", instance.get("PublicIpAddress"))
        print("-" * 30)
