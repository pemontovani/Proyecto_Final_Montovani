"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, LoginView
from proyecto_final.views import UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(template_name='login.html', next_page='inicio'), name='login'),
    path('', include('BlogApp.urls'), name="Inicio"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registrar', UserCreateView.as_view(), name='registrar'),
]

#imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)