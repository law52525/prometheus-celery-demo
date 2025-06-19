import os
from celery import Celery
from prometheus_client import start_http_server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

app = Celery('demo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# 启动指标服务器
if 'METRICS_PORT' in os.environ:
    port = int(os.environ['METRICS_PORT'])
    start_http_server(port)
else:
    raise ValueError("METRICS_PORT environment variable is not set")

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')