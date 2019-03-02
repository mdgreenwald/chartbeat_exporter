# Chartbeat exporter
Exporter for [chartbeat](https://chartbeat.com/) concurrent metrics [https://prometheus.io/](https://prometheus.io/)

This exporter for prometheus makes a request to the chartbeat quickstats/v3 API and returns the number of concurrents (people) on the requested domain.

chartbeat exporter can be used to get the number of concurrents into prometheus and perhaps a dashboard such as grafana.

## Features

* Simply returns number of concurrents (people) from the quickstats/v3 API for a given domain(s) as `chartbeat_concurrents`
* Labels each requested site with the domain as `chartbeat_site`

```txt
chartbeat_concurrents{chartbeat_site="domain1.com"} 1.0
chartbeat_concurrents{chartbeat_site="domain2.org"} 39.0
chartbeat_concurrents{chartbeat_site="domain3.net"} 63.0
```

## Configuration

Exposes metrics at `0.0.0.0:9132/metrics`

* `CHARTBEAT_API_KEY` = `4bTOp80NVxF7m4LupW4VzZqcfY8njE1r`
* `CHARTBEAT_HOST` = `domain.com` OR `domain1.com,domain2.org,domain3.net`
* `CHARTBEAT_POLL=` = `#` seconds OR `.###` milliseconds**†**

**†** *Chartbeat rate limit is 200 requests per minute*.[[1]](http://support.chartbeat.com/docs/api.html)

## Run Locally

```bash
docker run \
-e "CHARTBEAT_API_KEY=4bTOp80NVxF7m4LupW4VzZqcfY8njE1r" \
-e "CHARTBEAT_HOST=domain1.com,domain2.org,domain3.net" \
-e "CHARTBEAT_POLL=.500" \
-p 9132:9132 \
chartbeat_exporter:latest
```