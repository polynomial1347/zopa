from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'moi/index.html', {'title': 'Главная страница сайта хуёв', 'tasks': tasks})


def about(request):
    return render(request, 'moi/admin.html')
# Create your views here.
