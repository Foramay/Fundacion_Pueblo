import django_filters
from .models import Eventos

class FiltrarEvento(django_filters.FilterSet):
    class Meta:
        model = Eventos
        fields = ['nombre', 'fecha_evento', 'modalidad']