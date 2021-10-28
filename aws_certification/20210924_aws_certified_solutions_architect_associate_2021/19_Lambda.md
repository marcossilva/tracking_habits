# Serverless

What's serverless?

* Serverless is a new paradigm in which the developers don’t have to manage servers anymore...
* They just deploy code 
* They just deploy... functions ! 
* Initially... Serverless == FaaS (Function as a Service)
* Serverless was pioneered by AWS Lambda but now also includes anything that’s managed: “databases, messaging, storage, etc.’
* Serverless does not mean there are no servers... it means you just don't manage / provision / see them

Serverless in AWS

* AWS Lambda
* DynamoDB
* AWS Cognito
* AWS API Gateway
* Amazon $3
* AWS SNS & SQS
* AWS Kinesis Data Firehose 
* Aurora Serverless
* Step Functions
* Fargate

## 203 - AWS Lambda

EC2:
* Virtual Servers in the Cloud
* Limited by RAM and CPU
* Continuously running
* Scaling means intervention to add / remove servers

Lambda:
* Virtual functions — no servers to manage!
* Limited by time - short executions
* Run on-demand
* Scaling is automated

* Easy Pricing: 
  * Pay per request and compute time 
  * Free tier of 1,000,000 AWS Lambda requests and 400,000 GBs of compute time
* Integrated with the whole AWS suite of services
* Integrated with many programming languages
* Easy monitoring through AWS CloudWatch
* Easy to get more resources per functions (up to 10GB of RAM!) 
* Increasing RAM will also improve CPU and network!

AWS Lambda language support

* Node,js (JavaScript)
* Python
* Java (Java 8 compatible)
* C# (.NET Core)
* Golang
* C# / Powershell
* Ruby
* Custom Runtime API (community supported, example Rust)
* Lambda Container Image 
  * The container image must implement the Lambda Runtime API
  * ECS / Fargate is preferred for running arbitrary Docker images

Applications
* Thumbnail images on S3
* Serverless CRON Job

AWS Lambda Limits to Know - per region

* Execution: 
  * Memory allocation: 128 MB - 1OGB (64 MB increments) 
  * Maximum execution time: 900 seconds (15 minutes) 
  * Environment variables (4 KB) 
  * Disk capacity in the "function container" (in /tmp): 512 MB 
  * Concurrency executions: 1000 (can be increased)

* Deployment: 
  * Lambda function deployment size (compressed .zip): 50 MB 
  * Size of uncompressed deployment (code + dependencies): 250 MB 
  * Can use the /tmp directory to load other files at startup 
  * Size of environment variables: 4 KB

## 207 - DynamoDB

DynamoDB

* Fully Managed, Highly available with replication across 3 AZ 
* NoSQL database - not a relational database 
* Scales to massive workloads, distributed database
* Millions of requests per seconds, trillions of row, 100s of TB of storage 
* Fast and consistent in performance (low latency on retrieval)
* Integrated with IAM for security, authorization and administration
* Enables event driven programming with DynamoDB Streams
* Low cost and auto scaling capabilities

* DynamoDB is made of tables
* Each table has a primary key (must be decided at creation time) 
* Each table can have an infinite number of items (= rows)
* Each tem has attributes (can be added over time — can be null) 
* Maximum size of a tem is 400KB
* Data types supported are: 
  * Scalar Types: String, Number, Binary, Boolean, Null 
  * Document Types: List, Map 
  * Set Types: String Set, Number Set, Binary Set

DynamoDB — Provisioned Throughput

* Table must have provisioned read and write capacity units
* Read Capacity Units (RCU): throughput for reads ($0.00013 per RCU) 
  * 1 RCU = 1 strongly consistent read of 4 KB per second 
  * 1 RCU = 2 eventually consistent read of 4 KB per second
* Write Capacity Units (WCU): throughput for writes ($0.00065 per WCU) 
  * 1 WCU = 1 write of 1 KB per second
* Option to setup auto-scaling of throughput to meet demand
* Throughput can be exceeded temporarily using "burst credit"
* If burst credit are empty, you'll get a "ProvisionedThroughputException". 
* It's then advised to do an exponential back-off retry

## 209 - DynamoDB - DAX

