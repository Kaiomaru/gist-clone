from django.contrib import admin
from django.urls import path, include
from .views import GistsAPIView, GistsRUDView

urlpatterns = [
    path('gists/', GistsAPIView.as_view()),
    path('gists/<int:pk>', GistsRUDView.as_view())
]