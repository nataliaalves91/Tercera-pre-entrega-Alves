from django.db import models
from django.contrib.auth.models import User

#se crean las diferentes clases de modelos que se utilizarán posteriormente

class Teatro (models.Model):

    nombre = models.CharField (max_length=35)
    genero = models.CharField (max_length=20)
    edad = models.IntegerField ()
    autor= models.CharField (max_length=35)
    fecha = models.DateField(null=True)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

    def __str__ (self):
        return f'{self.nombre}, fecha {self.fecha}'


class Danza (models.Model):

    nombre = models.CharField (max_length=35)
    edad = models.IntegerField () 
    fecha = models.DateField(null=True)
    clasico = models.BooleanField(null=True)
    independiente = models.BooleanField(null=True)


    def __str__ (self):
        return f'Función: {self.nombre} - {self.fecha}'

class Cine (models.Model):

    nombre = models.CharField (max_length=35)
    genero = models.CharField (max_length=20)
    edad_minima = models.IntegerField ()
    fecha = models.DateField(null=True)
    estreno = models.BooleanField(null=True)
    

    def __str__ (self):

        return f'{self.nombre} - apta a partir de {self.edad_minima} años'
    
class Gastronomia (models.Model):

    nombre = models.CharField (max_length=35)
    localidad = models.CharField (max_length=50)
    testeado = models.BooleanField(null=True)
    telefono = models.IntegerField(null=True)
    apto_veganos = models.BooleanField(null=True)
    


    def __str__ (self):
        return f'Restaurante: {self.nombre} - Localidad: {self.localidad}'
    

class Musica (models.Model):

    nombre_grupo = models.CharField (max_length=35)
    genero= models.CharField (max_length=50)
    edad_minima = models.IntegerField ()
    pais_origen = models.CharField(max_length=35)
    descripcion = models.CharField (max_length=150)

    def __str__ (self):
        return f'La formación musical {self.nombre_grupo}, de {self.pais_origen}'
    

class Avatar(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return f'{self.user} -{self.imagen}'

    