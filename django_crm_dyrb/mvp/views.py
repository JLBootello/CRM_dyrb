from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views import generic
from .custom_forms import RepresentadaForm, ContactoRepresentadaForm, ClienteRepresentadaForm, StaffVentasForm
from django.urls import reverse_lazy
from .models import Representada, Contacto_Representada, Cliente_Representada, Staff_Ventas

# Create your views here.
class RepresentadaView(generic.CreateView):
	form_class = RepresentadaForm
	success_url = reverse_lazy('nuevarepresentada')
	template_name = 'mvp/FormRepresentada.html'

class RepresentadaUpdateView (generic.ListView):
	model = Representada
	template_name = 'mvp/ListaRepresentadas.html'

class ContactoRepresentadaView(generic.CreateView):
	form_class = ContactoRepresentadaForm
	success_url = reverse_lazy('contactorepresentada')
	template_name = 'mvp/FormContactoRepresentada.html'

class ContactoRepresentadaUpdateView(generic.ListView):
	model = Contacto_Representada
	template_name = 'mvp/ListaContactoRepresentada.html'

class ClienteRepresentadaView(generic.CreateView):
	form_class = ClienteRepresentadaForm
	success_url = reverse_lazy('clienterepresentada')
	template_name = 'mvp/FormClienteRepresentada.html'

class ClienteRepresentadaUpdateView(generic.ListView):
	model = Cliente_Representada
	template_name = 'mvp/ListaClienteRepresentada.html'

class StaffVentasView(generic.CreateView):
	form_class = StaffVentasForm
	success_url = reverse_lazy('staffventas')
	template_name = 'mvp/FormStaffVentas.html'

class StaffVentasUpdateView(generic.ListView):
	model = Staff_Ventas
	template_name = 'mvp/ListaStaffVentas.html'