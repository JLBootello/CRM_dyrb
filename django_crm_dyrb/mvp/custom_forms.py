from django.forms import ModelForm
from .models import Representada, Contacto_Representada, Cliente_Representada, Staff_Ventas

class RepresentadaForm(ModelForm):
    class Meta:
        model = Representada
        fields = '__all__'

class ContactoRepresentadaForm(ModelForm):
    class Meta:
        model = Contacto_Representada
        fields = '__all__'

class ClienteRepresentadaForm(ModelForm):
    class Meta:
        model = Cliente_Representada
        fields = '__all__'

class StaffVentasForm(ModelForm):
    class Meta:
        model = Staff_Ventas
        fields = '__all__'