from django.contrib import admin
from django.urls import path
from Board import views as board_views

urlpatterns = [
    path('', board_views.mainPage, name='mainPage'),
    #path('add_post', board_views.addPost, name='addPost'),
    #path('edit_post', board_views.editPost, name='editPost'),
]
