from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news_list, name='news'),
    path('articles/', views.articles, name='articles'),
    path('contacts/', views.contacts, name='contacts'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # изменено
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
