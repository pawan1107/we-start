from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.signup, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login')
]