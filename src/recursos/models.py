from django.db import models

class Recursos(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    recurso = models.FileField(upload_to='recurso/', null=True, blank=True)
