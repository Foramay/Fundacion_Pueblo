from django.urls import path
from . import views

app_name = 'recursos'

urlpatterns = [
    path('recursos/', views.ListarRecursos.as_view(), name='recursos' )
]
