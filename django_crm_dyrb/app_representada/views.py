from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views import generic
from .custom_forms import RepresentadaForm
from django.urls import reverse_lazy

# Create your views here.
class representada(generic.CreateView):
	form_class = RepresentadaForm
	success_url = reverse_lazy('representada')
	template_name = 'app_representada/form_Representada.html'