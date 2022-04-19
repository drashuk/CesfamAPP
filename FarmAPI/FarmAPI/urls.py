from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listarMedicamentos', listarMedicamentos, name='listarMedicamentos'),
    path('api/agregarMedicamentos', agregarMedicamentos, name='agregarMedicamentos'),
    path('api/gestionarMedicamentos/<idMed>', gestionarMedicamentos, name='gestionarMedicamentos'),
    path('', index, name='index')
]

