from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from .models import *
from .forms import *


# Vinculando HTMLs que se van a usar.

def pagina_principal(request):
                
    return render(request,'Personal/index.html')

def agregar_empleado(request):

    if request.method == "POST":

        formulario = Personal_form(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            personal = Personal(

                nombre = info["nombre"],
                apellido = info["apellido"],
                dni = info["dni"],
                fecha_nacimiento = info["fecha_nacimiento"],
                mail = info["mail"],
                direccion = info["direccion"],
                localidad = info["localidad"],
                cp = info["cp"],
                numero_contacto = info["numero_contacto"],
                nombre_emergencia = info["nombre_emergencia"],
                apellido_emergencia = info["apellido_emergencia"],
                vinculo = info["vinculo"],
                numero_contacto_emergencia = info["numero_contacto_emergencia"],
                sector = info["sector"]

                )
            
            personal.save()

    else:
        
        formulario = Personal_form()

    return render(request, 'Personal/agregar_empleado.html', {"form":formulario})

def buscar_empleado(request):


    return render(request,'Personal/buscar_empleado.html')

def resultado_busqueda_empleado(request):
    
    if request.GET["apellido"]:

        apellido = request.GET["apellido"]

        personal = Personal.objects.filter(apellido__icontains=apellido)

        return render(request, 'Personal/resultado_busqueda_empleado.html', {'personal':personal, "apellido":apellido})
    
    else:

        resp = "Por favor ingrese un apellido para la busqueda"
    
    return HttpResponse(resp)





























"""user = "lolo"
password = "cuco"

usuarios = Usuario.objects.values_list('user','password')

for u in usuarios:

    if user == u['user'] and password == u['password']:

        return HttpResponse(f'Bienvenido {user}, su pass es {password}')
    
    else:

        return HttpResponse("El user no existe")"""