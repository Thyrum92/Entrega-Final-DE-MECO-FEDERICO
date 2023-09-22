from django.urls import path
from Personal.views import *

urlpatterns = [
    path("", login),
    path("index.html", pagina_principal),
    path("agregar_empleado.html",agregar_empleado),
    path("buscar_empleado.html",buscar_empleado),


]
