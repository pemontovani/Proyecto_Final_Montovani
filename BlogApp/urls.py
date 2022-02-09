import imp
from django.urls import path

from BlogApp.views import inicio, about_me, BlogListView, BlogDetailView, BlogUserView, BlogMyView

urlpatterns = [
   
    path('', BlogListView.as_view(), name="inicio"), 
    path('Blog/ver/<pk>', BlogDetailView.as_view(), name='blog_ver'),
    path('Blog/usuario/<user>', BlogUserView.as_view(), name='blog_ver_usuario'),
    path('MisBlogs', BlogMyView.as_view(), name="mis_blogs"),
    # path('blogs/crearBlog', blog_add, name='blog_add'),
    # path('blogs/{id}', blog_add, name='blog_add'),
    # path('profile', profile, name="profile"),
    path('aboutme', about_me, name="about_me"),
]