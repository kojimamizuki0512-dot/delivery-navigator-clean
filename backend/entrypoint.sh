#!/bin/sh
set -e

python manage.py migrate --noinput

# Railway から渡される $PORT（未設定なら 8000）
: ${PORT:=8000}

exec gunicorn dnbackend.wsgi:application \
  --bind 0.0.0.0:$PORT \
  --workers 3 \
  --preload
