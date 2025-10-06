from pathlib import Path
import os

# ─────────────────────────────────────────────────────────
# 基本
# ─────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-secret-key")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# 例: "example.com,api.example.com"
ALLOWED_HOSTS = [h for h in os.environ.get("ALLOWED_HOSTS", "*").split(",") if h]

# Railway などリバースプロキシ越しで HTTPS を正しく判定
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

# ─────────────────────────────────────────────────────────
# アプリ
# ─────────────────────────────────────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "corsheaders",

    "core",
]

# ─────────────────────────────────────────────────────────
# ミドルウェア（WhiteNoise は Security の直後、CORS は Common の前）
# ─────────────────────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",          # ★必須：静的配信
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",               # ★Common より前
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dnbackend.urls"

# ─────────────────────────────────────────────────────────
# テンプレート
#   Dockerfile で frontend/dist/index.html を
#   backend/templates/index.html にコピーします
# ─────────────────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   # ← ここが重要
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dnbackend.wsgi.application"

# ─────────────────────────────────────────────────────────
# DB（SQLite）
# ─────────────────────────────────────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []  # 必要なら後で設定

# ─────────────────────────────────────────────────────────
# ロケール
# ─────────────────────────────────────────────────────────
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

# ─────────────────────────────────────────────────────────
# 静的ファイル（WhiteNoise 前提）
#   Dockerfile で collectstatic を実行します
# ─────────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # 無ければ空ディレクトリでもOK
STATIC_ROOT = BASE_DIR / "staticfiles"

# Django 4+ の推奨：STORAGES で WhiteNoise を指定
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ─────────────────────────────────────────────────────────
# CORS / REST
# ─────────────────────────────────────────────────────────
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}

# 本番で CSRF オリジンを縛りたい時用（カンマ区切り）
CSRF_TRUSTED_ORIGINS = [
    o for o in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if o
]
