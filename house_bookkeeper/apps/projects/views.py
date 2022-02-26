from django.shortcuts import render
from apps.config import base_param

def projects(request):
    return render(request, 'projects/projects.html', base_param)
