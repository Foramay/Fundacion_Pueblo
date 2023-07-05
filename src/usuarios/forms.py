from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'style': 'height: 50px;'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'style': 'height: 50px;'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'height: 50px;'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario', 'style': 'height: 50px;'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'style': 'height: 50px;'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeti la contraseña', 'style': 'height: 50px;'}))
    telefono = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeti la contraseña', 'style': 'height: 50px;'}))
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) == 0:
            raise forms.ValidationError('Agrega un nombre')
        return nombre
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) == 0:
            raise forms.ValidationError('Agrega un apellido')
        return last_name
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) == 0:
            raise forms.ValidationError('Agrega un email')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) == 0:
            raise forms.ValidationError('Agrega un nombre')
        return username
    
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if len(password1) == 0:
            raise forms.ValidationError('Ingresá una contraseña')
        return password1
    
    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if len(password2) == 0:
            raise forms.ValidationError('Escribí una contraseña') 
        return password2
