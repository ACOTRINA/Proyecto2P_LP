from django.db import models

# Create your models here.

class Mascotas(models.Model):

	id_user = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE)
	nombre=models.CharField(max_length=100)
	raza=models.CharField(max_length=100)
	especie=models.CharField(max_length=100)
	sexo=models.CharField(max_length=100)
	edad=models.CharField(max_length=100)
	ciudad=models.CharField(max_length=100)
