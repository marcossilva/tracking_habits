# 18 - ECS

## 193 - Docker Introduction

What is Docker?

* Docker is a software development platform to deploy apps 
* Apps are packaged in containers that can be run on any OS
* Apps run the same, regardless of where they're run 
  * Any machine 
  * No compatibility issues 
  * Predictable behavior 
  * Less work 
  * Easier to maintain and deploy 
  * Works with any language, any OS, any technology

Where are Docker images stored?

* Docker images are stored in Docker Repositories 
  * Public: Docker Hub https://hub.docker.com/
* Find base images for many technologies or OS: 
  * Ubuntu 
  * MySQL 
  * NodeS, Java... 
* Private: Amazon ECR (Elastic Container Registry)
* Public: Amazon ECR Public

Docker Containers Management

* To manage containers, we need a container management platform * Three choices:
* ECS: Amazon's own container platform
* Fargate: Amazon's own Serverless container platform
* EKS: Amazon's managed Kubernetes (open source)

## 194 - ECS

What is ECS?

* ECS = Elastic Container Service, Launch Docker containers on AWS
* You must provision & maintain the infrastructure (the EC2 instances)
* AWS takes care of starting / stopping containers
* Has integrations with the Application Load Balancer

What is Fargate?

* Launch Docker containers on AWS
* You do not provision the infrastructure (no EC2 instances to manage) — simpler!
* Serverless offering
* AWS just runs containers for you based on the CPU / RAM you need
* Each ECS Task is attached to a private ENI so to run many tasks it's necessary to have enough private IP addresses in the VPC

IAM Roles for ECS Tasks

* EC2 Instance Profile: 
  * Used by the ECS agent 
  * Makes API calls to ECS service 
  * Send container logs to CloudWatch Logs 
  * Pull Docker image from ECR
  * Reference sensitive data in Secrets Manager or SSM Parameter Store

* ECS Task Role:
  * Allow each task to have a specific role
  * Use different roles for the different ECS Services you run
  * Task Role is defined in the task definition

ECS Data Volumes — EFS File Systems
* Works for both EC2 Tasks and Fargate tasks
* Ability to mount EFS volumes onto
* Tasks launched in any AZ will be able to share the same data in the EFS volume
* Fargate + EFS = serverless + data storage without managing servers
* Use case: persistent multi-AZ shared storage for your containers

## 195 - ECS Services & Tasks

Load Balancing for EC2 Launch Type
* We get a dynamic port mapping
* The ALB supports finding the right port on your EC2 Instances
* You must allow on the EC2 instance’s security group any port from the ALB security group

Load Balancing for Fargate
* Each task has a unique IP
* You must allow on the ENI's security group the task port from the ALB security group

ECS tasks invoked by Event Bridge

## 197 - ECS Scaling — Service CPU Usage Example

You have two levels of scaling:
* Service Scaling (scale tasks based on CloudWatch Metric)
* Backend EC2 Capacity Provider (scales cluster EC2 instances if the machines aren t able to scale up properly)

## 198 - ECS Rolling Updates

When updating you have two parameters to control:
* Minimum health percent, defaults to 100%
* Maximum percent, defaults to 200%

The minimum health percent points out how many ECS Tasks should be kept running during update while the versions are rolling. That means the 100% keeps all the running instances.

The maximum health percent points out how many ECS Tasks should be created with the new Task version. That means the 200% allows up to 2x the instances to be created (in which the new ones will be with the new version).

## 199 - ECR Overview
Amazon ECR — Elastic Container Registry

* Store, manage and deploy containers on AWS, pay for what you use 
* Fully integrated with ECS & IAM for security, backed by Amazon S3 
* Supports image vulnerability scanning, version, tag, image lifecycle

## 200 - Amazon EKS Overview

* Amazon EKS = Amazon Elastic Kubernetes Service 
* It is a way to launch managed Kubernetes clusters on AWS
* Kubernetes is an open-source system for automatic deployment, scaling and management of containerized (usually Docker) application
* It's an alternative to ECS, similar goal but different API
* EKS supports EC2 if you want to to deploy worker nodes or Fargate to deploy serverless containers
* Use case: if your company is already using Kubernetes on-premises or in another cloud, and wants to migrate to AWS using Kubernetes
* Kubernetes is cloud-agnostic (can be used in any cloud — Azure, GCP...)
* Pods = Kubernets