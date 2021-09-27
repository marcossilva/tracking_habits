Vertical Scalability = t2.micro -> t2.large
Horizontal Scalability = 1 instance -> 10 instances
High Availability = Horizontal Scalability + System Running in at least 2 data centers (the objective is to survive a data center loss)
# ELB - Elastic Load Balancer

A Load balancer is an interface of EC2 instances which serve traffic seamlessly to the instances. An ELB:

* Expose a single point of access (DNS) of your application
* Do regular health checks
* Separate public and private IPs

3 kinds of load balancers:

1) Classic Load Balancer (v1 - old generation) - 2009:
   * HTTP, HTTPS, TCP
2) Application Load Balancer (v2 - new generation) - 2016:
   * HTTP, HTTPS, WebSocket
3) Network Load Balancer (v3 - ner generation) - 2017:
   * TCP, TLS (secure TCP), & UDP

A classic setup is expose the load balancer to the world trhough the Security Group but only allow the instances to receive traffic from the Load Balancer, so no instance is directly exposed.

## 75 - Application Load Balancer (ALB) v2

![](../../assets/2021-09-25-00-36-58.png)

![](../../assets/2021-09-25-00-37-14.png)

![](../../assets/2021-09-25-00-37-34.png)

![](../../assets/2021-09-25-00-37-56.png)

## 77 - Network Load Balancer (NLB)

![](../../assets/2021-09-25-00-45-35.png)

## 79 - Load Balancer Stickiness

![](../../assets/2021-09-25-20-18-42.png)

## 80 - Cross Zone

![](../../assets/2021-09-25-20-22-30.png)

![](../../assets/2021-09-25-20-23-48.png)

## 82- Connection Draining

![](../../assets/2021-09-25-20-55-35.png)

## 83 - Auto Scaling Group (ASG)

![](../../assets/2021-09-25-21-24-19.png)
![](../../assets/2021-09-25-21-23-37.png)
Scale out = increase instances
Scale in = reduce instances

## 85 - Auto Scaling Groups

![](../../assets/2021-09-25-22-08-25.png)
![](../../assets/2021-09-25-22-08-46.png)

## 86 - ASG for Solutions Architects

![](../../assets/2021-09-27-00-02-55.png)
![](../../assets/2021-09-27-00-03-28.png)
![](../../assets/2021-09-27-00-05-20.png)

