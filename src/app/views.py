from django.shortcuts import render
from eventos.models import Eventos
def home(request):
    template_name = 'home.html'
    #
    eventos = Eventos.objects.all()

    ctx = {
        'eventos': eventos,
    }
    # 
    # 
    return render(request, template_name, ctx)


