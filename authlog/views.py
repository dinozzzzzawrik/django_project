from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def auth(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Произошла ошибка')
    else:
        form = UserRegisterForm()
    return render(request, 'authlog/index.html', {'title': 'Авторизация', 'form': form})

def user_login(request):
    pass