from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('representada/', views.representada.as_view(), name='representada')
]