from django.shortcuts import render
from apps.config import base_param


def news(request):
    return render(request, 'news/news.html', base_param)

