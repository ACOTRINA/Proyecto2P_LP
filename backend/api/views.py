from django.shortcuts import render
from mascotas import models
from formAdopcion import models as modelA
from usuario import models as modelU
from .serializers import MascotasSerializer, FormSerializer, UsuarioSerializer
from rest_framework import generics, filters
# Create your views here.

class ListMascotas(generics.ListCreateAPIView):  #Crear y ver mascotas

	search_fields = ['especie','ciudad','id_user__id']
	filter_backends = (filters.SearchFilter,)
	queryset=models.Mascotas.objects.all()
	serializer_class=MascotasSerializer

class GestionMascotas(generics.RetrieveUpdateDestroyAPIView):

	queryset=models.Mascotas.objects.all()
	serializer_class=MascotasSerializer

class ListForms(generics.ListCreateAPIView): #crear y ver formularios

	search_fields = ['id_user__id']
	filter_backends = (filters.SearchFilter,)
	queryset = modelA.FormAdopcion.objects.all()
	serializer_class = FormSerializer

class GestionForms(generics.RetrieveUpdateDestroyAPIView): #Eliminar formularios

	queryset = modelA.FormAdopcion.objects.all()
	serializer_class = FormSerializer

class ListUsuarios(generics.ListCreateAPIView): #crear y ver formularios

	search_fields = ['email']
	filter_backends = (filters.SearchFilter,)
	queryset = modelU.Usuario.objects.all()
	serializer_class = UsuarioSerializer

# class GestionUsuarios(generics.RetrieveUpdateDestroyAPIView):

# 	queryset = modelU.Usuario.objects.all()
# 	serializer_class = UsuarioSerializer
