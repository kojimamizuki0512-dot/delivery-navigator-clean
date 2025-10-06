from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),  # ← core/urls.py へ全委譲
]
