from django.test import TestCase
from django.urls import reverse
from .models import Post

class BlogRoutesTests(TestCase):
    def setUp(self):
        # Создаём тестовый пост для проверки динамических маршрутов
        self.post = Post.objects.create(title="Тестовый пост", content="Тестовое содержимое")

    def test_home_page(self):
        # Проверка главной страницы
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Добро пожаловать")

    def test_about_page(self):
        # Проверка страницы "О нас"
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "О проекте")

    def test_post_list(self):
        # Проверка списка постов
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail(self):
        # Проверка страницы отдельного поста
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.content)

    def test_post_create(self):
        # Проверка создания нового поста через форму
        response = self.client.post(reverse('post_create'), {
            'title': 'Новый пост',
            'content': 'Новое содержимое'
        })
        self.assertEqual(response.status_code, 302)  # Должно быть перенаправление
        self.assertTrue(Post.objects.filter(title='Новый пост').exists())
# Create your tests here.
