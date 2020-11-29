# pages URL Configuration

from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
]