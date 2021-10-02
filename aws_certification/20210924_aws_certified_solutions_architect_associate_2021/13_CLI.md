# 13 - CLI

Section Introduction

* So far, we've interacts with services manually and they exposed standard information for clients: 
  * EC2 exposes a standard Linux machine we can use any way we want 
  * RDS exposes a standard database we can connect to using a URL 
  * ElastiCache exposes a cache URL we can connect to using a URL 
  * ASG / ELB are automated and we don't have to program against them 
  * Route53 was setup manual

* Developing against AWS has two components: 
  * How to perform interactions with AWS without using the Online Console? 
  * How to interact with AWS Proprietary services? (S3, DynamoDB, etc...)

* Developing and performing AWS tasks against AWS can be done in several ways 
  * Using the AWS CLI on our local computer 
  * Using the AWS CLI on our EC2 machines 
  * Using the AWS SDK on our local computer 
  * Using the AWS SDK on our EC2 machines 
  * Using the AWS Instance Metadata Service for EC2

* In this section, we'll learn: 
  * How to do all of those 
  * In the right & most secure way. adhering to best practices


## 138 - AWS EC2 Instance Metadata

* AWS EC? Instance Metadata is powerful but one of the least known features to developers
* It allows AWS EC? instances to "learn about themselves” without using an IAM Role for that purpose.
* The URL is http://169.254.169.254/latest/meta-data
* You can retrieve the IAM Role name from the metadata, but you CANNOT retrieve the [AM Policy.
* Metadata = Info about the EC2 instance 
* Userdata = launch script of the EC2 instance
* Using http://169.254.169.254/latest/meta-data/iam/security-credentials/role_name it's possible to obtain the short lived credential obtained to this EC2 instance which has the AccessKey, SecretKey and Token. These are obtained in the EC2 using the IAM role.

## 139 - AWS SDK Overview

* We have to use the AWS SDK when coding against AWS Services such as DynamoDB
* Fun fact... the AWS CLI uses the Python SDK (boto3) ¢ The exam expects you to know when you should use an SDK ¢ We'll practice the AWS SDK when we get to the Lambda functions
* Good to know: if you don't specify or configure a default region, then us-east-| will be chosen by default