from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('crear/', views.Crear.as_view(), name='crear'),
    path('listar/', views.ListarEvents.as_view(), name='listar')
]