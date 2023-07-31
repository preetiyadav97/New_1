from django.contrib import admin
from .views import first
from django.urls import path

urlpatterns = [
  
    path('im/',first)
]
