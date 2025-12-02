import boto3
from botocore.exceptions import ClientError

# Your instance ID
INSTANCE_ID = "i-05e93c6d9ea8da997"

# Create EC2 client
ec2 = boto3.client("ec2", region_name="us-east-1")

try:
    response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
    instance = response["Reservations"][0]["Instances"][0]

    print("\n=== EC2 Instance Metadata ===")
    print("Instance ID:", instance["InstanceId"])
    print("Instance Type:", instance["InstanceType"])
    print("AMI ID:", instance["ImageId"])
    print("Private IP:", instance.get("PrivateIpAddress"))
    print("Public IP:", instance.get("PublicIpAddress"))
    print("State:", instance["State"]["Name"])
    print("Launch Time:", instance["LaunchTime"])
    print("Availability Zone:", instance["Placement"]["AvailabilityZone"])
    print("\nSecurity Groups:")
    for sg in instance["SecurityGroups"]:
        print(" -", sg["GroupName"], "(", sg["GroupId"], ")")

except ClientError as e:
    print("Error retrieving instance details:", e)
