from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.MyLoginView.as_view(), name='login'),
]
