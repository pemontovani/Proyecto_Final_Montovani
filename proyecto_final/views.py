from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render

from django.views.generic import CreateView
from proyecto_final.forms import UserRegisterForm


class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy('login')
    template_name = 'registrar.html'
    form_class = UserRegisterForm
    
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
    

