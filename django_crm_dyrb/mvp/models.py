from django.db import models

# Create your models here.
class Representada(models.Model):
    ''' En esta tabla recogemos los datos de las representadas '''
    idrepresentada = models.AutoField(primary_key=True)
    nombre_fiscal = models.CharField(max_length=45, blank=False)
    cif = models.CharField(max_length=45, blank=False)
    nombre_comercial = models.CharField(max_length=45)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=60)
    telefono_corp_1 = models.IntegerField(blank=False)
    telefono_corp_2 = models.IntegerField(blank=True)
    email_corp = models.EmailField(max_length=200, blank=False, unique=True,
        error_messages={'blank': 'Por favor, introduzca una dirección de correo valida',
                        'unique': 'Una cuenta con esta dirección de correo ya existe.'},)
    web = models.CharField(max_length=200)



class Contacto_Representada(models.Model):
    '''En esta tabla recogemos aquellos contactos que provienen de las
        representadas.
        Va a haber dos campos con los valores restringidos, departamento y
        nivel_responsabilidad.'''
    DEPARTAMENTO = (
        ('PA', 'Propietario'),
        ('C', 'Comercial'),
        ('F', 'Financiero'),
        ('P', 'Producción'),
    )
    NIVEL_DECISION = (
        ('A', 'Alto'),
        ('M', 'Medio'),
        ('B', 'Bajo'),
    )
    idrepresentada = models.ForeignKey(Representada, on_delete=models.CASCADE)
    idcontacto_representada = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=45, blank=False)
    telefono_movil = models.IntegerField(blank=True)
    email = models.EmailField(max_length=200, blank=False, unique=True,
        error_messages={'blank': 'Por favor, introduzca una dirección de correo valida',
                        'unique': 'Una cuenta con esta dirección de correo ya existe.'},)
    nivel_decision = models.CharField(max_length=45, choices=NIVEL_DECISION)
    departamento = models.CharField(max_length=45, choices=DEPARTAMENTO)



class Cliente_Representada (models.Model):
    idcliente_representada = models.AutoField(primary_key=True)
    nombre_fiscal = models.CharField(max_length=45, blank=False)
    cif = models.CharField(max_length=45,blank=False)
    nombre_comercial = models.CharField(max_length=45)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=60)
    telefono_corp_1 = models.IntegerField(blank=False)
    telefono_corp_2 = models.IntegerField(blank=True)
    email_corp = models.EmailField(max_length=200, blank=False, unique=True,
        error_messages={'blank': 'Por favor, introduzca una dirección de correo valida',
                        'unique': 'Una cuenta con esta dirección de correo ya existe.'},)
    web = models.CharField(max_length=200)

class Contacto_Cliente_Representada(models.Model):
    '''En esta tabla recogemos aquellos contactos que provienen de los
        clientes de las representadas.
        Va a haber dos campos con los valores restringidos, departamento y
        nivel_responsabilidad.'''
    DEPARTAMENTO = (
        ('PA', 'Propiedad'),
        ('C', 'Comercial'),
        ('F', 'Financiero'),
        ('A', 'Almacén'),
    )
    NIVEL_DECISION = (
        ('A', 'Alto'),
        ('M', 'Medio'),
        ('B', 'Bajo'),
    )
    idcliente_representada = models.ForeignKey(Cliente_Representada, on_delete=models.CASCADE)
    idcontacto_cliente_representada = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=45)
    telefono_movil = models.IntegerField(blank=True)
    email = models.EmailField(max_length=200, blank=True, unique=True)
    nivel_decision = models.CharField(max_length=45, choices=NIVEL_DECISION)
    departamento = models.CharField(max_length=45, choices=DEPARTAMENTO)

class Staff_Ventas (models.Model):

    '''En esta clase vamos a recoger a los actores de las ventas de dyrb'''

    idstaff_ventas= models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=45)
    telefono_movil = models.IntegerField(blank=True)
    email = models.EmailField(max_length=200, blank=False, unique=True,
        error_messages={'blank': 'Por favor, introduzca una dirección de correo valida',
                        'unique': 'Una cuenta con esta dirección de correo ya existe.'},)

class Representacion (models.Model):
    '''En esta tabla recogemos las relaciones entre las tablas de comercial,
    cliente_representada y representada'''
    idrepresentacion = models.AutoField(primary_key=True)
    idrepresentada = models.ForeignKey(Representada, on_delete=models.CASCADE)
    idcliente_representada = models.ForeignKey(Cliente_Representada, on_delete=models.CASCADE)
    idstaff_ventas = models.ForeignKey(Staff_Ventas, on_delete=models.CASCADE)