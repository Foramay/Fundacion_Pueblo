from django.db import models

class Eventos(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=True)
    descripcion = models.TextField(max_length=255, null=False, blank=True)
    fecha_evento = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nombre, self.descripcion, self.fecha_evento