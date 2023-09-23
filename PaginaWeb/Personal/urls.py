from django.urls import path
from Personal.views import *

urlpatterns = [
    path("index.html", pagina_principal, name="inicio"),
    path("agregar_empleado.html",agregar_empleado, name="agregar_empleado"),
    path("buscar_empleado.html",buscar_empleado, name="buscar_empleado"),
    path("resultado_busqueda_empleado.html",resultado_busqueda_empleado, name="busqueda_empleado")

]
