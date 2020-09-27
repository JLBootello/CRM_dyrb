from django.urls import path
from . import views

urlpatterns = [
    path('nuevarepresentada', views.RepresentadaView.as_view(), name='nueva_representada'),
    path('listarepresentadas', views.RepresentadaUpdateView.as_view(), name='lista_representadas'),
]
