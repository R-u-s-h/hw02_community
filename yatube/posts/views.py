from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Group, Post


LIMIT_POST = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:LIMIT_POST]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/index.html'
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:LIMIT_POST]
    post_list = group.posts.order_by('group')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    context = {
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    context = {
    }
    return render(request, 'posts/post_detail.html', context)