from django.db import models

# Create your models here.

class FormAdopcion(models.Model):
	
	id_user=models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
	id_mascota=models.ForeignKey('mascotas.Mascotas', on_delete=models.CASCADE)
	nombre=models.CharField(max_length=100)
	telefono=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	ciudad=models.CharField(max_length=100)
	ocupacion=models.CharField(max_length=100)
	edad=models.IntegerField()
