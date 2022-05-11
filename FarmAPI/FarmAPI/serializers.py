from rest_framework import serializers
from .models import Medicamento, Ficha

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'