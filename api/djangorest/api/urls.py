from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('sample-view', views.SampleView.as_view()),
    path('create-account', views.UserCreate.as_view()),
    path('logout', views.Logout.as_view()),
]
