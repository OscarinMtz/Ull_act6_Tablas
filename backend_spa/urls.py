# backend_spa/urls.py (Incluir las URLs de la app_servicios)

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_servicios.urls')), # << MANDA LA RUTA RAIZ A LA APP
]