from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from backend.api.views_helper import (banner, materi, quiz)

app_name = 'api'

urlpatterns = [

    # Auth
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # Banner
    path('banners', banner.ListBannerView.as_view()),

    # Materi
    path('materi', materi.MateriViewSet.as_view({'get': 'list'})),
    path('materi/<str:slug>', materi.MateriViewSet.as_view({'get': 'retrieve'})),

    path('quizes', quiz.QuizViewSet.as_view({'get': 'list'})),
    path('quizes/<int:quiz_id>/questions', quiz.QuizViewSet.as_view({'get': 'list_questions'})),

    path('questions/<str:slug>', quiz.QuestionViewSet.as_view({'get': 'retrieve'}))
]