from django.db import models

class Home(models.Model):
    presentacion = models.TextField()
    quienes_somos = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    