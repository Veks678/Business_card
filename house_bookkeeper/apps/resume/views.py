from django.shortcuts import render
from apps.config import base_param

def resume(request):
    return render(request, 'resume/resume.html', base_param)
