class Sacramento:

    def __init__(self, beneficiario, fecha, costo):
        self.beneficiario = beneficiario
        self.fecha = fecha
        self.costo = costo

    def mostrar_datos(self):
        print("Actividad:", self.tipo())
        print("Beneficiario:", self.beneficiario.nombre)
        print("Fecha:", self.fecha)
        print("Costo: S/.", self.costo)

    def tipo(self):
        return "Sacramento"


class Bautizo(Sacramento):

    def tipo(self):
        return "Bautizo"


class Matrimonio(Sacramento):

    def tipo(self):
        return "Matrimonio"


class Retiro(Sacramento):

    def tipo(self):
        return "Retiro"
