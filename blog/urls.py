from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home.as_view(), name='blog_home'),
    path('posts', views.collected_post.as_view(), name='collected_post'),
    path('posts/readlater', views.read_later.as_view(), name='read_later'),
    path('posts/<slug:slug>', views.individual_post.as_view(), name='individual_post'),
]
