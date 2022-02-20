from django.shortcuts import get_object_or_404, render

from .models import Group, Post

LIMIT_POST = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:LIMIT_POST]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:LIMIT_POST]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
