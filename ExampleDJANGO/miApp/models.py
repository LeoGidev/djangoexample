from django.db import models

class Dato(models.Model):
    Fecha = models.DateTimeField(auto_now_add=True)   # Cambié a DateTimeField para que coincida con el uso de timezone.now() en la vista
    ID = models.AutoField(primary_key=True)
    Dato = models.CharField(max_length=255)

    class Meta:
        db_table = 'data'  # Vincula este modelo a la tabla 'data'
    

    def __str__(self):
        return f"{self.Fecha} - {self.Dato}"
