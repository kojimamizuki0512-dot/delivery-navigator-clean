# ==== 1) Build frontend (Vite) ====
FROM node:20-alpine AS frontend
WORKDIR /app
COPY frontend/package*.json ./frontend/
RUN cd frontend && npm ci
COPY frontend ./frontend
RUN cd frontend && npm run build

# ==== 2) Run Django (serve static via WhiteNoise) ====
FROM python:3.11-slim AS backend
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# system deps (Pillow等は要らないので最小)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# backend を先にコピー（requirements インストールのキャッシュを効かせる）
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# ソース配置
COPY backend ./backend

# フロントの成果物を Django に同梱
#   - /app/frontend_dist へ一旦コピー
#   - index.html を Django の templates に、残りを static に入れる
COPY --from=frontend /app/frontend/dist /app/frontend_dist
RUN mkdir -p backend/templates backend/static/frontend \
 && cp -f /app/frontend_dist/index.html backend/templates/index.html \
 && cp -rf /app/frontend_dist/* backend/static/frontend/

# collectstatic（WhiteNoiseで配信）
WORKDIR /app/backend
RUN python manage.py collectstatic --noinput

# 本番用設定
ENV PORT=8000 \
    DJANGO_SETTINGS_MODULE=dnbackend.settings \
    PYTHONPATH=/app/backend

EXPOSE 8000
CMD ["gunicorn", "dnbackend.wsgi:application", "--bind", "0.0.0.0:8000", "--preload"]
