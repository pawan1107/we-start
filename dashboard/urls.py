from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.signup, name='register'),
    path('login/', auth_view.login, {'template_name':'dashboard/login.html'}, name='login'),
    path('logout/', auth_view.logout, {'template_name': 'dashboard/logout.html'}, name='logout'),

]