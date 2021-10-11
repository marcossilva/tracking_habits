# 16 - Extra Storage

## 167 - AWS Snow Family
Offline devices to perform data migrations
If it takes more than a week to transfer over the network, use Snowball devices!

### Snowball Edge (for data transfers)
* Physical data transport solution: move TBs or PBs of data in or out of AWS
* Alternative to moving data over the network (and paying network fees)
* Pay per data transfer job 
* Provide block storage and Amazon S3-compatible object storage
Snowball Edge Storage Optimized 
* 80TB of HDD capacity for block volume and S3 compatible object storage Snowball Edge Compute Optimized
* 42TB of HDD capacity for block volume and $3 compatible object storage
* Use cases: large data cloud migrations, DC decommission, disaster
recovery

AWS Snowcone

* Small, portable computing, anywhere, rugged & secure withstands harsh environments
* Light (4.5 pounds, 2.1 kg)
* Device used for edge computing, storage, and data transfer
* 8 TBs of usable storage
* Use Snowcone where Snowball does not fit (space-constrained environment)
* Must provide your own battery / cables
* Can be sent back to AWS offline, or connect it to internet and use AWS DataSync to send data

Snow Family — Edge Computing

* Snowcone (smaller) 
  * 2 CPUs, 4 GB of memory, wired or wireless access 
  * USB-C power using a cord or the optional battery
* Snowball Edge — Compute Optimized 
  * 52 vCPUs, 208 GiB of RAM 
  * Optional GPU (useful for video processing or machinel learning) 
  * 427B usable storage 
* Snowball Edge — Storage Optimized = 
  * Up to 40 vCPUs, 80 GiB of RAM ) 
  * Object storage clustering available ° All: Can run EC2 Instances & AWS Lambda functions (using AWS loT Greengrass)

* Long-term deployment options: | and 3 years discounted pricing

Solution Architecture: Snowball into Glacier

* Snowball cannot import to Glacier directly 
* You must use Amazon S3 first, in combination with an S3 lifecycle policy

AWS Storage Gateway Summary

* Exam tip: Read the question well, it will hint at which gateway to use * On-premises data to the cloud => Storage Gateway
* File access / NFS — user auth with Active Directory => File Gateway (backed by $3)
* Volumes / Block Storage / iSCSI => Volume gateway (backed by S3 with EBS snapshots)
* VTL Tape solution / Backup with iSCSI = > Tape Gateway (backed by S3 and Glacier)
* No on-premises virtualization => Hardware Appliance

## 172 - Amazon FSx

Amazon FSx for Windows (File Server)

* EFS is a shared POSIX system for Linux systems.
* FSx for Windows is a fully managed Windows file system share drive
* Supports SMB protocol & Windows NTFS
* Microsoft Active Directory integration, ACLs, user quotas
* Built on SSD, scale up to 10s of GB/s, millions of IOPS, 100s PB of data 
* Can be accessed from your on-premise infrastructure
* Can be configured to be Multi-AZ (high availability)
* Data is backed-up daily to S3

Amazon FSx for Lustre

* Lustre is a type of parallel distributed file system, for large-scale computing 
* The name Lustre is derived from "Linux" and "cluster"
* Machine Learning, High Performance Computing (HPC) 
* Video Processing, Financial Modeling, Electronic Design Automation 
* Scales up to |00s GB/s, millions of IOPS, sub-ms latencies
* Seamless integration with $3 
* Can “read S3"’as a file system (through FSx) 
* Can write the output of the computations back to $3 (through FSx)
* Can be used from on-premise servers

## 174 - AWS Storage Options Compared

Storage Comparison

* $3: Object Storage
* Glacier: Object Archival
* EFS: Network File System for Linux instances, POSIX filesystem
* FSx for Windows: Network File System for Windows servers
* FSx for Lustre: High Performance Computing Linux file system
* EBS volumes: Network storage for one EC2 instance at a time
* Instance Storage: Physical storage for your EC2 instance (high |OPS)
* Storage Gateway: File Gateway, Volume Gateway (cache & stored), Tape Gateway 
* Snowball / Snowmobile: to move large amount of data to the cloud, physically
* Database: for specific workloads, usually with indexing and querying