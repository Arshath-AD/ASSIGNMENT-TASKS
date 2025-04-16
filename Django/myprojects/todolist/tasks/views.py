from django.shortcuts import render
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

# tasks/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Tasks!")
