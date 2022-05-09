from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listarMedicamentos', listarMedicamentos, name='listarMedicamentos'),
    path('api/agregarMedicamentos', agregarMedicamentos, name='agregarMedicamentos'),
    path('api/gestionarMedicamentos/<idMed>', gestionarMedicamentos, name='gestionarMedicamentos'),
    path('api/listarFichas', listarFichas, name='listarFichas'),
    path('api/agregarFicha', agregarFicha, name='agregarFicha'),
    path('api/gestionarFicha/<idFicha>', gestionarFicha, name='gestionarFicha'),
]


# api/gestionarMedicamentos/1 