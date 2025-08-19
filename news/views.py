from django.shortcuts import render

def index(request):
    # Главная страница
    return render(request, 'news/main.html')

def news_list(request):
    # Список новостей
    news = []  # Здесь можно получить новости из базы
    return render(request, 'news/news_list.html', {'news': news})

def articles(request):
    # Страница статей
    return render(request, 'news/articles.html')

def contacts(request):
    # Страница контактов
    return render(request, 'news/contacts.html')

def category(request, category_name):
    # Страница категории
    return render(request, 'news/category.html', {'category_name': category_name})

def article_detail(request, article_slug):
    # Страница статьи
    return render(request, 'news/article_detail.html', {'article_slug': article_slug})