* DAX = DynamoDB Accelerator
* Seamless cache for DynamoDB, no application rewrite
* Writes go through DAX to DynamoDB
* Micro second latency for cached reads & queries 
* Solves the Hot Key problem (too many reads)
* 5 minutes TTL for cache by default
* Up to 10 nodes in the cluster
* Multi AZ (3 nodes minimum recommended for production)
* Secure (Encryption at rest with KMS,VPC, IAM, CloudTrail.. )

DynamoDB Streams

* Changes in DynamoDB (Create, Update, Delete) can end up in a DynamoDB Stream
* This stream can be read by AWS Lambda, and we can then do: 
  * React to changes in real time (welcome email to new users) 
  * Analytics 
  * Create derivative tables / views 
  * Insert into ElasticSearch
* Could implement cross region replication using Streams

* Transactions:
  * All or nothing type of operations 
  * Coordinated Insert, Update & Delete across multiple tables 
  * Include up to 10 unique items or up to 4 MB of data

* On Demand:
  * No capacity planning needed (WCU / RCV) — scales automatically 
  * 2.5x more expensive than provisioned capacity (use with care) 
  * Helpful when spikes are un-predictable or the application is very low throughput
* Security: 
  * VPC Endpoints available to access DynamoDB without internet 
  * Access fully controlled by IAM 
  * Encryption at rest using KMS 
  * Encryption in transit using SSL/TLS
* Backup and Restore feature available 
  * Point in time restore like RDS 
  * No performance impact
* Global Tables 
  * Multi region, fully replicated, high performance
* Amazon DMS can be used to migrate to DynamoDB (from Mongo, Oracle, MySQL, S3, etc...)
* You can launch a local DynamoDB on your computer for development purposes

* Global Tables: (cross region replication)
  * Active Active replication, many regions
  * Must enable DynamoDB Streams
  * Useful for low latency, DR purposes

* Capacity planning:
  * Planned capacity: provision WCU & RCU, can enable auto scaling
  * On-demand capacity: get unlimited WCU & RCU, no throttle, more expensive

## 210 - AWS API Gateway

* AWS Lambda + API Gateway: No infrastructure to manage 
* Support for the WebSocket Protocol
* Handle API versioning (v!, v2...)
* Handle different environments (dey, test, prod...)
* Handle security (Authentication and Authorization)
* Create API keys, handle request throttling
* Swagger / Open API import to quickly define APIs
* Transform and validate requests and responses
* Generate SDK and API specifications
* Cache API responses

* Lambda Function
  * Invoke Lambda function
  * Easy way to expose REST API backed by AWS Lambda
* HTTP
  * Expose HTTP endpoints in the backend
  * Example: internal HTTP API on premise, Application Load Balancer...
  * Why? Add rate limiting, caching, user authentications, API keys, etc...
* AWS Service
  * Expose any AWS API through the API Gateway?
  * Example: start an AWS Step Function workflow, post a message to SQS
  * Why? Add authentication, deploy publicly, rate control...

* Edge-Optimized (default): For global clients
  * Requests are routed through the CloudFront Edge locations (improves latency)
  * The API Gateway still lives in only one region
* Regional:
  * For clients within the same region
  * Could manually combine with CloudFront (more control over the caching
strategies and the distribution)
* Private:
  * Can only be accessed from your VPC using an interface VPC endpoint (ENI)
  * Use a resource policy to define access

## 213 - AWS Cognito [=k

* We want to give our users an identity so that they can interact with our application. 
* Cognito User Pools: 
  * Sign in functionality for app users 
  * Integrate with API Gateway 
* Cognito Identity Pools (Federated Identity): 
  * Provide AWS credentials to users so they can access AWS resources directly 
  * Integrate with Cognito User Pools as an identity provider 
* Cognito Sync: 
  * Synchronize data from device to Cognito. 
  * May be deprecated and replaced by AppSync

## 214 - AWS SAM - Serverless Application Model ;

* SAM = Serverless Application Model : 
* Framework for developing and deploying serverless applications
* All the configuration is YAML code 
  * Lambda Functions 
  * DynamoDB tables 
  * API Gateway 
  * Cognito User Pools

* SAM can help you to run Lambda, API Gateway, DynamoDB locally 
* SAM can use CodeDeploy to deploy Lambda functions