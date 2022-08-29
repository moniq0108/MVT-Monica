from django.db import models

class Familiares(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_de_nacimiento = models.DateField()
    peso = models.IntegerField()


