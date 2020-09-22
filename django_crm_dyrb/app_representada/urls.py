from django.urls import path
from . import views

urlpatterns = [
    path('', views.representada.as_view(), name='representada'),
]
