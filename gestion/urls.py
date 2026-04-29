from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.lista_clientes, name='clientes'),
    path('empleados/', views.lista_empleados, name='empleados'),
    path('mesas/', views.lista_mesas, name='mesas'),
    path('platos/', views.lista_platos, name='platos'),
    path('ordenes/', views.lista_ordenes, name='ordenes'),
    path('facturas/', views.lista_facturas, name='facturas'),
]
