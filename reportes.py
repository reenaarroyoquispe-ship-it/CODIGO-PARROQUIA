class ReporteParroquia:

    def __init__(self, repositorio):
        self.repo = repositorio

    def mostrar_resumen(self):
        print("\n================================")
        print("   REPORTE DE LA PARROQUIA     ")
        print("================================")
        
        total_feligreses = 0
        total_sacerdotes = 0
        
        for p in self.repo.personas:
            if p.__class__.__name__ == "Feligres":
                total_feligreses = total_feligreses + 1
            if p.__class__.__name__ == "Sacerdote":
                total_sacerdotes = total_sacerdotes + 1
                
        total_inscripciones = len(self.repo.inscripciones)
        
        print("Feligreses guardados:", total_feligreses)
        print("Sacerdotes guardados:", total_sacerdotes)
        print("Sacramentos guardados:", total_inscripciones)
        print("================================\n")
