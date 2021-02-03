from django.db import models

# Create your models here.

class Usuario(models.Model):

	email=models.EmailField(max_length=100, unique=True)
	contrasenia=models.CharField(max_length=20)
	nombre_completo=models.CharField(max_length=200)
	cedula=models.CharField(max_length=10)
	telefono=models.CharField(max_length=10)
	ciudad=models.CharField(max_length=20)
