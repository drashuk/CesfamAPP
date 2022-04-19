from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MedicamentoSerializer
from .models import Medicamento
from rest_framework import status
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect




@csrf_exempt
@api_view(['GET'])


def listarMedicamentos(request):
    if request.method == 'GET':
        medicamentos = Medicamento.objects.all()
        serializer = MedicamentoSerializer(medicamentos, many=True)
        return Response(serializer.data)

@api_view(['POST'])

def agregarMedicamentos(request):
    if request.method == 'POST':
        serializer = MedicamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])

def gestionarMedicamentos(request, idMed):
    try:
        medicamento = Medicamento.objects.get(idMed=idMed)
    except Medicamento.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(MedicamentoSerializer(medicamento).data)

    elif request.method == 'PUT':
        serializer = MedicamentoSerializer(medicamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        medicamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return render(request, 'index.html')


