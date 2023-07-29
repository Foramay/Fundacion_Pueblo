from django.db import models
from usuarios.models import Usuario



class Eventos(models.Model):
    MODALIDAD_CHOICES = (
        ('V', 'Virtual'),
        ('P', 'Presencial')
    )
    nombre = models.CharField(max_length=30, null=False, blank=True)
    descripcion_corta = models.CharField(max_length=30)
    descripcion_completa = models.TextField(null=False, blank=True)
    fecha_evento = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes_evento', null=True, blank=True)
    modalidad = models.CharField(max_length=1, choices=MODALIDAD_CHOICES, default='P')
    
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def obtener_info(self):
        return self.evento
    
class MisEventos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)

    def obtener_info(self):
        return self.evento