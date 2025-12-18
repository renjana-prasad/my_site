from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('posts', views.collected_post, name='collected_post'),
    path('posts/<slug:slug>', views.individual_post, name='individual_post'),
]
