import requests
import time
import random

while True:
    print(requests.get("http://localhost:8000/trigger-tasks/").json())
    time.sleep(random.random() * 10 + random.randint(1, 5))  # 随机等待1到15秒
