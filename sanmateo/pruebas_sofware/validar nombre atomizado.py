import re

def ingresar_texto():
    while True:
        try:
            texto = input("Ingresa un texto (solo letras y espacios): ")
            
            # Verificar que el texto no esté vacío
            if not texto.strip():
                raise ValueError("El texto no puede estar vacío.")
            
            # Verificar que contenga solo letras y espacios
            regex = "^[a-zA-Z\s]+$"
            if not re.match(regex, texto):
                raise ValueError("El texto sólo puede contener letras y espacios (sin números ni caracteres especiales).")
            
            return texto
        
        except ValueError as e:
            print(f"Error: {e} por favor intenta nuevamente ")
print(ingresar_texto())
