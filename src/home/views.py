from django.shortcuts import render
from django.views.generic import ListView
from .models import Home


class ListarHome(ListView):
    template_name = 'home/listar_home.html'
    model = Home
    context_object_name = 'home'