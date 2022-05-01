from os.path import exists
import re

from django.shortcuts import render

from apps.config import base_param
from .models import Publications
from ..news.views import news_publication

var_param = 213

# Обновление публикаций
def updating_publications():
    if not exists('..\\publications.txt'): return

    with open('..\\publications.txt', 'r') as publ: new_publ = publ.read()
    with open('..\\publications.txt', 'w') as publ: publ.write('')

    if not re.search(r'\w+', new_publ): return

    new_publ = new_publ.replace('\n', ' ').rstrip().strip()
    old_publ = [publ.text for publ in Publications.objects.all()]
    
    if new_publ not in old_publ:
        entry = Publications(text=new_publ)
        entry.save() 
        return 'Запись в блоге', entry.id

def blog(request):
    entry_info = updating_publications()
    if entry_info != None: news_publication(entry_info)

    base_param['posts'] = Publications.objects.all()
    return render(request, 'blog/blog.html', base_param)
