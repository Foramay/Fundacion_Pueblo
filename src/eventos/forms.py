from django import forms
from .models import Eventos
from django.forms import ClearableFileInput
from django.utils.translation import gettext_lazy as _

class EventosForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre', 'style': 'height: 50px;'}))
    descripcion=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción', 'style': 'height: 100px;'}))
    imagen = forms.ImageField(widget=ClearableFileInput(attrs={'class': 'form-control-file'}), label=_('Imagen: '))
    class Meta:
        model = Eventos
        fields = ['nombre', 'descripcion_corta', 'descripcion_completa', 'imagen']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) == 0:
            raise forms.ValidationError('Agrega un nombre')
        return nombre 
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) == 0:
            raise forms.ValidationError('Agrega una descripcion')
        return descripcion