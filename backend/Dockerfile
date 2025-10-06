# Python（軽量）イメージ
FROM python:3.11-slim

# 便利な環境変数
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# 必要なら OS 依存パッケージ（今回はSQLiteのみなので最小限）
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ
WORKDIR /app

# 依存を入れる
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# アプリ本体
COPY . /app

# 静的ファイル収集（失敗しても先に進む）
RUN python manage.py collectstatic --noinput || true

# ポートは Railway が環境変数 PORT を渡す
EXPOSE 8000

# ★ここが重要：$PORT をシェル展開（未設定なら 8000）
CMD ["sh", "-c", "exec gunicorn dnbackend.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2"]
