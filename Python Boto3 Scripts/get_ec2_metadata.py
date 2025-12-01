import requests

url = "http://169.254.169.254/latest/meta-data/instance-id"
try:
    instance_id = requests.get(url, timeout=1).text
    print("EC2 Instance ID:", instance_id)
except:
    print("This script must run ON an EC2 instance to get metadata.")
