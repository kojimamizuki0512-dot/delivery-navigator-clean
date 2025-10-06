# C:\Users\kojim\Documents\deliveryNavigator_clean\backend\core\urls.py
from django.urls import path
from .views import heatmap_data, daily_route, daily_summary, weekly_forecast, upload_screenshot

urlpatterns = [
    path("heatmap-data/", heatmap_data),
    path("daily-route/", daily_route),
    path("daily-summary/", daily_summary),
    path("weekly-forecast/", weekly_forecast),
    path("upload-screenshot/", upload_screenshot),
]
