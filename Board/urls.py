from django.contrib import admin
from django.urls import path
from Board import views as board_views

urlpatterns = [
    path('', board_views.mainPage, name='mainPage'),
]
