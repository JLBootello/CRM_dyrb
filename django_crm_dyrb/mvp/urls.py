from django.urls import path
from . import views

urlpatterns = [
    path('nuevarepresentada', views.RepresentadaView.as_view(), name='nueva_representada'),
    path('listarepresentadas', views.RepresentadaUpdateView.as_view(), name='lista_representadas'),
    path('contactorepresentada', views.ContactoRepresentadaView.as_view(), name='contacto_representada'),
    path('listacontactosrepresentadas', views.ContactoRepresentadaUpdateView.as_view(), name='lista_contactos_representadas'),
    path('clienterepresentada', views.ClienteRepresentadaView.as_view(), name='cliente_representada'),
    path('listaclientesrepresentadas', views.ClienteRepresentadaUpdateView.as_view(), name='lista_clientes_representadas'),
    path('staffventas', views.StaffVentasView.as_view(), name='staff_ventas'),
    path('listastaffventas', views.StaffVentasUpdateView.as_view(), name='lista_staff_ventas'),
]
