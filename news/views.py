from django.shortcuts import render, get_object_or_404
from .models import News, Category

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'news/news_list.html', {'news': news, 'categories': categories})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

def category_news(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    news = News.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'news/news_list.html', {'news': news, 'categories': categories, 'selected_category': category})