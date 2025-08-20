from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import News  # импорт модели News, если есть

def index(request):
    return render(request, 'news/main.html')

def news_list(request):
    news = News.objects.all().order_by('-created_at')  # сортируем по дате создания
    return render(request, 'news/news_list.html', {'news': news})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # перенаправление на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'news/register.html', {'form': form})

def articles(request):
    return render(request, 'news/articles.html')

def contacts(request):
    return render(request, 'news/contacts.html')

def category(request, category_name):
    return render(request, 'news/category.html', {'category_name': category_name})

def article_detail(request, article_slug):
    return render(request, 'news/article_detail.html', {'article_slug': article_slug})