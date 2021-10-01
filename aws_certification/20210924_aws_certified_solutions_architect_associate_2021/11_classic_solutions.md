# 11 - Solution Architecture

## 115 - Stateless Application: WhatsTheTime.com

In this lecture we've discussed...

* Public vs Private IP and EC2 instances
* Elastic IP vs Route 53 vs Load Balancers
* Route 53 TTL,A records and Alias Records
* Maintaining EC2 instances manually vs Auto Scaling Groups 
* Multi AZ to survive disasters
* ELB Health Checks
* Security Group Rules
* Reservation of capacity for costing savings when possible
* We're considering 5 pillars for a well architected application: costs, performance, reliability, security, operational excellence


## 116 - Stateful Web App: MyClothes.com

* MyClothes.com allows people to buy clothes online. 
* There's a shopping cart 
* Our website is having hundreds of users at the same time
* We need to scale, maintain horizontal scalability and keep our web application as stateless as possible
* Users should not lose their shopping cart 
* Users should have their details (address, etc) in a database

1) 
     * Introduce Stickiness (Session Affinity)
     * Might be gone if an instance die

2)
      * Introduce User Cookies. The information of the shopping cart is in the client-side
      * Stateless
      * HTTP requests are heavier Security risk
      * (cookies can be altered) Cookies must be validated
      * Cookies must be less than 4KB

3)
      * Introduce Server Session
      * ElastiCache / Amazon Dynamo DB
      * Store / retrieve session data

4)
      * Scaling Reads
      * Amazon RDS
      * Scale Reads with replicas

5)
      * Scaling Reads (Alternative) — Write Through
      * Uses both RDS and ElastiCache. Only access RDS when information is not on ElastiCache

6)
      * Multi AZ — Survive disasters
      * Route 53 is already multi AZ, there's no need to do anything
      * ELB is Multi AZ, inside an ASG the EC2 instances might be distributed across Multi AZ and lastly both ElastiCache and RDS are Multi AZ ready as well.
      * Restrict traffic to ElastiCache Security group from the EC2 security group

In this lecture we've discussed...

3-tier architectures for web applications (Client, Web and Database Tier)

* ELB sticky sessions * Web clients for storing cookies and making our web app stateless * ElastiCache
* For storing sessions (alternative: DynamoDB)
* For caching data from RDS ° Multi AZ
* RDS * For storing user data * Read replicas for scaling reads * Multi AZ for disaster recovery
* Tight Security with security groups referencing each other

## 117 - Stateful Web App: MyWordPress.com

* We are trying to create a fully scalable WordPress website
* We want that website to access and correctly display picture uploads
* Our user data, and the blog content should be stored in a MySQL database

1)
      * Scaling with Aurora: Multi AZ & Read Replicas
      * Aurora MySQL
      * Multi AZ
      * Read Replicas
2)
      * Storing images with EBS
      * Each instance has its own EBS volume so it adds inconsistencies
      * Only works with single instace

3)
      * Storing images with EFS
      * Through the ENI the instances can access the EFS regardless of their AZ

In this lecture we've discussed...

* Aurora Database to have easy Multi-AZ and Read-Replicas 
* Storing data in EBS (single instance application) 
* Vs Storing data in EFS (distributed application)

## 118 - Instantiating Applications quickly

* When launching a full stack (EC2, EBS, RDS), it can take time to:     
  * Install applications 
  * Insert initial (or recovery) data 
  * Configure everything 
  * Launch the application

* We can take advantage of the cloud to speed that up!


* EC2 Instances:
  * Use a Golden AMI: Install your applications, OS dependencies etc.beforehand and launch your EC2 instance from the Golden AMI
  * Bootstrap using User Data: For dynamic configuration, use User Data scripts 
  * Hybrid: mix Golden AMI and User Data (Elastic Beanstalk)

* RDS Databases: 
  * Restore from a snapshot: the database will have schemas and data ready!

* EBS Volumes:
  * Restore from a snapshot: the disk will already be formatted and have data!

## 119 - Beanstalk Overview

Developer problems on AVVS

* Managing infrastructure 
* Deploying Code 
* Configuring all the databases, load balancers, etc
* Scaling concerns
* Most web apps have the same architecture (ALB + ASG) 
* All the developers want Is for their code to run! 
* Possibly, consistently across different applications and environments


* ElasticBeanStalk is a developer centric view of deploying an application on AWS
* It uses all the component's we've seen before: EC2, ASG, ELB, RDS, etc...
* But It’s all in one view that’s easy to make sense of!
* We still have full control over the configuration
* BeanStalk is free but you pay for the underlying instances

ElasticBeanStalk

* Managed service 
* Instance configuration / OS is handled by beanstalk 
* Deployment strategy is configurable but performed by ElasticBeanStalk

* Just the application code is the responsibility of the developer

* Three architecture models: 
  * Single Instance deployment: good for dev 
  * LB + ASG: great for production or pre-production web applications 
  * ASG only: great for non-web apps in production (workers, etc..)

* ElasticBeanStalk has three components:
  * Application 
  * Application version: each deployment gets assigned a version 
  * Environment name (dev, test, prod...): free naming

* You deploy application versions to environments and can promote application versions to the next environment
* Rollback feature to previous application version 
* Full control over lifecycle of environments