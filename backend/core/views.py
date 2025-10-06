# C:\Users\kojim\Documents\deliveryNavigator_clean\backend\core\views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def heatmap_data(request):
    data = [
        {"lat": 35.6585, "lng": 139.7013, "intensity": 0.9, "restaurants": ["A飯店", "Bカフェ", "Cバーガー"]},
        {"lat": 35.6610, "lng": 139.7038, "intensity": 0.7, "restaurants": ["Dラーメン", "Eピザ"]},
        {"lat": 35.6555, "lng": 139.6990, "intensity": 0.5, "restaurants": ["Fストア"]},
    ]
    return Response(data)

@api_view(["GET"])
def daily_route(request):
    data = {
        "recommended_area": "渋谷エリア",
        "predicted_income": 18500,
        "timeline": [
            {"time": "12:00-12:30", "action": "渋谷ストリーム周辺で待機"},
            {"time": "12:30-13:00", "action": "道玄坂のファストフード店集中エリアを巡回"},
            {"time": "13:00-13:30", "action": "ピーク終了。神泉駅方面へ移動しつつ案件を待つ"},
        ],
    }
    return Response(data)

@api_view(["GET"])
def daily_summary(request):
    data = {
        "sales": 12800,
        "orders": 9,
        "avg_hourly": 1650,
        "work_time_min": 310,
    }
    return Response(data)

@api_view(["GET"])
def weekly_forecast(request):
    data = [
        {"day": "Mon", "weather": "Cloudy", "demand": "High"},
        {"day": "Tue", "weather": "Rain",   "demand": "Very High"},
        {"day": "Wed", "weather": "Clear",  "demand": "Medium"},
        {"day": "Thu", "weather": "Clear",  "demand": "Medium"},
        {"day": "Fri", "weather": "Cloudy", "demand": "High"},
        {"day": "Sat", "weather": "Rain",   "demand": "Very High"},
        {"day": "Sun", "weather": "Clear",  "demand": "Medium"},
    ]
    return Response(data)

@api_view(["POST"])
def upload_screenshot(request):
    # 受け取ったファイルはダミー処理。実際のOCRは後で差し替え
    _ = request.FILES.get("file")
    return Response({"ok": True, "extracted": {"amount": "不明", "time": "不明"}})
