from django.views.generic import ListView
from .models import Recursos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RecursosForm
from django.urls import reverse


class ListarRecursos(ListView):
    template_name = 'recursos/listar_recursos.html'
    model = Recursos
    context_object_name = 'recursos'
    paginate_by = 5

class CrearRecurso(LoginRequiredMixin, CreateView):
    model = Recursos
    form_class = RecursosForm
    template_name = 'recursos/crear_recurso.html'

    def get_success_url(self):
        return reverse('recursos:recursos')
    
class EditarRecurso(LoginRequiredMixin, UpdateView):
    template_name = 'recursos/editar_recurso.html'
    model = Recursos
    form_class = RecursosForm

    def get_success_url(self):
        return reverse('recursos:recursos')
    

class EliminarRecurso(LoginRequiredMixin, DeleteView):
    model = Recursos
    template_name = 'recursos/eliminar_recurso.html'

    def get_success_url(self):
        return reverse('recursos:recursos')