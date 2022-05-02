from django.shortcuts import render

from .models import Publications

from apps.config import base_param

entry_info = {}

# Публикация новостей
def news_publication(entry): 
    name, url, entry_id = entry
    Publications(section=name, url=url, focus_id=entry_id).save()

def news(request):
    base_param['news'] = Publications.objects.all()
    return render(request, 'news/news.html', base_param)

