from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Представление для главной страницы
def home(request):
    # Отображает приветствие и ссылки на другие страницы
    return render(request, 'blog/home.html')

# Представление для страницы "О нас"
def about(request):
    # Отображает информацию о проекте
    return render(request, 'blog/about.html')

# Класс для отображения списка всех постов
class PostListView(ListView):
    model = Post  # используем модель Post
    template_name = 'blog/post_list.html'  # шаблон для отображения

# Класс для отображения отдельного поста
class PostDetailView(DetailView):
    model = Post  # используем модель Post
    template_name = 'blog/post_detail.html'  # шаблон для отображения

# Класс для создания нового поста через форму
class PostCreateView(CreateView):
    model = Post  # используем модель Post
    form_class = PostForm  # используем форму PostForm
    template_name = 'blog/post_form.html'  # шаблон для формы
    success_url = '/posts/'  # перенаправление после успешного создания


# Класс для редактирования поста
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # используем тот же шаблон, что и для создания
    success_url = reverse_lazy('post_list')  # после редактирования возвращаемся к списку

# Класс для удаления поста
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # шаблон для подтверждения удаления
    success_url = reverse_lazy('post_list')  # после удаления возвращаемся к списк