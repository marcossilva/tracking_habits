# Route 53

## 103 - Route 53 CNAME vs Alias
![](../../assets/2021-09-29-23-58-53.png)

## 104 - Routing Policy - Simple
![](../../assets/2021-09-30-00-05-17.png)

## 105 - Routing Policy - Weighted
![](../../assets/2021-09-30-00-06-34.png)
From a client side perspective, we're not aware that there are multiple IPs

## 106 - Routing Policy - Latency
![](../../assets/2021-09-30-00-10-15.png)

## 106 -Health Check
If a health check fails, Route 53 will not send traffic to that route
![](../../assets/2021-09-30-00-15-03.png)

## 108 - Routing Policy - Failover
Works by pointing the Route 53 to two instances, primary and secondary. The primary need to have a health check enabled and, in caso it goes unhealthy the traffic is redirected to the secondary.

## 109 - Routing Policy - Geolocation
Works creating rules based on geographic rules (country, continent, etc). Needs to have a Default case.

## 110 - Routing Policy - Geographic Bias
![](../../assets/2021-09-30-00-28-31.png)
Works by defining smallest latency of users x resources given a bias parameter.

## 111 - Routing Policy - Multi Value
![](../../assets/2021-09-30-00-30-43.png)
Give some fault tolerance on the client side since even if a resource goes down there are others to ask from.

## 112 - 3rd party domains
You can buy 3rd party domains and point out the name servers to the service in the Route 53 service to configure its DNS.