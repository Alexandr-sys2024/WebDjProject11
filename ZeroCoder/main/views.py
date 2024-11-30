from django.shortcuts import render
from django.http import HttpResponse

# Главная страница
def index(request):
    data = {
        'caption': "CatDjango"
    }
    return render(request, 'main/index.html', data)

# Второстепенная страница
def new(request):
    return render(request, 'main/new.html')

# О нас
def about(request):
    return render(request, 'main/about.html')

# Контакты
def contact(request):
    return render(request, 'main/contact.html')
from django.shortcuts import render

# Create your views here.
