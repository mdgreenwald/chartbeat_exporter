# Chartbeat Exporter - Kubernetes

#### Example Kubernetes Manifest: ####

**[chartbeat_exporter.yaml](chartbeat_exporter.yaml)**

**Snippet:**

```yaml
...
      - image: mdgreenwald/chartbeat_exporter:v0.1.0
        imagePullPolicy: IfNotPresent
        name: prometheus-chartbeat-exporter
        ports:
        - containerPort: 9132
        env:
          - name: CHARTBEAT_API_KEY
            valueFrom:
              secretKeyRef:
                name: prometheus-chartbeat-exporter-secret
                key: apikey
          - name: CHARTBEAT_HOST
            value: "domain1.com,domain2.org,domain3.net"
          - name: CHARTBEAT_POLL
            value: "1"
...

```

####Example Prometheus Configuration:####
```yaml
  - job_name: 'chartbeat_exporter'
    scrape_interval: 1s
    scrape_timeout: 500ms
    metrics_path: /metrics
    static_configs:
      - targets:
        - prometheus-chartbeat-exporter:9132

```
