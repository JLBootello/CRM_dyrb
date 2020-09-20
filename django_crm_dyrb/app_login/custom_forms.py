from django.forms import ModelForm
from .models import Representada

class RepresentadaForm(ModelForm):
    class Meta:
        model = Representada
        fields = '__all__'