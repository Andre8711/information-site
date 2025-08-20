from django.urls import path
from . import views
from news import views
urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news_list, name='news'),
    path('articles/', views.articles, name='articles'),
    path('contacts/', views.contacts, name='contacts'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('article/<str:article_slug>/', views.article_detail, name='article'),
    path('register/', views.register, name='register'),
]