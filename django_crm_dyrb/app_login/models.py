from django.db import models

# Create your models here.


class Usuario (models.Model):
    '''Esta es la tabla usuario en la que crearemos los usuarios de la
    base de datos.
    Hay un campo con los valores predefinidos, nivel_permiso'''
    NIVEL_PERMISO = (
        ('A', 'Alto'),
        ('M', 'Medio'),
        ('B', 'Bajo'),
    )
    idusuario = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200, blank=False, unique=True)
    password = models.CharField(max_length=45)
    nivel_permiso = models.CharField(max_length=45, choices=NIVEL_PERMISO)

