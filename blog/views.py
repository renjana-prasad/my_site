from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from django.views.generic import ListView,CreateView,TemplateView
from .models import Posts,Comments
from .forms import CommentForms

# Create your views here.
blog_introduction = "Hi, I am Renjana and I love to blog about Disney movies and series."

all_posts = Posts.objects.all()

class blog_home(ListView):
    template_name = 'blog/blog_home.html'
    model = Posts
    context_object_name = 'posts'

    def get_queryset(self):
        query_set = super().get_queryset()
        extracted_data = query_set.filter(favourite=True)[:3]
        return extracted_data


class collected_post(ListView):
    template_name = 'blog/collected_post.html'
    model = Posts
    context_object_name = 'posts'

class individual_post(CreateView):
    model = Comments
    form_class = CommentForms
    template_name = 'blog/single_post.html'

    def form_valid(self, form):
        # Attach the post foreign key
        post = get_object_or_404(Posts, slug=self.kwargs['slug'])
        form.instance.post = post
        form.save()
        return redirect('individual_post', slug=post.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Posts, slug=self.kwargs['slug'])
        context['single_post'] = post
        context['list_of_comments'] = Comments.objects.filter(post=post).order_by('-id')
        existing_title = self.request.session.get('list_read_later_titles', [])
        context['read_later'] = post.title not in existing_title
        
        # Ensure the form shows on GET
        if 'form' not in context:
            context['form_data'] = self.get_form()
        else:
            context['form_data'] = context['form']
        return context

class read_later(TemplateView):
    template_name = 'blog/read_later.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['read_later'] = self.request.session.get('list_read_later_titles')
        return context

    def post(self, request, *args, **kwargs):
        remove = request.POST.get('remove')
        existing_title = request.session.get('list_read_later_titles', [])
        title = request.POST.get('title')

        if remove and remove in  existing_title :
            existing_title.remove(remove)
        elif title and title not in existing_title:
                existing_title.append(title)
                
        request.session['list_read_later_titles'] = existing_title
        return redirect('read_later')