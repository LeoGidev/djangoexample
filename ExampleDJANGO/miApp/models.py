from django.db import models

# Create your models here.
class Dato(models.Model):
    fecha = models.DateField()
    id = models.AutoField(primary_key=True)
    dato = models.CharField(max_length=255)