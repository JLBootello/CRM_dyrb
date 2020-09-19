from django.db import models

# Create your models here.

class representacion (models.Model):
    '''En esta tabla recogemos las relaciones entre las tablas de comercial,
    cliente_representada y representada'''
    idrepresentacion = models.AutoField(primary_key=True)
    idrepresentada = models.ForeignKey(representada, on_delete=models.CASCADE)
    idcliente_representada = models.ForeignKey(cliente_representada, on_delete=models.CASCADE)
    idstuff_ventas = models.ForeignKey(stuff_ventas, on_delete=models.CASCADE)

class usuario (models.Model):
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

class representada(models.Model):
    ''' En esta tabla recogemos los datos de las representadas '''
    idrepresentada = models.AutoField(primary_key=True)
    nombre_fiscal = models.CharField(max_length=45)
    cif = models.IntegerField(blank=False)
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

class contacto_representada(models.Model):
    '''En esta tabla recogemos aquellos contactos que provienen de las
        representadas.
        Va a haber dos campos con los valores restringidos, departamento y
        nivel_responsabilidad.'''
    DEPARTAMENTO = (
        ('C', 'Comercial'),
        ('F', 'Financiero'),
        ('P', 'Producción'),
    )
    NIVEL_DECISION = (
        ('A', 'Alto'),
        ('M', 'Medio'),
        ('B', 'Bajo'),
    )
    idrepresentada = models.ForeignKey(representada, on_delete=models.CASCADE)
    idcontacto_representada = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=45)
    telefono_movil = models.IntegerField(blank=True)
    email = models.EmailField(max_length=200, blank=True, unique=True)
    nivel_decision = models.CharField(max_length=45, choices=NIVEL_DECISION)
    departamento = models.CharField(max_length=45, choices=DEPARTAMENTO)

class cliente_representada (models.Model):
    idcliente_representada = models.AutoField(primary_key=True)
    nombre_fiscal = models.CharField(max_length=45)
    cif = models.IntegerField(blank=False)
    nombre_comercial = models.CharField(max_length=45)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=60)
    telefono_corp_1 = models.IntegerField(blank=False)
    telefono_corp_2 = models.IntegerField(blank=True)
    email_corp = models.EmailField(max_length=200, blank=False, unique=True,
                                   error_messages={'required': 'Por favor, introduzca una dirección de correo valida',
                                                   'unique': 'Una cuenta con esta dirección de correo ya existe.'}, )
    web = models.CharField(max_length=200)

class contacto_cliente_representada(models.Model):
    '''En esta tabla recogemos aquellos contactos que provienen de los
        clientes de las representadas.
        Va a haber dos campos con los valores restringidos, departamento y
        nivel_responsabilidad.'''
    DEPARTAMENTO = (
        ('C', 'Comercial'),
        ('F', 'Financiero'),
        ('A', 'Almacén'),
    )
    NIVEL_DECISION = (
        ('A', 'Alto'),
        ('M', 'Medio'),
        ('B', 'Bajo'),
    )
    idcliente_representada = models.ForeignKey(cliente_representada, on_delete=models.CASCADE)
    idcontacto_cliente_representada = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=45)
    telefono_movil = models.IntegerField(blank=True)
    email = models.EmailField(max_length=200, blank=True, unique=True)
    nivel_decision = models.CharField(max_length=45, choices=NIVEL_DECISION)
    departamento = models.CharField(max_length=45, choices=DEPARTAMENTO)

class stuff_ventas (models.Model):

    '''En esta clase vamos a recoger a los actores de las ventas de dyrb'''

    idstuff_ventas= models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=45)
    telefono_movil = models.IntegerField(blank=True)
    email = models.EmailField(max_length=200, blank=True, unique=True)