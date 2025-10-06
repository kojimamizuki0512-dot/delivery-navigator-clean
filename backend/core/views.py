from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def heatmap_data(request):
    data = [
        {"lat": 35.6585, "lng": 139.7013, "intensity": 0.9, "restaurants": ["A飯店", "Bカフェ", "Cバーガー"]},
        {"lat": 35.6610, "lng": 139.7038, "intensity": 0.7, "restaurants": ["Dラーメン", "Eピザ"]},
        {"lat": 35.6555, "lng": 139.6990, "intensity": 0.5, "restaurants": ["Fストア"]},
    ]
    return JsonResponse(data, safe=False)

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
    return JsonResponse(data)

def daily_summary(request):
    data = {
        "total_sales": 12500,
        "job_count": 9,
        "avg_hourly": 1780,
        "worked_minutes": 95,
        "work_hours": 1.6,
    }
    return JsonResponse(data)

def weekly_forecast(request):
    data = [
        {"day": "月", "weather": "晴れ", "demand": 0.8},
        {"day": "火", "weather": "くもり", "demand": 0.6},
        {"day": "水", "weather": "雨", "demand": 0.9},
        {"day": "木", "weather": "晴れ", "demand": 0.7},
        {"day": "金", "weather": "晴れ", "demand": 0.75},
        {"day": "土", "weather": "くもり", "demand": 0.65},
        {"day": "日", "weather": "雨", "demand": 0.85},
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
def upload_screenshot(request):
    if request.method != "POST":
        return JsonResponse({"detail": "POSTしてください"}, status=405)
    f = request.FILES.get("file")
    if not f:
        return JsonResponse({"detail": "file を送ってください"}, status=400)
    return JsonResponse({
        "status": "ok",
        "parsed": {
            "amount": 1340,
            "time": "12:14",
            "restaurant": "ダミー寿司",
            "area": "渋谷駅西口",
            "distance_km": 1.2,
            "boost": 1.1,
        }
    })
