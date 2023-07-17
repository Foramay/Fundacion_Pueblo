from django.urls import path
from . import views

app_name = 'recursos'

urlpatterns = [
    path('recursos/', views.ListarRecursos.as_view(), name='recursos' ),
    path('crear_recurso/', views.CrearRecurso.as_view(), name='crear_recurso' ),
    path('editar/<int:pk>', views.EditarRecurso.as_view() , name='editar')
]
