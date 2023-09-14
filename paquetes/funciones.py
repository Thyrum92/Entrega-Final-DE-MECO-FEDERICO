encabezado = "Usuario,Contraseña,Nombre,Apellido,DNI,Saldo"
def crear_db(ruta,archivo): #Funcion para crear bd

    try: #Intento leer el archivo, si se puede es porque existe, si no existe, se crea un archivo con encabezado.

        lectura = open(f"{ruta}/{archivo}", "r")

        print("Leyendo Archivo...")

        lectura.close()

    except:

        f = open(f"{ruta}/{archivo}", "w")

        f.write(f"{encabezado} \n")

        print("Archivo creado con exito")

        f.close()

def validador_input(usuario,u,ruta,archivo): #Funcion validadora de datos
  while len(usuario) < 5:
    usuario = input(f"{u} tiene menos de 5 caracteres, intentelo nuevamente").strip()

  f = open(f"{ruta}/{archivo}", "r") # leo el archivo para trabajarlo

  dic = {} # Creo un diccionario vacio

  for l in f.readlines(): #Leo las lineas y las separo 2 partes por ',' parra luego ingresarlas en el diccionario
    if l != encabezado:
      partes = l.split(",")

      dic[partes[0]] = partes[1]
    else:

      pass

  f.close()

  while usuario in dic:
    usuario = input("Ese nombre de usuario ya existe. Por favor, ingrese otro nombre de usuario: ").strip()

  return usuario

def subida_bd(u,p,ruta,archivo,nom,ape,dni): #Funcion para subida a la bd

  dic = {"usuario":u,"contraseña":p,"nombre":nom,"apellido":ape,"dni":dni,"saldo":str(0)} #Se genera el diccionario para guardar el usuario y contraseña suministrado por el user

  f = open(f"{ruta}/{archivo}", "a") #Se abre el archivo con apertura A para agregar datos.

  f.write(dic["usuario"] + "," + dic["contraseña"] + "," + dic["nombre"] + "," + dic["apellido"] + "," + dic["dni"] + "," + dic["saldo"] + "\n") # Se guarda en la base de datos

  print(f"{u} felicitaciones, te registraste corrrectamente")

  f.close()

def login(ruta,user,password): #Funcion de login

  lectura = open(f"{ruta}/base_datos.txt", "r")

  dic = {}

  for l in lectura.readlines(): #Leo las lineas y las separo 2 partes por ',' para luego ingresarlas en el diccionario

    par = l.split(",")
    usuario = par[0]
    passw = par[1]
    
    dic[usuario] = passw

  if user in dic and dic[user] == password: #Busco la informacion que brindó el user, si coincide, se loguea, sino tira "Datos incorrectos"
      print(f"Bienvenido {user}")
      lectura.close()
      return user
  else:
      print("Datos incorrectos")
      lectura.close()
      exit()
    

def repetirBucle2Opciones(opcion1,descripcion1,opcion2,descripcion2):#Funcion para validar que el usuario seleccione las opciones disponibles

  respuesta = input(f"Bienvenido, desea: \n {opcion1}- {descripcion1} \n {opcion2}- {descripcion2} \n ").lower().strip()

  while respuesta != opcion1 and respuesta != opcion2: # Se valida y verifica que el usuario seleccione las opciones disponibles
    respuesta = input(f"Por favor seleccione una respuesta valida: \n '{opcion1}' {descripcion1} \n '{opcion2}' {descripcion2} \n ").lower().strip()
  return respuesta

def validacionSaldo(saldo): #Funcion para validar opciones de saldo
  while True:

    resp = input(f"Ingresaste {float(saldo)}, es correcto? \n 1- Es correcto \n 2- Quiero cambiarlo ").strip()

    while resp != "1" and resp != "2":
        resp = input(f"Por favor, ingresa 1- para continuar con el valor asignado o 2 para cambiarlo ").strip()
      
    if resp == "1":
        return float(saldo)
    else:
        
      saldo = input("ingrese el saldo que desea agregar ")

def actualizacionDato(usuario,nuevoSaldo,ruta,archivo): #Funcion para actualizar el saldo
  
  lectura = open(f"{ruta}/{archivo}", "r")
  lineas_actualizadas = []
  for l in lectura.readlines():
    partes = l.split(",")
    user = partes[0]

    if user == usuario:
      saldo = float(partes[5])
      saldo += float(nuevoSaldo)
      partes[5] = str(saldo)

      l_actualizada = f"{partes[0]},{partes[1]},{partes[2]},{partes[3]},{partes[4]},{partes[5]}"
      print(l_actualizada)
      print(l)

      lineas_actualizadas.append(f"{l_actualizada}\n")
    else: 
      lineas_actualizadas.append(f"{l}")

  print(lineas_actualizadas)
  f = open(f"{ruta}/{archivo}",'w')

  n = 0

  for la in lineas_actualizadas:
    if n == len(lineas_actualizadas):
      f.write(f"{la}\n")
    else:
       f.write(la)
  
  print(f"Saldo actualizado con exito, su nuevo saldo es de: {saldo}")
  
  f.close()
  lectura.close()

def crearClase(ruta,archivo,usuario,Cliente): #Funcion para crear la clase comprador o actualizarla

    lectura = open(f"{ruta}/{archivo}", "r")

    for l in lectura:
        partes = l.split(",")
        user = partes[0]
        passw = partes[1]
        nom = partes[2]
        ape = partes[3]
        dni = partes[4]
        saldo = partes[5]
        if user == usuario:
            comprador = Cliente(nom,ape,dni,user,passw,float(saldo))
            break
    lectura.close()
    return comprador
