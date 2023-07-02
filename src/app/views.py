from django.shortcuts import render
from eventos.models import Eventos
def home(request):
    template_name = 'home.html'
    ctx = {
    }
    return render(request, template_name, ctx)


