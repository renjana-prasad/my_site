from django.shortcuts import render,get_object_or_404
from django.http import Http404

from .models import Posts

# Create your views here.
blog_introduction = "Hi, I am Renjana and I love to blog about Disney movies and series."

all_posts = Posts.objects.all().values()

def blog_home(request):
    try:
        # Get favourite posts, up to 3
        posts = [post for post in all_posts if post.get('favourite') == True][:3]

        if not posts:
            # Optional: show empty page message
            return render(request, 'blog/blog_home.html', {
                "blog_introduction": blog_introduction,
                "posts": [],
                "message": "No favourite posts available."
            })

        return render(request, 'blog/blog_home.html', {
            "blog_introduction": blog_introduction,
            "posts": posts
        })
    except Exception as e:
        # Log the error if needed
        raise Exception(f"Error loading blog home: {e}")



def collected_post(request):
    try:
        if all_posts:
            return render(request, 'blog/collected_post.html', {"posts": all_posts})
        else:
            # Safe fallback for empty posts
            return render(request, 'blog/collected_post.html', {
                "posts": [],
                "message": "No posts available yet."
            })
    except Exception as e:
        raise Exception(f"Error loading collected posts: {e}")


def individual_post(request, slug):
    try:
        # Safe lookup for a post by slug
        identified_post = get_object_or_404(Posts,slug=slug)

        return render(request, 'blog/single_post.html', {"single_post": identified_post})
    except Http404:
        raise Http404("Post not found")
    except Exception as e:
        raise Exception(f"Error loading individual post: {e}")