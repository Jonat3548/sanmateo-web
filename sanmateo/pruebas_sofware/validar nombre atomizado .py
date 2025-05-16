# Importar librerías
import re

# Declaración de funciones
def solicitar_nombre():
    """Función que solicita al usuario un nombre."""
    while True:
        try:
            nombre = input("Introduce el primer nombre: ").strip()
            if nombre and validar_nombre(nombre):
                break
            else:
                print("El primer nombre no es válido. Por favor, ingresa un nombre válido.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    return nombre

def validar_nombre(nombre):
    pattern = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$"
    patterence = r"^[!@#$%^&*(),.?\":{}|<>]+$"

    # Validar que el nombre contenga solo letras (mayúsculas y minúsculas) y espacios
    if not re.match(pattern, nombre):
        return False

    # Validar que el nombre no esté vacío
    if len(nombre.strip()) == 0:
        return False

    # Validar longitud mínima de 3 caracteres max 15 caracteres
    if len(nombre) < 3 or len(nombre) > 15:
        return False

    # Validar que el nombre no tenga caracteres especiales (como @, #, $, etc.)
    if re.search(patterence, nombre):
        return False

    return True

def imprimir_resultado(nombre, es_valido):
    """Función que imprime el resultado de la validación."""
    if es_valido:
        print(f"El nombre '{nombre}' es válido.")
    else:
        print(f"El nombre '{nombre}' no es válido. Debe tener entre 3 y 15 caracteres, sin caracteres especiales.")

# Función principal
def main():
    # Solicitar el nombre
    nombre = solicitar_nombre()
    
    # Validar el nombre
    es_valido = validar_nombre(nombre)

    # Imprimir el resultado
    imprimir_resultado(nombre, es_valido)

if __name__ == "__main__":
    main()
