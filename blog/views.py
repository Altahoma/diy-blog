from django.shortcuts import render
from django.views import generic
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


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    model = Blog


class BloggerListView(generic.ListView):
    template_name = 'blog/blogger_list.html'
    model = Author
    paginate_by = 5


class BloggerDetailView(generic.DetailView):
    template_name = 'blog/blogger_detail.html'
    model = Author
