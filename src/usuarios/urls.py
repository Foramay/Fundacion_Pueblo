from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.Registro.as_view(), name='registro'),
    path('perfil/', views.Perfil.as_view(), name='perfil'),
    path('editar_perfil/<int:pk>', views.EditarPerfil.as_view(), name='editar_perfil')
]
