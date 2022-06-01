from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from backend.api.views_helper import (banner, materi)

app_name = 'api'

urlpatterns = [

    # Auth
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # Banner
    path('banners', banner.ListBannerView.as_view()),

    # Materi
    path('materi', materi.ListMateriView.as_view())
]