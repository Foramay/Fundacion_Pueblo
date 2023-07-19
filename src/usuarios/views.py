from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Usuario
from .forms import UserRegisterForm
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm

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

class Perfil(ListView):
    model = Usuario
    template_name = 'usuarios/perfil.html'
    context_object_name = 'perfil'
    #Esta funcion queryset filtra todos los registros dependiendo de que usuario este logueado
    def get_queryset(self):
        return Usuario.objects.filter(id=self.request.user.id)
    

class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'usuarios/editar_perfil_usuario.html'
    model = Usuario
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse('usuarios:perfil')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
    

class EliminarPerfil(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_perfil.html'

    def get_success_url(self):
        return reverse('eventos:listar')