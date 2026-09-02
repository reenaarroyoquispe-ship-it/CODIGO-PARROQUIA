class Persona:

    def __init__(self, nombre, dni, telefono):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("DNI:", self.dni)
        print("Teléfono:", self.telefono)


class Feligres(Persona):

    def __init__(self, nombre, dni, telefono, direccion):
        super().__init__(nombre, dni, telefono)
        self.direccion = direccion

    def mostrar_datos(self):
        print("FELIGRÉS")
        super().mostrar_datos()
        print("Dirección:", self.direccion)


class Sacerdote(Persona):

    def __init__(self, nombre, dni, telefono, cargo):
        super().__init__(nombre, dni, telefono)
        self.cargo = cargo

    def mostrar_datos(self):
        print("SACERDOTE")
        super().mostrar_datos()
        print("Cargo:", self.cargo)
