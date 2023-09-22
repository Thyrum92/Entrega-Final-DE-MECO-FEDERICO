from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from .models import Usuario


# Vinculando HTMLs que se van a usar.

def login(request):

    return render(request,'Personal/login.html')


def pagina_principal(request):

    return render(request,'Personal/index.html')

def agregar_empleado(request):

    return render(request,'Personal/agregar_empleado.html')

def buscar_empleado(request):

    return render(request,'Personal/buscar_empleado.html')



























"""user = "lolo"
password = "cuco"

usuarios = Usuario.objects.values_list('user','password')

for u in usuarios:

    if user == u['user'] and password == u['password']:

        return HttpResponse(f'Bienvenido {user}, su pass es {password}')
    
    else:

        return HttpResponse("El user no existe")"""