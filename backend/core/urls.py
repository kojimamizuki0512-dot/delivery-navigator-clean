from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    # あなたの API ルーティング（core/api_urls.py 側に各エンドポイントを定義）
    path("api/", include("core.api_urls")),

    # ヘルスチェック（任意）
    path("healthz", TemplateView.as_view(template_name="index.html")),

    # それ以外の全てのパス（/api/ を除く）は SPA の index.html を返す
    # 例: /records, /read などのクライアントサイドルーティング対応
    re_path(r"^(?!api/).*", TemplateView.as_view(template_name="index.html")),
]
