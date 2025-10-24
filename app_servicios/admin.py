# app_servicios/admin.py

from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    # Esto define las columnas que se muestran en la lista del panel admin
    list_display = ('id', 'nombre_ser', 'precio', 'duracion', 'tipo_de_serv')