from django.contrib import admin
from django.urls import path
from registros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nuevo/', views.nuevo_registro, name='nuevo_registro'),
    path('lista/', views.lista_registros, name='lista_registros'),
    path('exportar/', views.exportar_csv, name='exportar_csv'),
]
