from django.contrib import admin
from django.urls import path, include
from .views import GistsAPIView, GistsRUDView, StarredAPIView
from rest_framework.authtoken import views

urlpatterns = [
    path('gists/', GistsAPIView.as_view(), name='gists-api-view'),
    path('gists/<int:pk>', GistsRUDView.as_view(), name='gists-rud-view'),
    path('gists/starred', StarredAPIView.as_view(), name='starred-api-view'),
    path('auth/', views.obtain_auth_token, name='auth'),
]