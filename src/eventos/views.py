from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Eventos
from .forms import EventosForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class Crear(LoginRequiredMixin, CreateView):
    models = Eventos
    form_class = EventosForm
    template_name = 'eventos/crear.html'

    def get_success_url(self):
        return reverse('eventos:listar')
    

class ListarEvents(ListView):
    template_name = 'eventos/listar_eventos.html'
    model = Eventos
    context_object_name = 'eventos'

class Actualizar(LoginRequiredMixin, UpdateView):
    template_name = 'eventos/actualizar.html'
    model = Eventos
    form_class = EventosForm

    def get_success_url(self):
        return reverse('eventos:listar')

