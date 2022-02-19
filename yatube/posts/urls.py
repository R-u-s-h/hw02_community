# posts/urls.py
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('group_list.html', views.group_posts, name='group_posts'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]
