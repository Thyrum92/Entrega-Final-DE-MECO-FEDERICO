class Cliente():
    def __init__(self,nombre,apellido,dni,usuario,contrasenia,saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.saldo = saldo
    
    def __str__(self):
        if self.saldo == str(0):
            return f"El cliente es: {self.nombre} {self.apellido} \n Su dni es: {self.dni}. Su nombre de usuario es: {self.usuario} y su contraseña: {self.contrasenia} \n No posee saldo disponible"
        else:
            return f"El cliente es: {self.nombre} {self.apellido} \n Su nombre de usuario es: {self.usuario} y su contraseña: {self.contrasenia} \n Su saldo disponible es de: {self.saldo}"
    
    def bienvenida(self):
        return f"Bienvenido {self.nombre}"
    
    def agregarSaldo(self, saldo):
        self.saldo += saldo