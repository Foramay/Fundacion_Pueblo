from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Eventos, MisEventos
from .forms import EventosForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


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
    paginate_by = 5

class Actualizar(LoginRequiredMixin, UpdateView):
    template_name = 'eventos/actualizar.html'
    model = Eventos
    form_class = EventosForm

    def get_success_url(self):
        return reverse('eventos:listar')

class Eliminar(LoginRequiredMixin, DeleteView):
    model = Eventos
    template_name = 'eventos/eliminar.html'

    def get_success_url(self):
        return reverse('eventos:listar')
    

class ListarMisEventos(LoginRequiredMixin, ListView):
    template_name = 'eventos/eventos_usuario.html'
    #Acá estamos diciendo a la vista basada en clases que vamos a trabajar con el modelo de 'MisEventos'.
    model = MisEventos
    context_object_name = 'mis_eventos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Con este context_data estamos recuperando todos los eventos en donde el usuario este participando mediante un filtrado por id
        eventos = MisEventos.objects.filter(usuario_id=self.request.user.id)
        context['eventos'] = eventos
        #Y por último estamos capturando toda la información del modelo 'Eventos' así lo podemos renderizar en el html de 'eventos_usuarios.html'.
        context['mis_eventos'] = self.model.objects.filter(usuario_id=self.request.user.id)
        return context
    
@login_required
def participar(request):
    #Con esta funcion estamos dando funcionalidad al boton de participar.
    if request.method == 'POST':
        #Aca obtenemos el id del usuario logueado y lo guardamos en una variable.
        usuario = request.user.id
        #Obtenemos el id del evento que quiere participar el usuario logueado y lo guardamos en una variable.
        evento_id = request.POST['evento_id']
        #Buscamos el id del evento para saber si esta participando o no.
        existe_evento = MisEventos.objects.filter(evento_id=evento_id, usuario_id=usuario).exists()
        if existe_evento:
            print("Ya estás participando.")
        else:
            #Creamos una instancia del modelo 'MisEventos' para poder guardar las variables en los campos correspondientes.
            mis_eventos = MisEventos(evento_id=evento_id, usuario_id=usuario)
            #Y al final de todo, guardamos.
            mis_eventos.save()
        return redirect('eventos:mis_eventos')
    else:
        #Este else funciona para que si el usuario no esta logueado, lo redireccione al loguin y después lo lleve a la url de listar
        return redirect('eventos:listar')
    
@login_required
def dejar_de_participar(request):
    if request.method == 'POST':
        #Recupero el id del usuario
        usuario = request.user.id
        #Recupero el id del evento que desea dejar de participar
        evento_id = request.POST['evento_id']
        #Hago un filtrado por el evento mediante el filter
        mis_eventos = MisEventos.objects.filter(id=evento_id, usuario_id=usuario)
        #Y borro el registro
        mis_eventos.delete()
        return redirect('eventos:listar')
    else:
        return redirect('eventos:listar')