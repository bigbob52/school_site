from django.shortcuts import render
from .models import Post
from PIL import Image


def home(request):
    items = Post.objects.all()
    return render(request, 'home.html', {'all_items': items})


def post_detail(request, url_name):
    item = Post.objects.get(url_name=url_name)
    return render(request, 'post.html', {'item': item})
