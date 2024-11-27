from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto', 'descripcion', 'cumpleaños', 'telefono', 'direccion']
        widgets = {