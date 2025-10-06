# backend/Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 依存ビルド用
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# 依存インストール
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# アプリ本体
COPY . /app

# static を集める（失敗しても先へ進む）
RUN python manage.py collectstatic --noinput || true

# 起動スクリプト
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
CMD ["/bin/sh", "/entrypoint.sh"]
