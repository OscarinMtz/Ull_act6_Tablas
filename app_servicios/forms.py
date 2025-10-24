# app_servicios/forms.py

from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        # Campos que se mostrarán en el formulario para AGREGAR
        fields = ['nombre_ser', 'desc', 'precio', 'duracion', 'tipo_de_serv']
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 2}), # Para que la descripción sea un campo de texto más pequeño
        }