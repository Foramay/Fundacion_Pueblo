import django_filters
from .models import Eventos
from django import forms

class FiltrarEvento(django_filters.FilterSet):
    nombre = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del evento'})
    )

    MODALIDADES_CHOICES = (
        ('V', 'Virtual'),
        ('P', 'Presencial')
    )
    modalidad = django_filters.ChoiceFilter(
        choices=MODALIDADES_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Seleccione una modalidad'
    )

    class Meta:
        model = Eventos
        fields = ['nombre', 'modalidad']