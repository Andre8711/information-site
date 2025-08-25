from django.contrib import admin
from .models import Article, Category, Author, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_at', 'is_published')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'category', 'author')
    date_hierarchy = 'published_at'
    ordering = ('-published_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'article', 'created_at', 'is_approved')
    search_fields = ('author_name', 'text')
    list_filter = ('is_approved', 'created_at', 'article')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)