from django.contrib import admin
from .models import Author, Blog, Comment


class BlogInline(admin.TabularInline):
    model = Blog
    extra = 0


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BlogInline]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'pub_date')
