""" API url patterns. """

from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('api/token', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/create-account', views.UserCreate.as_view()),
    path('api/create-single-player-game',
         views.CreateSinglePlayerGame.as_view()),
    path('api/get-single-player-games', views.GetSinglePlayerGames.as_view()),
    path('api/delete-game', views.GameDelete.as_view()),
]
