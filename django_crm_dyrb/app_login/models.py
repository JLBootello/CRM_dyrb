from django.db import models

# Create your models here.
class Representada(models.Model):
    # En esta tabla recogemos los datos de las representadas
    idrepresentadas = models.AutoField(primary_key=True)
    nombre_fiscal = models.CharField(max_length=45)
    nombre_comercial = models.CharField(max_length=45)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=60)
    telefono_corp_1 = models.IntegerField(blank=False)
    telefono_corp_2 = models.IntegerField(blank=True)
    email_corp = models.EmailField(max_length=200, blank=False, unique=True,
        error_messages={'required': 'Por favor, introduzca una dirección de correo valida',
                        'unique': 'Una cuenta con esta dirección de correo ya existe.'},)
    web = models.CharField(max_length=200)