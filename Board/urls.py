from django.contrib import admin
from django.urls import path
from Board import views as board_views

urlpatterns = [
    path('', board_views.main_page, name='main_page'),
    path('upd', board_views.update_posts, name='update_posts'),
    path('add_post', board_views.add_post, name='add_post'),
    path('edit_post/<int:post_pk>', board_views.edit_post, name='edit_post'),
    path('show_all_posts', board_views.show_all_posts, name='show_all_posts'),
]
