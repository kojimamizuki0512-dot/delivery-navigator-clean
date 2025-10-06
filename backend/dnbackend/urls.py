# C:\Users\kojim\Documents\deliveryNavigator_clean\backend\dnbackend\urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
    path("healthz", lambda r: HttpResponse("ok")),
]
