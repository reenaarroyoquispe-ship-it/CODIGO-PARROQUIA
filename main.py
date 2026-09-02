from personas import Feligres
from seguridad import validar_dni
from excepciones import DatosInvalidosError

def menu():
    print("\n--- SISTEMA PARROQUIAL ---")
    print("1. Registrar Feligrés")
    print("2. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        telefono = input("Ingrese teléfono: ")
        direccion = input("Ingrese dirección: ")
        dni = input("Ingrese DNI: ")
        
        try:
            # Aquí tu código de seguridad intercepta y valida el DNI ingresado
            if validar_dni(dni):
                nuevo_feligres = Feligres(nombre, dni, telefono, direccion)
                print("\n¡Feligrés registrado con éxito!")
                nuevo_feligres.mostrar_datos()
                
        except DatosInvalidosError as e:
            # Si el DNI está mal, tu excepción atrapa el error y avisa en pantalla
            print(f"\n[ERROR]: {e}")
            print("El feligrés no pudo ser registrado.")
            
    elif opcion == "2":
        print("Saliendo del sistema...")
        return False
    else:
        print("Opción no válida.")
    return True

# Bucle para mantener el programa corriendo
corriendo = True
while corriendo:
    corriendo = menu()
