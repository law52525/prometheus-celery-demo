import time
import random
import logging
from celery import shared_task
from prometheus_client import Counter, Histogram

logger = logging.getLogger(__name__)

# 定义 Prometheus 指标
TASKS_STARTED = Counter('tasks_started', 'Started tasks', ['task_name'])
TASKS_COMPLETED = Counter('tasks_completed', 'Completed tasks', ['task_name'])
TASKS_FAILED = Counter('tasks_failed', 'Failed tasks', ['task_name'])
TASK_DURATION = Histogram('task_duration_seconds', 'Task duration', ['task_name'])

@shared_task(name="tasks.generate_report")  # 显式指定任务名
def generate_report(report_id):
    task_name = generate_report.name
    logger.info(f"Starting {task_name} report generation: {report_id}")
    TASKS_STARTED.labels(task_name=task_name).inc()
    
    start_time = time.time()
    try:
        # 模拟报告生成
        time.sleep(random.uniform(0.5, 5))
        
        # 10% 概率失败
        if random.random() < 0.1:
            raise ValueError("Report generation failed")
            
        TASKS_COMPLETED.labels(task_name=task_name).inc()
        logger.info(f"Report {task_name} generated: {report_id}")
        return f"Report {report_id} generated"
    except Exception as e:
        TASKS_FAILED.labels(task_name=task_name).inc()
        raise
    finally:
        duration = time.time() - start_time
        TASK_DURATION.labels(task_name=task_name).observe(duration)


@shared_task(name="tasks.process_data")  # 显式指定任务名
def process_data(data_id):
    task_name = process_data.name
    logger.info(f"Processing {task_name} data: {data_id}")
    TASKS_STARTED.labels(task_name=task_name).inc()
    
    start_time = time.time()
    try:
        # 模拟数据处理
        time.sleep(random.uniform(0.2, 3))
        
        # 5% 概率失败
        if random.random() < 0.05:
            raise RuntimeError("Data processing error")
            
        TASKS_COMPLETED.labels(task_name=task_name).inc()
        logger.info(f"Data {task_name} processed: {data_id}")
        return f"Data {data_id} processed"
    except Exception as e:
        TASKS_FAILED.labels(task_name=task_name).inc()
        raise
    finally:
        duration = time.time() - start_time
        TASK_DURATION.labels(task_name=task_name).observe(duration)


@shared_task(name="tasks.generate_report1", queue="celery-worker1")  # 显式指定任务名
def generate_report1(report_id):
    task_name = generate_report1.name
    logger.info(f"Starting {task_name} report generation: {report_id}")
    TASKS_STARTED.labels(task_name=task_name).inc()
    
    start_time = time.time()
    try:
        # 模拟报告生成
        time.sleep(random.uniform(0.5, 5))
        
        # 10% 概率失败
        if random.random() < 0.1:
            raise ValueError("Report generation failed")
            
        TASKS_COMPLETED.labels(task_name=task_name).inc()
        logger.info(f"Report {task_name} generated: {report_id}")
        return f"Report {report_id} generated"
    except Exception as e:
        TASKS_FAILED.labels(task_name=task_name).inc()
        raise
    finally:
        duration = time.time() - start_time
        TASK_DURATION.labels(task_name=task_name).observe(duration)


@shared_task(name="tasks.generate_report2", queue="celery-worker2")  # 显式指定任务名
def generate_report2(report_id):
    task_name = generate_report2.name
    logger.info(f"Starting {task_name} report generation: {report_id}")
    TASKS_STARTED.labels(task_name=task_name).inc()
    
    start_time = time.time()
    try:
        # 模拟报告生成
        time.sleep(random.uniform(0.5, 5))
        
        # 10% 概率失败
        if random.random() < 0.1:
            raise ValueError("Report generation failed")
            
        TASKS_COMPLETED.labels(task_name=task_name).inc()
        logger.info(f"Report {task_name} generated: {report_id}")
        return f"Report {report_id} generated"
    except Exception as e:
        TASKS_FAILED.labels(task_name=task_name).inc()
        raise
    finally:
        duration = time.time() - start_time
        TASK_DURATION.labels(task_name=task_name).observe(duration)


@shared_task(name="tasks.generate_report3", queue="celery-worker3")  # 显式指定任务名
def generate_report3(report_id):
    task_name = generate_report3.name
    logger.info(f"Starting {task_name} report generation: {report_id}")
    TASKS_STARTED.labels(task_name=task_name).inc()
    
    start_time = time.time()
    try:
        # 模拟报告生成
        time.sleep(random.uniform(0.5, 5))
        
        # 10% 概率失败
        if random.random() < 0.1:
            raise ValueError("Report generation failed")
            
        TASKS_COMPLETED.labels(task_name=task_name).inc()
        logger.info(f"Report {task_name} generated: {report_id}")
        return f"Report {report_id} generated"
    except Exception as e:
        TASKS_FAILED.labels(task_name=task_name).inc()
        raise
    finally:
        duration = time.time() - start_time
        TASK_DURATION.labels(task_name=task_name).observe(duration)
