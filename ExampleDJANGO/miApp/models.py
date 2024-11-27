from django.db import models

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
       