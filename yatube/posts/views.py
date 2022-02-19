from django.shortcuts import get_object_or_404, render

from .models import Group, Post

LIMIT_POSTS = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:LIMIT_POSTS]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:LIMIT_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request,template,context)
    