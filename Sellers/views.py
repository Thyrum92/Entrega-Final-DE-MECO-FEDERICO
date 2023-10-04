from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def inicio_sellers(request):
    return render(request,'Sellers/inicio_sellers.html')

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

            return render(request, 'Sellers/seller_agregado.html',{"seller":seller.nickname,"r_z":seller.razon_social})

    else:
        
        formulario = Seller_form()

    return render(request, 'Sellers/agregar_seller.html', {"form2":formulario})

def seller_agregado(request):

    return render(request, 'Sellers/seller_agregado.html')

def buscar_seller(request):
    return render(request,"Sellers/buscar_seller.html")

def resultado_busqueda_seller(request):
    
    if request.GET["nickname"]:

        nickname = request.GET["nickname"]

        sellers = Seller.objects.filter(nickname__icontains=nickname)

        return render(request, 'Sellers/resultado_busqueda_seller.html', {'seller':sellers, "nickname":nickname})
    
    else:

        sellers = Seller.objects.all()
    
    return render(request, 'Sellers/resultado_busqueda_seller.html', {'seller':sellers})
