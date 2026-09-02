import hashlib
from excepciones import DatosInvalidosError

def generar_huella_dni(dni):
    return hashlib.sha256(dni.encode()).hexdigest()

def validar_dni(dni):
    if len(dni) != 8 or not dni.isdigit():
        raise DatosInvalidosError("El DNI debe tener exactamente 8 dígitos numéricos.")
    return True
