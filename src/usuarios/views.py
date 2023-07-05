from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import UserRegisterForm
from django.urls import reverse
from django.contrib.auth import login

class Registro(CreateView):
    form_class = UserRegisterForm
    template_name = 'usuarios/registro.html'
    model = Usuario


    def get_success_url(self):
        return reverse('eventos:listar')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
