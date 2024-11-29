from django.db import models
from django.contrib.auth.models import User

class Dato(models.Model):
    Fecha = models.DateField(auto_now_add=True)   
    ID = models.AutoField(primary_key=True)
    Dato = models.IntegerField()

    class Meta:
        db_table = 'data'  # Vincula este modelo a la tabla 'data'
    

    def __str__(self):
        return f"{self.Fecha} - {self.Dato}"
    

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    descripcion = models.TextField("Sobre mí", blank=True)
    cumpleaños = models.DateField("Cumpleaños", blank=True, null=True)
    telefono = models.CharField("Teléfono", max_length=15, blank=True, null=True)
    direccion = models.CharField("Dirección", max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"    

      