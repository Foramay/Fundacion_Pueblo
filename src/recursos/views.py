from django.shortcuts import render
from django.views.generic import ListView
from .models import Recursos


class ListarRecursos(ListView):
    template_name = 'recursos/listar_recursos.html'
    model = Recursos
    context_object_name = 'recursos'