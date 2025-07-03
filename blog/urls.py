# filepath: blog/urls.py
from django.urls import path
from .views import home, about, PostListView, PostDetailView, PostCreateView
from .views import (
    home, about, PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView  # добавьте эти строки
)


urlpatterns = [
    path('', home, name='home'),  # главная страница
    path('about/', about, name='about'),  # страница "О нас"
    path('posts/', PostListView.as_view(), name='post_list'),  # список постов
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # отдельный пост
    path('posts/create/', PostCreateView.as_view(), name='post_create'),  # создание поста

    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),      # редактирование
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # удаление
]