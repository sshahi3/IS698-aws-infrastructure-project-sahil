AWS Cloud Infrastructure Automation Project

This repository contains the complete implementation of an automated, multi-tier cloud environment developed using Terraform, AWS CloudFormation, AWS Lambda, API Gateway, Step Functions, and Python Boto3. The project follows Infrastructure-as-Code (IaC) principles and demonstrates a full workflow used by cloud engineers and DevOps teams to design, deploy, automate, and validate an AWS-based architecture.

⭐ Project Overview

This project automates every core component of a modern AWS environment, integrating:

Terraform – VPC, subnets, routing, and security

AWS CloudFormation – EC2, ALB, Auto Scaling, RDS

Lambda Functions – event-driven S3 processing

Amazon S3 – object storage + Lambda triggers

Amazon EC2 – web application hosting

Amazon RDS (MySQL) – database backend

API Gateway – HTTP-based serverless invocation

AWS Step Functions – workflow orchestration

AWS CLI – operational cloud management

Python Boto3 – programmatic AWS automation

The goal is to build a real-world, production-aligned system demonstrating automation, scalability, observability, and serverless event handling.

🚀 Technologies Used
Technology	Purpose
Terraform	Network layer (VPC, subnets, routing, SGs)
CloudFormation	Compute + database stack (EC2, ASG, ALB, RDS)
AWS Lambda	S3 event-driven processing
Amazon S3	File storage + triggers
Amazon RDS	Persistent MySQL backend
API Gateway	HTTP endpoints for Lambda
Step Functions	Orchestrated serverless workflows
AWS CLI	Resource validation + operations
Python Boto3	Scripted AWS interactions
🏗️ 1. Architecture Summary

The deployment follows a multi-tier cloud architecture consisting of:

A custom VPC with isolated public and private subnets

NAT Gateway for private subnet outbound internet access

Internet Gateway for public subnet traffic

Route Tables configured for segmentation

Security Groups following least-privilege patterns

EC2 Application Tier behind an Application Load Balancer

Auto Scaling Group for EC2 workload elasticity

Private RDS MySQL instance

Lambda function triggered by S3 uploads

CloudWatch Logs for monitoring and debugging

📌 The architecture diagram is included in the repository.

📁 2. Repository Structure
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

🌐 3. Terraform Implementation

Terraform provisions the entire network layer, including:

Custom VPC

Public & private subnets

Route tables and subnet associations

Internet Gateway & NAT Gateway

Security groups for ALB, EC2, and database

Deployment Steps
terraform init
terraform validate
terraform plan
terraform apply

Destroy Infrastructure
terraform destroy


🔒 Terraform state files are excluded via .gitignore.

🧱 4. CloudFormation Stacks

CloudFormation deployed the application layer:

EC2 Application Stack

EC2 instance with Apache auto-installation (via UserData)

Launch Template + Auto Scaling Group

Application Load Balancer + Target Group

Security Groups

RDS Stack

MySQL database in private subnets

Secure connectivity routed only from EC2

Lambda Stack

Python Lambda function for S3 upload logging

IAM execution role

CloudWatch log groups

🪝 5. AWS Lambda – S3 Event Logging

A Python-based Lambda function logs metadata whenever a file is uploaded into the S3 bucket.

Responsibilities

Capture object key + bucket name

Record structured logs in CloudWatch

Demonstrate serverless + event-driven design

Trigger
S3 (ObjectCreated) → Lambda → CloudWatch Logs

🖥️ 6. AWS CLI Interaction

The AWS CLI was used to validate resources and manage cloud components.

Examples

List running EC2 instances:

aws ec2 describe-instances --filters Name=instance-state-name,Values=running


Invoke Lambda:

aws lambda invoke --function-name <lambda-name> output.json


Create S3 bucket:

aws s3 mb s3://mybucket-unique-id

🐍 7. Python Boto3 Automation Scripts

Python scripts were developed to automate AWS operations:

Included Scripts

Create S3 bucket & upload file

Retrieve EC2 instance metadata

List running EC2 instances

Invoke Lambda programmatically

Run Any Script
python script_name.py


Scripts include exception handling, AWS authentication, and parameterization.

🗺️ 8. Architecture Diagram

The repository includes a high-level architecture diagram that illustrates:

VPC + subnet design

Routing architecture

ALB → EC2 → RDS request flow

S3 → Lambda event processing

Step Functions workflow chain

This diagram is also embedded in the final PDF report.

🎯 9. Bonus Implementation: API Gateway → Lambda

As part of extra credit, an HTTP API Gateway triggers a Lambda function via a REST endpoint.

Configuration Highlights

Route: ANY /

Stage: $default

Integration: Lambda Proxy

Output returns a JSON message

This validates HTTP-based Lambda invocation and cloud-native serverless routing.

🔄 10. Bonus Implementation: AWS Step Functions Workflow

A three-state Step Functions machine orchestrates multiple Lambda functions:

Step1Start

Step2Process

Step3Finish

The graph visually displays execution sequence and successful termination.

This demonstrates event chaining and workflow automation.

🔧 11. How to Reproduce the Entire Project
Prerequisites

AWS Account

AWS CLI configured

Terraform installed

Python 3.9+

boto3 library

Deployment Flow

Clone the repository

Run Terraform to build the network

Deploy CloudFormation to launch compute & DB

Upload Lambda code + configure S3 triggers

Run Boto3 scripts

Test end-to-end flows using Console, CLI, and API Gateway

Clean up AWS resources

📘 12. Academic Integrity & Notes

This project was developed as part of graduate coursework focusing on:

Infrastructure-as-Code

Cloud automation

Serverless architecture

Event-driven design

AWS service integration

All implementations were completed independently and tested using real AWS environments.

👤 13. Author

Sahil Shahi
Graduate Student – M.S. Information Systems
University of Maryland, Baltimore County
Student ID: IM58977
