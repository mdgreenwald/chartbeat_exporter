from prometheus_client import start_http_server, Gauge
import urllib3
import json
import time
import os

http = urllib3.PoolManager()

chartbeat_root = "http://api.chartbeat.com/live/quickstats/v3"
chartbeat_api_key = os.environ.get('CHARTBEAT_API_KEY')
chartbeat_host = os.environ.get('CHARTBEAT_HOST')
chartbeat_poll = float(os.environ.get('CHARTBEAT_POLL'))

chartbeat_url = chartbeat_root + "/?apikey=" + chartbeat_api_key + "&host="

def collect_people(host):
    r = http.request('GET', chartbeat_url + host)
    j = json.loads(r.data.decode('utf-8'))
    return j['people']

g = Gauge('chartbeat_concurrents', 'Number of people', ['chartbeat_site'])

def f():
    groups = {k:k for k in chartbeat_host.split(',')}
    for key in groups:
        g.labels(chartbeat_site=key).set(collect_people(groups[key]))

if __name__ == '__main__':
    start_http_server(9132)
    while True:
        time.sleep(chartbeat_poll)
        f()
