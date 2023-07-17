from django.db import models
from usuarios.models import Usuario


class Eventos(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=True)
    descripcion = models.TextField(max_length=255, null=False, blank=True)
    fecha_evento = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes_evento', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class MisEventos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)

    def obtener_info(self):
        return self.evento