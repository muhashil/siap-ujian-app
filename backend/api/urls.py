from django.urls import path

from backend.api.views_helper import (banner)

app_name = 'api'

urlpatterns = [
    path('banners', banner.ListBannerView.as_view())
]