from django.shortcuts import render
from .models import Books

# Create your views here.

def index(request):
    books = Books.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная', 'books': books})