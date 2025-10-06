# dnbackend/settings.py
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ────────────── 基本 ──────────────
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-only-secret-key")
DEBUG = os.getenv("DEBUG", "1") == "1"
# 例: ALLOWED_HOSTS="localhost,127.0.0.1,.koyeb.app"
ALLOWED_HOSTS = [h for h in os.getenv("ALLOWED_HOSTS", "*").split(",") if h]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "corsheaders",          # ← ここは django より下でOK
    "rest_framework",

    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Security の直後 & CommonMiddleware より前
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dnbackend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

# ────────────── DB ──────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []  # ローカル優先。必要なら適宜追加。

# ────────────── ロケール ──────────────
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

# ────────────── 静的ファイル ──────────────
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # 任意: ある場合のみ有効
STATIC_ROOT = BASE_DIR / "staticfiles"    # collectstatic 用

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ────────────── REST ──────────────
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}

# ────────────── CORS/CSRF ──────────────
# ローカルは全部許可。環境変数 CORS_ALLOW_ALL=0 で明示指定モードに切替
if os.getenv("CORS_ALLOW_ALL", "1") == "1":
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOW_ALL_ORIGINS = False
    # 例: FRONTEND_ORIGIN="https://your-frontend.koyeb.app"
    FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "").rstrip("/")
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ] + ([FRONTEND_ORIGIN] if FRONTEND_ORIGIN else [])

CORS_ALLOW_CREDENTIALS = True
# /api/ 配下だけに限定（任意だがセーフ）
CORS_URLS_REGEX = r"^/api/.*$"

# フォーム/POST に備えて CSRF 信頼元も入れておく（フロントから直POSTする場合に有効）
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
_front = os.getenv("FRONTEND_ORIGIN", "").rstrip("/")
if _front:
    CSRF_TRUSTED_ORIGINS.append(_front)

# ────────────── 逆プロキシ（Koyeb 等）向け ──────────────
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
