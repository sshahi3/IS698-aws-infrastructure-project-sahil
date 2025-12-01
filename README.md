AWS Cloud Infrastructure Automation Project
A fully automated cloud deployment built using Terraform, AWS CloudFormation, AWS Lambda, API Gateway, Step Functions, and Python Boto3. This repository demonstrates multi-tier architecture design, serverless workflows, and end-to-end cloud automation following Infrastructure-as-Code principles.

Overview: This repository contains the complete implementation of an end-to-end cloud deployment project that integrates:
  Terraform
  AWS CloudFormation
  AWS Lambda
  S3
  EC2
  RDS
  Python Boto3
  API Gateway
  Step Functions
The objective is to design, automate, and validate a cloud architecture using IaC while demonstrating real-world AWS interactions using the AWS Console, AWS CLI, and Boto3.
The workflow mirrors industry practices followed by cloud engineers and DevOps teams.

Technologies Used
  Terraform – VPC, Subnets, Routing, Security Groups
  AWS CloudFormation – EC2, ALB, Auto Scaling, RDS
  AWS Lambda (Python) – S3 event processing
  Amazon S3 – Object storage and Lambda triggers
  Amazon RDS (MySQL) – Database backend
  API Gateway – HTTP-based Lambda invocation
  AWS Step Functions – Workflow orchestration
  AWS CLI – Command-line resource management
  Python Boto3 – Programmatic AWS automation

1. Project Architecture
The automated environment includes:
  Custom VPC with public and private subnets
  Internet Gateway and NAT Gateway
  Route Tables for public and private traffic
  Security Groups following least-privilege principles
  EC2 Instance hosting a simple web application
  Application Load Balancer (ALB)
  RDS MySQL Database (via CloudFormation)
  Lambda Function for S3 event-driven processing
  CloudWatch Logging Integration
The deployment follows a multi-tier architecture, where web components reside in public subnets, and the database layer is isolated within private subnets.

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

3. Terraform Implementation
Terraform provisions networking infrastructure:
  Custom VPC + CIDR
  Public & private subnets
  Internet Gateway & NAT Gateway
  Route Tables
  Security Groups
  Outputs exposing resource IDs for CloudFormation

How to Deploy
  terraform init
  terraform validate
  terraform plan
  terraform apply

Destroy
  terraform destroy

.gitignore ensures sensitive state files like terraform.tfstate are not committed.

4. CloudFormation Stacks
EC2 Web Application Stack
  EC2 instance with user-data installing Apache
  ALB + Target Group
  Auto Scaling Group
  Security groups and IAM roles

RDS Stack
  MySQL database
  Private subnet placement
  Multi-AZ capability

Lambda Stack
  Python Lambda (S3 event logging)
  IAM execution role
  CloudWatch logs

5. AWS Lambda: S3 Event Logging
The Lambda function automatically logs every new S3 upload.

Key Responsibilities
  Capture bucket name & object key
  Log to CloudWatch
  Demonstrate event-driven architecture

Trigger
  S3 (ObjectCreated) → Lambda

6. AWS CLI Interaction
Demonstrates operational AWS management using CLI.

Examples

List running EC2 instances
  aws ec2 describe-instances --filters Name=instance-state-name,Values=running

Invoke Lambda
  aws lambda invoke --function-name <lambda-name> output.json

Create S3 bucket
  aws s3 mb s3://mybucket-unique-id

7. Python Boto3 Scripts: Python scripts were developed to automate AWS tasks programmatically.

Included Scripts
  Create S3 bucket & Upload object
  Retrieve EC2 instance metadata
  List running EC2 instances
  Invoke Lambda function programmatically

Running a Script: python create_bucket_and_upload.py

All scripts include error handling and AWS authentication via IAM roles or credentials stored in the AWS CLI configuration.

8. Architecture Diagram
A high-level architecture diagram is included to illustrate:
  VPC layout
  Network segmentation
  Routing architecture
  Application flow from user → ALB → EC2 → S3/Lambda
  Database isolation
This diagram helps visualize the deployment and is suitable for academic reports.

9. Bonus Implementation: API Gateway → Lambda Integration
To extend the serverless capabilities of the infrastructure, an HTTP API Gateway was implemented and integrated with the Lambda function. This enables invocation of serverless compute through standard HTTPS requests.

Configuration
  API Type: HTTP API
  Route: ANY /
  Stage: $default
  Integration: Lambda Proxy Integration
  Region: us-east-1
  Invoke URL (example): https://<api-id>.execute-api.us-east-1.amazonaws.com/

Purpose
This bonus task demonstrates:
  API-driven serverless execution
  Lambda invocation via HTTP
  Cloud-native request handling
  Event transformation between API Gateway and Lambda

Lambda Response Output
{
  "message": "Hello from Sahil's Lambda via API Gateway!"
}

This output confirms that the API Gateway successfully triggers Lambda and returns structured JSON to the client.

10. Bonus Implementation: AWS Step Functions Workflow
A three-step AWS Step Functions workflow was created to demonstrate orchestration and automation of serverless tasks.

Workflow Overview
The State Machine coordinates three Lambda functions:
  Step1Start – Initializes the workflow
  Step2Process – Performs intermediate processing
  Step3Finish – Returns completion response

State Machine Logic
  "StartAt": "Step1",
  "States": {
    "Step1": { "Type": "Task", "Next": "Step2" },
    "Step2": { "Type": "Task", "Next": "Step3" },
    "Step3": { "Type": "Task", "End": true }
  }

Purpose
This implementation demonstrates:
  Cloud-native orchestration
  Serverless workflow automation
  Event chaining between Lambda functions
  Step-by-step visual execution using AWS Step Functions Graph Inspector

The workflow successfully executed all three steps in sequence, confirming proper orchestration and integration.

11. How to Reproduce the Entire Project
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

12. Academic Integrity & Notes:
This project was developed as part of a graduate-level course requirement focusing on:
  Infrastructure-as-Code methodology
  Cloud automation
  Serverless design patterns
  Event-driven programming
  AWS service integration
All components have been independently implemented, tested, and documented.

13. Author
Sahil Shahi (IM58977)
Graduate Student – M.S. Information Systems
University of Maryland, Baltimore County
