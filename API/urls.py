from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),


    path('posts/', views.list_posts, name='list_posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/', views.read_post, name='read_post'),
    path('posts/<int:post_id>/update/', views.update_post, name='update_post'),
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
