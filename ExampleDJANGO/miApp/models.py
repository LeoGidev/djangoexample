from django.db import models

class Dato(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)   # Cambié a DateTimeField para que coincida con el uso de timezone.now() en la vista
    id = models.AutoField(primary_key=True)
    dato = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.fecha} - {self.dato}"
