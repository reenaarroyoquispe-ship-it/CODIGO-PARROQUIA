class Repositorio:

    def __init__(self):
        self.personas = []
        self.inscripciones = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def agregar_inscripcion(self, inscripcion):
        self.inscripciones.append(inscripcion)

    def mostrar_feligreses(self):
        print("\n=== LISTA DE FELIGRESES ===")
        hay_datos = False
        for p in self.personas:
            if p.__class__.__name__ == "Feligres":
                p.mostrar_datos()
                print("-" * 20)
                hay_datos = True
        if not hay_datos:
            print("No hay feligreses registrados.")

    def mostrar_sacerdotes(self):
        print("\n=== LISTA DE SACERDOTES ===")
        hay_datos = False
        for p in self.personas:
            if p.__class__.__name__ == "Sacerdote":
                p.mostrar_datos()
                print("-" * 20)
                hay_datos = True
        if not hay_datos:
            print("No hay sacerdotes registrados.")

    def mostrar_inscripciones(self):
        print("\n=== LISTA DE SACRAMENTOS REGISTRADOS ===")
        if not self.inscripciones:
            print("No hay sacramentas registrados.")
        for i in self.inscripciones:
            i.mostrar_datos()
            print("-" * 20)
