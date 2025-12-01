AWS Cloud Infrastructure Automation Project

Overview: This repository contains the complete implementation of an end-to-end cloud deployment project that integrates Terraform, AWS CloudFormation, AWS Lambda, S3, EC2, and Python Boto3. The objective of this project is to design, automate, and validate a cloud architecture following Infrastructure-as-Code (IaC) principles while demonstrating practical interaction with AWS services using both the AWS Console, AWS CLI, and Python SDK (Boto3). The repository is organized to reflect a real-world workflow commonly used by cloud engineers, DevOps teams, and solution architects. Every component has been implemented, tested, and documented to ensure reproducibility and clarity for academic evaluation.

1. Project Architecture: The automated environment includes:
Custom VPC with public and private subnets
Internet Gateway and NAT Gateway
Route Tables for public and private traffic
Security Groups following least-privilege principles
EC2 Instance hosting a simple web application
Application Load Balancer (ALB)
RDS MySQL Database (via CloudFormation)
Lambda Function for S3 event-driven processing
CloudWatch Logging Integration
The infrastructure follows a multi-tier design where the web server components reside in public subnets, and the database layer is isolated within private subnets.

2. Repository Structure
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── vpc.tf
│   ├── subnets.tf
│   ├── route_tables.tf
│   ├── security_groups.tf
│   ├── igw_nat.tf
│   ├── outputs.tf
│
├── cloudformation/
│   ├── cloudformation-app.yaml
│
├── boto3-scripts/
│   ├── create_bucket_and_upload.py
│   ├── list_ec2_instances.py
│   ├── invoke_lambda.py
│   ├── get_ec2_metadata.py
│
├── architecture-diagram.png
└── README.md

3. Terraform Implementation: Terraform is used to provision networking and foundational AWS components:
Custom VPC with CIDR blocks
Public and private subnets across multiple AZs
Route Tables and Internet/NAT gateways
Security groups for EC2, ALB, and RDS
Outputs exposing key resource IDs for downstream use

How to Deploy
terraform init
terraform validate
terraform plan
terraform apply

Destroying the Infrastructure
terraform destroy

.gitignore file is used to prevent committing sensitive files such as terraform.tfstate.

4. CloudFormation Stacks: CloudFormation templates were used to deploy application-level services:
EC2 Web Application Stack
  EC2 instance with a user-data script hosting a static web page
  ALB + Target Group
  Auto Scaling Group
  Security groups and IAM roles

RDS Stack
  MySQL database deployment
  Private subnet placement
  Multi-AZ capability

Lambda Stack
  Python Lambda function for S3 event logging
  IAM execution role
  CloudWatch integration

5. AWS Lambda: S3 Event Logging: A Python Lambda function was created to automatically log every new S3 upload.

Responsibilities
  Capture bucket name and object key
  Write structured logs to CloudWatch
  Demonstrate event-driven serverless architecture

Trigger
  S3 → “Object Created” → Lambda

6. AWS CLI Interaction: AWS CLI was used to demonstrate command-line interaction with core services.

Examples
  List Running EC2 Instances: aws ec2 describe-instances --filters Name=instance-state-name,Values=running
  Invoke Lambda Function: aws lambda invoke --function-name <lambda-name> output.json
  Create an S3 Bucket: aws s3 mb s3://mybucket-unique-id

These steps confirm operational knowledge of CLI-based resource management.

7. Python Boto3 Scripts: Python scripts were developed to automate AWS tasks programmatically.

Included Scripts
  Create S3 bucket & Upload object
  Retrieve EC2 instance metadata
  List running EC2 instances
  Invoke Lambda function programmatically

Running a Script: python create_bucket_and_upload.py

All scripts include error handling and AWS authentication via IAM roles or credentials stored in the AWS CLI configuration.

8. Architecture Diagram: A high-level architecture diagram is included to illustrate:

  VPC layout
  Network segmentation
  Routing architecture
  Application flow from user → ALB → EC2 → S3/Lambda
  Database isolation

This diagram helps visualize the deployment and is suitable for academic reports.

10. How to Reproduce the Entire Project
Prerequisites:
  AWS Account
  IAM user with administrative privileges
  AWS CLI installed and configured
  Terraform 1.x
  Python 3.9+
  boto3 and requests library

Deployment Workflow:
  Clone this repository
  Deploy Terraform networking layer
  Deploy CloudFormation application and database stacks
  Upload Lambda function code
  Configure S3 triggers
  Run Boto3 automation scripts
  Validate logs and infrastructure via AWS Console
  Clean up resources after evaluation

10. Academic Integrity & Notes: This project was developed as part of a graduate-level course requirement focusing on:
  Infrastructure-as-Code methodology
  Cloud automation
  Serverless design patterns
  Event-driven programming
  AWS service integration
All components have been independently implemented, tested, and documented.

11. Author
Sahil Shahi (IM58977)
Graduate Student – M.S. Information Systems
University of Maryland, Baltimore County
