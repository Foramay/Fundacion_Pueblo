from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Eventos
from .forms import EventosForm
from django.urls import reverse

class Crear(CreateView):
    models = Eventos
    form_class = EventosForm
    template_name = 'eventos/crear.html'

    def get_success_url(self):
        return reverse('home')