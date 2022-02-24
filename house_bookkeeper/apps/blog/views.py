from django.shortcuts import render
from apps.base_param import base_param
from .models import Writing

def blog(request):
    base_param['posts'] = Writing.objects.all()
    return render(request, 'blog/blog.html', base_param)