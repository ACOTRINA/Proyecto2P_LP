from django.urls import path
from .views import *

urlpatterns = [
	path('mascotas',ListMascotas.as_view()), #Listado de mascotas y creacion
	path('mascotas/<int:pk>', GestionMascotas.as_view()),
	path('formularios', ListForms.as_view()), #Listado de formularios y creacion
	path('formularios/<int:pk>', GestionForms.as_view()), #Eliminar formulario
	path('usuarios', ListUsuarios.as_view()), #Crear y obtener usuarios
	#path('usuarios/<int:pk>', GestionUsuarios.as_view()) #Eliminar y modificar users

]
