from django import forms
from .models import Recursos
from django.forms import ClearableFileInput
from django.utils.translation import gettext_lazy as _



class RecursosForm(forms.ModelForm):
    titulo=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre', 'style': 'height: 50px;'}))
    descripcion=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción', 'style': 'height: 100px;'}))
    recurso = forms.ImageField(widget=ClearableFileInput(attrs={'class': 'form-control-file'}), label=_('Imagen: '))
    class Meta:
        model = Recursos
        fields = ['titulo', 'descripcion', 'recurso']



