from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('crud/', views.crud),
    path('insert/', views.insert),
]
