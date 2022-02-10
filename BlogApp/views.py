from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView


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
    ordering = ['fecha']
    
    def get_queryset(self, **kwargs):
        return Blog.objects.filter(user__username=self.kwargs['user'])
  
class BlogMyView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'BlogApp/mis_blogs.html'
    context_object_name = 'blogs'
    paginate_by = 10
    
    def get_queryset(self, **kwargs):
        return Blog.objects.filter(user__username=self.request.user)
  
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('inicio')
    fields = ['titulo', 'subtitulo', 'fecha', 'contenido','imagen']
    template_name = 'BlogApp/nuevo_blog.html'
    
    def get_initial(self):
        return {
            'user':self.request.user,
            'fecha': datetime.date.today()
        }
        
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super(BlogCreateView, self).form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy('inicio')
    fields = ['titulo', 'subtitulo', 'fecha', 'contenido','imagen']
    template_name = 'BlogApp/editar_blog.html'
    
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('inicio')
    template_name = 'BlogApp/eliminar_blog.html'
      