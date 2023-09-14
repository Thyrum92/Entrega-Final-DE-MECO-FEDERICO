from paquetes.funciones import *
from paquetes.clases import *
import os

root = os.path.dirname(__file__) #Buscando mi ruta raiz

ruta = f"{root}/bd" #Creando la ruta de trababjo

archivo_base = "base_datos.txt"

crear_db(ruta,archivo_base) #Funcion para crear la base de datos

# Preguntando al usuario si desea registrarse o logearse

resp = repetirBucle2Opciones("r","para registrarse","l","para login")

if resp == "r":

  # Pidiendo datos al usuario
  print("Bienvenido al entorno de registro, a continuacion se te solicitaran algunos datos para completar el registro. ")
  usuario = input("Ingrese el nombre de usuario, el mismo debe tener 5 o mas caracteres ")
  u = "El nombre de usuario ingresado"

  usuario = validador_input(usuario,u,ruta,archivo_base) #Funcion validadora

  respuesta2 = input(f"Ingresaste {usuario}, es correcto? y/n ").lower().strip() # Preguntando al usuario si es correcto

  while respuesta2 != 'y' and respuesta2 != 'n': #Siempre que la respuesta sea diferente a y o n, se repetirá el bucle hasta que el user de la respuesta valida
    respuesta2 = input("Selecciona una respuesta valida, 'y' para si, o 'n' para no. Deseas cambiar el usuario ingresado? ").lower().strip()

  while respuesta2 == 'n': #Si la rta es n, se volverá a pedir los datos

    usuario = input("Ingrese el nombre de usuario, el mismo debe tener 5 o mas caracteres ")
    u = "El nombre de usuario ingresado"

    validador_input(usuario,u,ruta,archivo_base) #Funcion validadora

    respuesta2 = input(f"Ingresaste {usuario}, es correcto? y/n").lower().strip()

    while respuesta2 != 'y' and respuesta2 != 'n':
      respuesta2 = input("Selecciona una respuesta valida, 'y' para si, o 'n' para no. Deseas cambiar el usuario ingresado? ").lower().strip()

  if respuesta2 == 'y': # SI la respuesta es y, se le pedirá la contraseña

    contrasenia = input("Ingrese una contraseña, la misma debe tener 5 o mas caracteres ").lower().strip()
    c = "La contraseña ingresada"
    nombre = input("Ingrese su nombre: ").lower().strip()
    apellido = input("Ingrese su apellido: ").lower().strip()
    dni = input("Ingrese su dni: ")

    validador_input(contrasenia,c,ruta,archivo_base)

    subida_bd(usuario,contrasenia, ruta,archivo_base,nombre,apellido,dni)

elif resp == "l":
    usuario = input("Por favor ingrese su nombre de usuario ")
    contrasenia = input("Por favor ingrese su contraseña ")

    login(ruta,usuario,contrasenia)

    comprador = crearClase(ruta,archivo_base,usuario,Cliente)
    
    resp2 = repetirBucle2Opciones("1","Ver informacion","2","Agregar saldo en la cuenta")

    if resp2 == "1":
       
       print(comprador.__str__())
    
    else:
       
       nuevoSaldo = input(f"En este momento su saldo es de: {comprador.saldo} \n Cual es el importe que desea agregar? \n")

       validacionSaldo(nuevoSaldo)

       print(nuevoSaldo)

       actualizacionDato(comprador.usuario,nuevoSaldo,ruta,archivo_base)



    
