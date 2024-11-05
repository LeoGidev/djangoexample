from django.db import models

# Create your models here.
class Dato(models.Model):
    Fecha = models.DateField()
    ID = models.AutoField(primary_key=True)
    Dato = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.Fecha} - {self.Dato}"