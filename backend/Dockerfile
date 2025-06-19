FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000