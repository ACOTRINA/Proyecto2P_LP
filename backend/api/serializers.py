from rest_framework import serializers
from mascotas import models
from formAdopcion import models as modelA
from usuario import models as modelU

class MascotasSerializer(serializers.ModelSerializer):

	class Meta:
		
		fields= '__all__'
		model=models.Mascotas

class FormSerializer(serializers.ModelSerializer):

	class Meta:

		fields = '__all__'
		model=modelA.FormAdopcion

class UsuarioSerializer(serializers.ModelSerializer):

	class Meta:

		fields= '__all__'
		model=modelU.Usuario
