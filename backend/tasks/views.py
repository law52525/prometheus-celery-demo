import os
from django.http import JsonResponse, HttpResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from .tasks import generate_report, process_data, generate_report1, generate_report2, generate_report3
import random


def test_metrics(request):
    """手动触发任务并返回指标"""
    # 触发测试任务
    generate_report.delay("test-report-123")
    process_data.delay("test-data-456")
    
    # 直接返回指标
    return HttpResponse(
        generate_latest(),
        content_type=CONTENT_TYPE_LATEST
    )


def get_random_int():
    random_bytes = os.urandom(4)
    random_int = int.from_bytes(random_bytes, byteorder='big') % 100
    return random_int


def trigger_tasks(request):
    # 生成随机任务
    n = 80
    for i in range(n + 1):
        go = i % 5
        if go == 1:
            generate_report.delay(f"RPT-{random.randint(1000,9999)}")
        # elif go == 0:
        #     process_data.delay(f"DATA-{random.randint(1000,9999)}")
        elif go == 2:
            generate_report1.delay(f"RPT-{random.randint(1000,9999)}")
        elif go == 3:
            generate_report2.delay(f"RPT-{random.randint(1000,9999)}")
        elif go == 4:
            generate_report3.delay(f"RPT-{random.randint(1000,9999)}")
    
    return JsonResponse({"status": "Tasks triggered"})


def health_check(request):
    """
    Health check endpoint to verify that the service is running.
    """
    return JsonResponse({"status": "ok"}, status=200)