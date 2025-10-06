# C:\Users\kojim\Documents\deliveryNavigator_clean\backend\Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# OS 依存
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# Python 依存
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# プロジェクト本体
COPY . .

# 静的ファイル収集（無くても失敗しないように || true）
RUN python manage.py collectstatic --noinput || true

# Koyeb では $PORT が渡される。未設定時は 8000 にフォールバック
EXPOSE 8000
CMD ["bash","-lc","gunicorn dnbackend.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3 --timeout 60"]
