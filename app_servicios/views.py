# app_servicios/views.py

from django.shortcuts import render, redirect
from .models import Servicio
from .forms import ServicioForm # Importa el formulario

def catalogo_servicios(request):
    # LÓGICA POST: Procesar y guardar nuevo registro
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo_servicios') # Redirige a la misma página
    else:
        # LÓGICA GET: Mostrar el formulario vacío
        form = ServicioForm()

    # Obtener todos los servicios para la tabla (la información)
    servicios = Servicio.objects.all()
    
    context = {
        'servicios': servicios, # << Variable para el bucle for
        'form': form,           # << Variable para el formulario
    }
    return render(request, 'index.html', context)