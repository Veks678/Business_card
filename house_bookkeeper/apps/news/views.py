from django.shortcuts import render

from .models import Publications

from apps.config import base_param

# Публикация новостей
def news_publication(entry_info): 
    name, entry_id = entry_info
    Publications(section=name).save()

def news(request):
    base_param['news'] = Publications.objects.all()
    return render(request, 'news/news.html', base_param)

