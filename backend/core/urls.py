from django.urls import path
from . import views

urlpatterns = [
    path("heatmap-data/", views.heatmap_data, name="heatmap-data"),
    path("daily-route/", views.daily_route, name="daily-route"),
    path("daily-summary/", views.daily_summary, name="daily-summary"),
    path("weekly-forecast/", views.weekly_forecast, name="weekly-forecast"),
    path("upload-screenshot/", views.upload_screenshot, name="upload-screenshot"),
]
