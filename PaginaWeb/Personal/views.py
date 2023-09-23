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
                sector = info["sector"],
                permisos = info["permisos"]

                )
            
            personal.save()

            return render(request, 'Personal/agregar_empleado.html')

    else:
        
        formulario = Personal_form()

    return render(request, 'Personal/agregar_empleado.html', {"form":formulario})

def buscar_empleado(request):


    return render(request,'Personal/buscar_empleado.html')

def seller_agregado(request):

    return render(request, 'Personal/seller_agregado.html')

def resultado_busqueda_empleado(request):
    
    if request.GET["apellido"]:

        apellido = request.GET["apellido"]

        personal = Personal.objects.filter(apellido__icontains=apellido)

        return render(request, 'Personal/resultado_busqueda_empleado.html', {'personal':personal, "apellido":apellido})
    
    else:

        personal = Personal.objects.all()
    
    return render(request, 'Personal/resultado_busqueda_empleado.html', {'personal':personal})

def agregar_seller(request):

    if request.method == "POST":

        formulario = Seller_form(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            seller = Seller(

                cust_id = info["cust_id"],
                nickname = info["nickname"],
                razon_social = info["razon_social"],
                nombre_responsable = info["nombre_responsable"],
                apellido_responsable = info["apellido_responsable"],
                contacto_resonsable = info["contacto_resonsable"],
                servicio_0 = info["servicio_0"],
                servicio_1 = info["servicio_1"],
                servicio_2 = info["servicio_2"],
                servicio_3 = info["servicio_3"],
                servicio_4 = info["servicio_4"],

                )
            
            seller.save()

            return render(request, 'Personal/seller_agregado.html',{"seller":seller.nickname,"r_z":seller.razon_social})

    else:
        
        formulario = Seller_form()

    return render(request, 'Personal/agregar_seller.html', {"form2":formulario})

def buscar_seller(request):
    return render(request,"Personal/buscar_seller.html")

def resultado_busqueda_seller(request):
    
    if request.GET["nickname"]:

        nickname = request.GET["nickname"]

        sellers = Seller.objects.filter(nickname__icontains=nickname)

        return render(request, 'Personal/resultado_busqueda_seller.html', {'seller':sellers, "nickname":nickname})
    
    else:

        sellers = Seller.objects.all()
    
    return render(request, 'Personal/resultado_busqueda_seller.html', {'seller':sellers})