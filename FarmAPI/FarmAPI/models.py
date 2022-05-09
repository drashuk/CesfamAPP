from django.db import models

class Medicamento(models.Model):
    idMed = models.IntegerField(primary_key =True, unique=True, blank=True)
    nombreMed = models.CharField(max_length=100, blank=True)
    miligramos = models.IntegerField(blank=True)
    stock = models.IntegerField(blank=True)
    disponible = models.BooleanField(blank=True)

    def __str__(self):
        return self.nombreMed


class Paciente(models.Model):
    idPac = models.IntegerField(primary_key =True, unique=True, blank=True)
    idFicha = models.IntegerField(blank=True)
    idDr = models.IntegerField(blank=True)
    diagnostico = models.CharField(max_length=100, blank=True)
    prescripcion = models.CharField(max_length=100, blank=True)
