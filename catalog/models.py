from django.db import models
from django.urls import reverse
from django.core.files import File


class Post(models.Model):
    title = models.CharField(max_length=30)
    url_name = models.CharField(max_length=8, unique=True)
    image = models.ImageField(upload_to='images')
    text = models.TextField(default='Это удивительный и уникальный экспонат музея школы №335!')

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.url_name])

    def __str__(self):
        return self.title
