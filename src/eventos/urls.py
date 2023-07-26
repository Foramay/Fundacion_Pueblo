from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('crear/', views.Crear.as_view(), name='crear'),
    path('listar/', views.ListarEvents.as_view(), name='listar'),
    path('actualizar/<int:pk>', views.Actualizar.as_view(), name='actualizar'),
    path('eliminar/<int:pk>', views.Eliminar.as_view(), name='eliminar'),
    path('mis_eventos/', views.ListarMisEventos.as_view(), name='mis_eventos'),
    path('participar/', views.participar, name='participar'),
    path('dejar_de_participar/', views.dejar_de_participar, name='dejar_de_participar'),
    path('ver/<int:pk>', views.ver, name='ver_mas'),
    path('comentario/<int:pk>', views.comentario, name='comentario')
]
