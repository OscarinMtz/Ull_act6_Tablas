# app_servicios/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Asigna la URL raíz a la función 'catalogo_servicios'
    path('', views.catalogo_servicios, name='catalogo_servicios'), 
]