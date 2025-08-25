from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Article

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})

ALLOWED_USERS = ['123']  # или ['user1', 'user2']

def user_allowed(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.username not in ALLOWED_USERS:
            return HttpResponseForbidden("Доступ запрещён")
        return view_func(request, *args, **kwargs)
    return wrapper

@user_allowed
def index(request):
    return render(request, 'news/main.html')

@user_allowed
def news_list(request):
    news = Article.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'news/news_list.html', {'news': news})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Регистрация прошла успешно! Войдите в систему.')
            return redirect('index')
    return render(request, 'news/register.html')

def articles(request):
    return render(request, 'news/articles.html')

def contacts(request):
    return render(request, 'news/contacts.html')

def category(request, category_name):
    return render(request, 'news/category.html', {'category_name': category_name})

def article_detail(request, article_slug):
    return render(request, 'news/article_detail.html', {'article_slug': article_slug})

