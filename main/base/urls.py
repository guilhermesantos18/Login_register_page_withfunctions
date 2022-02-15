from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('welcome/', views.welcomePage, name='welcome'),
]
