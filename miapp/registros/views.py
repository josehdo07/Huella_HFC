from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Registro
import pandas as pd
from django.http import HttpResponse

def nuevo_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm()
    return render(request, 'nuevo_registro.html', {'form': form})

def lista_registros(request):
    registros = Registro.objects.filter(usuario=request.user)
    return render(request, 'lista_registros.html', {'registros': registros})

def exportar_csv(request):
    registros = Registro.objects.filter(usuario=request.user).values()
    df = pd.DataFrame(registros)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=registros.csv'
    df.to_csv(path_or_buf=response, index=False)
    return response
