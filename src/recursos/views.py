from django.views.generic import ListView
from .models import Recursos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import RecursosForm
from django.urls import reverse


class ListarRecursos(ListView):
    template_name = 'recursos/listar_recursos.html'
    model = Recursos
    context_object_name = 'recursos'

class CrearRecurso(LoginRequiredMixin, CreateView):
    model = Recursos
    form_class = RecursosForm
    template_name = 'recursos/crear_recurso.html'

    def get_success_url(self):
        return reverse('recursos:recursos')