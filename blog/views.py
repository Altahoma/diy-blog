from django.shortcuts import render
from .models import Author, Blog, Comment


def index(request):
    num_authors = Author.objects.all().count()
    num_blogs = Blog.objects.all().count()
    num_comments = Comment.objects.all().count()
    context = {
        'num_authors': num_authors,
        'num_blogs': num_blogs,
        'num_comments': num_comments,
    }

    return render(request, 'index.html', context=context)
