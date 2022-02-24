from django.shortcuts import render
from apps.base_param import base_param

def projects(request):
    return render(request, 'projects/projects.html', base_param)
