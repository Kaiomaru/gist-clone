from django.contrib import admin
from django.urls import path, include
from .views import GistsAPIView, GistsRUDView
from rest_framework.authtoken import views

urlpatterns = [
    path('gists/', GistsAPIView.as_view()),
    path('gists/<int:pk>', GistsRUDView.as_view()),
    path('auth/', views.obtain_auth_token),
]