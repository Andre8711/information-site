from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden

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
    from .models import News
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})

# Страница регистрации
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # перенаправление на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'news/register.html', {'form': form})

# Остальные функции без изменений
def articles(request):
    return render(request, 'news/articles.html')

def contacts(request):
    return render(request, 'news/contacts.html')

def category(request, category_name):
    return render(request, 'news/category.html', {'category_name': category_name})

def article_detail(request, article_slug):
    return render(request, 'news/article_detail.html', {'article_slug': article_slug})