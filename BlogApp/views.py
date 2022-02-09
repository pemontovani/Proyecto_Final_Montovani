from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from django.views.generic import ListView, DetailView


# Create your views here.

def inicio(request):
      return render(request, "BlogApp/inicio.html")    

def about_me(request):
      return render(request, "BlogApp/about_me.html")    

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'BlogApp/blogs.html'
    context_object_name = 'blogs'
    paginate_by = 10
    
class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'BlogApp/ver_blog.html'
    context_object_name = 'blog'
    
class BlogUserView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'BlogApp/blogs.html'
    context_object_name = 'blogs'
    paginate_by = 10
    
    def get_queryset(self, **kwargs):
        return Blog.objects.filter(user__username=self.kwargs['user'])
  
class BlogMyView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'BlogApp/mis_blogs.html'
    context_object_name = 'blogs'
    paginate_by = 10
    
    def get_queryset(self, **kwargs):
        return Blog.objects.filter(user__username=self.request.user)
