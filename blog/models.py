from django.db import models

# Create your models here.
# filepath: blog/models.py
from django.db import models

class Post(models.Model):
    # Заголовок поста, максимум 100 символов
    title = models.CharField(max_length=100)
    # Содержимое поста
    content = models.TextField()

    def __str__(self):
        # Отображение поста по заголовку
        return self.title