from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views import generic
from .custom_forms import RepresentadaForm
from django.urls import reverse_lazy
from .models import Representada

# Create your views here.
class RepresentadaView(generic.CreateView):
	form_class = RepresentadaForm
	success_url = reverse_lazy('representada')
	template_name = 'mvp/form_Representada.html'

class RepresentadaUpdateView (generic.ListView):
	model = Representada
	template_name = 'mvp/listarepresentada.html'