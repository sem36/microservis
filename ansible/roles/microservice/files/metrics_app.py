from fastapi import FastAPI
from prometheus_client import start_http_server, Gauge
import platform
import subprocess
import time

app = FastAPI()
host_type_metric = Gauge('host_type', 'Host type (1=VM, 2=Container, 3=Physical)', ['type'])

def detect_host_type():
    try:
        with open('/proc/1/cgroup', 'rt') as f:
            content = f.read()
            if 'docker' in content or 'containerd' in content:
                return 'container'
    except:
        pass

    output = subprocess.getoutput("systemd-detect-virt")
    if output in ['kvm', 'vmware', 'oracle', 'qemu']:
        return 'vm'
    elif output == 'none':
        return 'physical'
    return 'unknown'

@app.get("/metrics")
def metrics():
    host_type = detect_host_type()
    val_map = {'vm': 1, 'container': 2, 'physical': 3}
    host_type_metric.labels(type=host_type).set(val_map.get(host_type, 0))
    return "OK"

if __name__ == "__main__":
    start_http_server(8080)
    while True:
        metrics()
        time.sleep(10)
