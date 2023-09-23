from django.urls import path
from Personal.views import *

urlpatterns = [
    path("index/", pagina_principal, name="Inicio"),
    path("agregar_empleado/",agregar_empleado, name="Agregar Empleado"),
    path("buscar_empleado/",buscar_empleado, name="Buscar Empleado"),
    path("resultado_busqueda_empleado/",resultado_busqueda_empleado, name="Busqueda Empleado"),
    path("Agregar_seller/",agregar_seller,name="Agregar Seller"),
    path("buscar_seller/",buscar_seller,name="buscar_seller"),
    path("resultado_busqueda_seller/",resultado_busqueda_seller,name="resultado_busqueda_seller"),

]
