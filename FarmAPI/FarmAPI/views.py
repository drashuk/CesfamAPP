from email import message
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import status
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect




@csrf_exempt 
@api_view(['GET']) 


def listarMedicamentos(request):
    if request.method == 'GET':
        medicamentos = Medicamento.objects.all()
        serializer = MedicamentoSerializer(medicamentos, many=True)
        if len(serializer.data) == 0:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='No hay medicamentos para listar')
        else:
            return Response(serializer.data)

@api_view(['POST'])

def agregarMedicamentos(request):
    if request.method == 'POST':
        serializer = MedicamentoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])

def gestionarMedicamentos(request, idMed):
    try:
        medicamento = Medicamento.objects.get(idMed=idMed)
    except Medicamento.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content="No existe el medicamento")

    if request.method == 'GET':
        return Response(MedicamentoSerializer(medicamento).data)

    elif request.method == 'PUT':
        medicamento = Medicamento.objects.get(idMed=idMed)
        serializer = MedicamentoSerializer(medicamento, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except:       
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        medicamento.delete()
        return Response(status=status.HTTP_200_OK)

def index(request):
    return render(request, 'index.html')

@api_view(['GET']) 


def listarFichas(request):
    if request.method == 'GET':
        
        fichas = Ficha.objects.all()
        serializer = FichaSerializer(fichas, many=True)
        if len(serializer.data) == 0:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='No hay fichas para listar')
        else:
            return Response(serializer.data)

@api_view(['POST'])

def agregarFicha(request):
    if request.method == 'POST':
        serializer = FichaSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                

@api_view(['GET', 'PUT', 'DELETE'])

def gestionarFicha(request, idFicha):
    try:
        ficha = Ficha.objects.get(idFicha=idFicha)
    except Ficha.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='Ficha no encontrada')

    if request.method == 'GET':
        return Response(FichaSerializer(ficha).data)

    elif request.method == 'PUT':
        ficha = Ficha.objects.get(idFicha=idFicha)
        serializer = FichaSerializer(ficha, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except:       
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ficha.delete()
        return Response(status=status.HTTP_200_OK)
