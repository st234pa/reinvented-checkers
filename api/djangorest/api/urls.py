""" API url patterns. """

from django.urls import path
from . import views

urlpatterns = [
    path('api/login', views.Login.as_view()),
    path('api/sample-view', views.SampleView.as_view()),
    path('api/create-account', views.UserCreate.as_view()),
    path('api/logout', views.Logout.as_view()),
    path('api/create-single-player-game',
         views.CreateSinglePlayerGame.as_view())
]
