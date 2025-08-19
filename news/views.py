from django.shortcuts import render
from .models import News  # импортируем модель News

def index(request):
    return render(request, 'news/main.html')

def news_list(request):
    news = News.objects.all().order_by('-published_date')  # получаем новости из базы
    return render(request, 'news/news_list.html', {'news': news})

# остальные функции без изменений
def articles(request):
    return render(request, 'news/articles.html')

def contacts(request):
    return render(request, 'news/contacts.html')

def category(request, category_name):
    return render(request, 'news/category.html', {'category_name': category_name})

def article_detail(request, article_slug):
    return render(request, 'news/article_detail.html', {'article_slug': article_slug})
def news_list(request):
    news = News.objects.all().order_by('-created_at')  # сортируем по дате создания
    return render(request, 'news/news_list.html', {'news': news})