# 14 - Athena

## 140 - S3 MFA-Delete

* MFA (multi factor authentication) forces user to generate a code on a device (usually a mobile phone or hardware) before doing important operations on S3
* To use MFA-Delete, enable Versioning on the S3 bucket 
* You will need MFA to
  * permanently delete an object version 
  * suspend versioning on the bucket 
* You won't need MFA for 
  * enabling versioning 
  * listing deleted versions
* Only the bucket owner (root account) can enable/disable MFA-Delete

## 142 - S3 Access Logs

* For audit purpose, you may want to log all access to $3 buckets
* Any request made to S3, from any account, authorized or denied, will be logged into another S3 bucket
* That data can be analyzed using data analysis tools... 
* Or Amazon Athena as we'll see later in this section!

S3 Access Logs: Warning

* Do not set your logging bucket to be the monitored bucket 
* It will create a logging loop, and your bucket will grow in size exponentially

## 144 - S3 Replication (CRR & SRR)

* Must enable versioning in source and destination 
  * Cross Region Replication (CRR)
  * Same Region Replication (SRR)
* Buckets can be in different accounts
* Copying Is asynchronous [ e Must give proper IAM permissions to S3 ..
* CRR - Use cases: compliance, lower latency access, replication across accounts
* SRR — Use cases: log aggregation, live replication between production and test accounts

53 Replication — Notes
* After activating, only new objects are replicated (not retroactive)
* For DELETE operations: 
  * If you delete without a version ID, it adds a delete marker, not replicated 
  * If you delete with a version ID, it deletes in the source, not replicated

* There is no ‘chaining’ of replication 
  * If bucket | has replication into bucket 2, which has replication into bucket 3 
  * Then objects created in bucket | are not replicated to bucket 3

## 146 - 53 pre-signed URLs

* Can generate pre-signed URLs using SDK or CLI 
  * For downloads (easy, can use the CLI) 
  * For uploads (harder, must use the SDK)
* Valid for a default of 3600 seconds, can change timeout with --expires-in [ TIME_BY_SECONDS] argument
* Users given a pre-signed URL inherit the permissions of the person who generated the URL for GET / PUT
* Examples : 
  * Allow only logged-in users to download a premium video on your S3 bucket 
  * Allow an ever changing list of users to download files by generating URLs dynamically
  * Allow temporarily a user to upload a file to a precise location in our bucket

```
 # do not forget to region parameter! (make sure it's the proper region you're choosing) aws Ss3 presign s3://mybucket/myobject --region my-region

# add a custom expiration time aws s3 presign s3://mybucket/myobject --expires-in 300 --region my-region

# IF YOU ARE GETTING ISSUES # set the proper signature version in order not to get issues

when generating URLs for encrypted files aws configure set default.s3.signature_version s3vqj
```

## 148 - S3 Storage Classes

* Amazon $3 Standard - General Purpose
* Amazon S3 Standard-Infrequent Access (IA) 
* Amazon S3 One Zone-Infrequent Access
* Amazon S3 Intelligent Tiering
* Amazon Glacier
* Amazon Glacier Deep Archive
* Amazon $3 Reduced Redundancy Storage (deprecated - omitted)

### S3 Standard — General Purpose

* High durability (99.999999999%) of objects across multiple AZ
* If you store 10,000,000 objects with Amazon S3, you can on average expect to incur a loss of a single object once every 10,000 years
* 99.99% Availability over a given year 
* Sustain 2 concurrent facility failures
* Use Cases: Big Data analytics, mobile & gaming applications, content distribution...

### S3 Standard — Infrequent Access (IA)

* Suitable for data that is less frequently accessed, but requires rapid access when needed
* High durability (99.999999999%) of objects across multiple AZs © 99.9% Availability
* Low cost compared to Amazon $3 Standard
* Sustain 2 concurrent facility failures
* Use Cases: As a data store for disaster recovery, backups...

### S3 One Zone - Infrequent Access (IA)

* Same as IA but data Is stored in a single AZ
* High durability (99.999999999%) of objects in a single AZ; data lost when AZ is destroyed
* 99.5% Availability
* Low latency and high throughput performance
* Supports SSL for data at transit and encryption at rest * Low cost compared to IA (by 20%)
* Use Cases: Storing secondary backup copies of on-premise data, or storing data you can recreate

### S3 Intelligent Tiering

* Same low latency and high throughput performance of $3 Standard 
* Small monthly monitoring and auto-tiering fee
* Automatically moves objects between two access tiers based on changing access patterns
* Designed for durability of 99.999999999% of objects across multiple Availability Zones
* Resilient against events that impact an entire Availability Zone 
* Designed for 99.9% availability over a given year

### Amazon Glacier

* Low cost object storage meant for archiving / backup
* Data is retained for the longer term (10s of years)
* Alternative to on-premise magnetic tape storage
* Average annual durability is 99.999999999%
* Cost per storage per month ($0.004 / GB) + retrieval cost 
* Each item in Glacier is called ‘‘Archive”’ (up to 40TB)
* Archives are stored in '’Vaults”’

### Amazon Glacier & Glacier Deep Archive

* Amazon Glacier — 3 retrieval options: 
  * Expedited (1 to 5 minutes) 
  * Standard (3 to 5 hours) 
  * Bulk (5 to 12 hours) 
  * Minimum storage duration of 90 days

* Amazon Glacier Deep Archive — for long term storage — cheaper: 
  * Standard (12 hours) 
  * Bulk (48 hours) 
  * Minimum storage duration of 180 days

## 150 - S3 — Moving between storage classes

* You can transition objects between storage classes
* For infrequently accessed object, move them to STANDARD_IA
* For archive objects you don't need in real-time, GLACIER or DEEP_ARCHIVE
* Moving objects can be automated using a lifecycle configuration

S3 Lifecycle Rules

* Tension actions: It defines when objects are transitioned to another storage Class. 
  * Move objects to Standard IA class 60 days after creation 
  * Move to Glacier for archiving after 6 months

* Expiration actions: configure objects to expire (delete) after some time 
  * Access log files can be set to delete after a 365 days 
  * Can be used to delete old versions of files (if versioning is enabled) 
  * Can be used to delete incomplete multi-part uploads

* Rules can be created for a certain prefix (ex - s3://mybucket/mp3/*) 
* Rules can be created for certain objects tags (ex - Department: Finance)

S3 Lifecycle Rules — Scenario |

* Your application on EC2 creates images thumbnails after profile photos are uploaded to Amazon $3. These thumbnails can be easily recreated, and only need to be kept for 45 days. The source images should be able to be immediately retrieved for these 45 days, and afterwards, the user can wait up to 6 hours. How would you design this?

* S3 source images can be on STANDARD, with a lifecycle configuration to transition them to GLACIER after 45 days.
* S3 thumbnails can be on ONEZONE_IA, with a lifecycle configuration to expire them (delete them) after 45 days.

S3 Lifecycle Rules — Scenario 2

* A rule in your company states that you should be able to recover your deleted S3 objects immediately for |5 days, although this may happen rarely. After this time, and for up to 365 days, deleted objects should be recoverable within 48 hours.

* You need to enable S3 versioning in order to have object versions, so that "deleted objects" are in fact hidden by a "delete marker" and can be recovered
* You can transition these “‘noncurrent versions” of the object to $3_IA
* You can transition afterwards these “noncurrent versions” to DEEP_ARCHIVE

## 152 - S3 Analytics — Storage Class Analysis 
* You can setup 53 Analytics to help determine when to transition objects from Standard to Standard_lA
* Does not work for ONEZONE_IA or GLACIER
* Report Is updated daily 
* Takes about 24h to 48h hours to first start
* Good first step to put together Lifecycle Rules (or improve them)!

## 153 - S3 — Baseline Performance

* Amazon $3 automatically scales to high request rates, latency |00-200 ms
* Your application can achieve at least 3,500 PUT/COPY/POST/DELETE and 5,500 GET/HEAD requests per second per prefix in a bucket.
* There are no limits to the number of prefixes in a bucket.
* Example (object path => prefix):
* bucket/folder1/sub1/file => /folder1/sub1/ 
* bucket/folder1/sub2/file => /folder1/sub2/ 
* bucket/1/file => /1/ 
* bucket/2/file => /2/
* If you spread reads across all four prefixes evenly, you can achieve 22,000 requests per second for GET and HEAD

S3 — KMS Limitation

* If you use SSE-KMS, you may be impacted by the KMS limits
* When you upload, it calls the GenerateDataKey KMS API
* When you download, it calls the Decrypt KMS API
* Count towards the KMS quota per second (5500, 10000, 30000 req/s based on region)
* As of today, you cannot request a quota increase for KMS
* If you have more than 10.000 requests in a region that only suppoer 5000 you'll be throthled.

S3 Performance

* Multi-Part upload: 
  * recommended for files > 1OOMB, must use for files > 5GB 
  * Can help parallelize uploads (speed up transfers)

* S3 Transfer Acceleration
  * Increase transfer speed by transferring file to an AWS edge location which will forward the data to the S3 bucket in the target region
  * Compatible with multi-part upload

S3 Performance — S3 Byte-Range Fetches

* Parallelize GETs by requesting specific byte ranges
* Better resilience in case of failures
* Can be used to speed up downloads
* Can be used to retrieve only partial data (for example the head of a file)

## 154 - S3 Select & Glacier Select

* Retrieve less data using SQL by performing server side filtering 
* Can filter by rows & columns (simple SQL statements) 
* Less network transfer, less CPU cost client-side

## 155 - $3 Event Notifications

* S3:ObjectCreated, $3:ObjectRemoved, S3:ObjectRestore, S3:Replication...
* Object name filtering possible (*.jpg) 
* Use case; generate thumbnails of images uploaded to $3 
* Can create as many ‘'S3 events” as desired
* S3 event notifications typically deliver events in seconds but can sometimes take a minute or longer
* If two writes are made to a single non-versioned object at the same time, it is possible that only a single event notification will be sent
* If you want to ensure that an event notification is sent for every successful write, you can enable versioning on your bucket.

## 157 - S3 — Requester Pays

* In general, bucket owners pay for all Amazon S3 storage and data transfer costs associated with their bucket
* With Requester Pays buckets, the requester instead of the bucket owner pays the cost of the request and the data download from the bucket
* Helpful when you want to share large datasets with other accounts
* The requester must be authenticated in AWS (cannot be anonymous)
* Chamada a Cobrar

## 158 - AWS Athena

* Serverless service to perform analytics directly against S3 files
* Uses SQL language to query the files
* Has a JOBC / ODBC driver
* Charged per query and amount of data scanned
* Supports CSV, JSON, ORC, Avro, and Parquet (built on Presto)
* Use cases: Business intelligence / analytics / reporting, analyze & query VPC Flow Logs, ELB Logs, CloudTrail trails, etc...
* Exam Tip: Analyze data directly on S3 => use Athena

## 160 - Glacier Vault Lock

* Adopt aWORM (Write Once Read Many) model
* Lock the policy for future edits (can no longer be changed)
* Helpful for compliance and data retention

S3 Object Lock (versioning must be enabled)

* Adopt a WORM (Write Once Read Many) model * Block an object version deletion for a specified amount of time
* Object retention: 
  * Retention Period: specifies a fixed period 
  * Legal Hold: same protection, no expiry date

* Modes:
  * Governance mode: users can't overwrite or delete an object version or alter its lock settings unless they have special permissions
  * Compliance mode: a protected object version can't be overwritten or deleted by any user, including the root user in your AWS account. When an object is locked in compliance mode, its retention mode can't be changed, and its retention period can't be shortened.