from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('category/<int:category_id>/', views.category_news, name='category_news'),
]