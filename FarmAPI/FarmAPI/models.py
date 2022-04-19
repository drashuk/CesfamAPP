from django.db import models

class Medicamento(models.Model):
    idMed = models.IntegerField(primary_key =True, unique=True)
    nombreMed = models.CharField(max_length=100)
    miligramos = models.IntegerField()
    stock = models.IntegerField()
    precio = models.CharField(max_length=20)
    disponible = models.BooleanField()
    imagen = models.ImageField(upload_to='static/img/', blank=True, null=True)

    def __str__(self):
        return self.nombreMed

