from django.forms import ModelForm
from app_login.models import Representada

class RepresentadaForm(ModelForm):
    class Meta:
        model = Representada
        fields = '__all__'