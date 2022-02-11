import imp
from django.urls import path

from BlogApp.views import inicio, about_me, BlogListView, BlogDetailView, BlogUserView, BlogMyView, BlogCreateView, BlogUpdateView, BlogDeleteView, profile

urlpatterns = [
   
    path('', BlogListView.as_view(), name="inicio"), 
    path('Blog/usuario/<user>', BlogUserView.as_view(), name='blog_ver_usuario'),
    path('MisBlogs', BlogMyView.as_view(), name="mis_blogs"),
    path('Blog/nuevo', BlogCreateView.as_view(), name='blog_add'),
    path('Blog/ver/<pk>', BlogDetailView.as_view(), name='blog_ver'),
    path('Blog/editar/<pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('Blog/eliminar/<pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('Profile', profile, name="profile"),
    path('aboutme', about_me, name="about_me"),
]