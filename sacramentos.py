class Sacramento:

    def __init__(self, nombre_sacramento, costo):
        self.nombre_sacramento = nombre_sacramento
        self.costo = costo

    def mostrar_detalle(self):
        print("Sacramento:", self.nombre_sacramento)
        print("Costo de tramitación: S/.", self.costo)


class Bautizo(Sacramento):

    def __init__(self, costo, fecha_bautizo):
        super().__init__("Bautizo", costo)
        self.fecha_bautizo = fecha_bautizo

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print("Fecha programada para el bautizo:", self.fecha_bautizo)


class Matrimonio(Sacramento):

    def __init__(self, costo, iglesia_boda):
        super().__init__("Matrimonio", costo)
        self.iglesia_boda = iglesia_boda

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print("Lugar de la boda:", self.iglesia_boda)
