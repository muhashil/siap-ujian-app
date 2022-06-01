from django.urls import path

from backend.api.views_helper import (banner, materi)

app_name = 'api'

urlpatterns = [
    path('banners', banner.ListBannerView.as_view()),

    # Materi
    path('materi', materi.ListMateriView.as_view())
]