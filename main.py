# Primero van las importaciones de tus otros archivos
from personas import Feligres
from seguridad import validar_dni
from repositorio import Repositorio
from sacramentos import Bautizo
from reportes import ReporteParroquia

# Segundo: Creamos el almacén en blanco
repo = Repositorio()

# Tercero: Iniciamos el interruptor del programa
continuar = True

# Cuarto: El menú que procesa las opciones
while continuar == True:
    print("")
    print("--- MENU DE LA PARROQUIA ---")
    print("1. Registrar Feligres y Bautizo")
    print("2. Mostrar todos los registros")
    print("3. Ver Reporte Estadistico")
    print("4. Salir del programa")
    print("----------------------------")
    
    opcion = input("Elija una opcion (1, 2, 3 o 4): ")
    
    if opcion == "1":
        print("\n--- DATOS DEL FELIGRES ---")
        nom = input("Ingrese el nombre: ")
        doc = input("Ingrese el DNI: ")
        tel = input("Ingrese el telefono: ")
        dir = input("Ingrese la direccion: ")
        
        if validar_dni(doc) == True:
            nuevo_feligres = Feligres(nom, doc, tel, dir)
            
            print("\n--- DATOS DEL BAUTIZO ---")
            fec = input("Ingrese la fecha (DD/MM/AAAA): ")
            cos = input("Ingrese el costo: ")
            
            nuevo_bautizo = Bautizo(nuevo_feligres, fec, cos)
            repo.agregar_inscripcion(nuevo_bautizo)
            print("\n¡Todo se guardo correctamente!")
        else:
            print("\n[ERROR] El DNI debe tener 8 numeros.")
            
    elif opcion == "2":
        repo.mostrar_inscripciones()
        
    elif opcion == "3":
        rep = ReporteParroquia(repo)
        rep.mostrar_resumen()
        
    elif opcion == "4":
        print("\nCerrando el sistema. ¡Adios!")
        continuar = False
        
    else:
        print("\nEsa opcion no existe. Marque 1, 2, 3 o 4.")
