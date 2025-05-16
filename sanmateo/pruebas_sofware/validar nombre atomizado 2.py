""" 
Nombre: jonathan steven sanchez trilleras 
Tema: validar nombre atomizado utilizado try except
Fecha: 29/03/2025
Lineas de condigo 8 al 90
Correo: jssanchezt@sanmateo.edu.co

"""

import re

# Validar el nombre individual
def validar_nombre(nombre):
    pattern = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$"
    patterence = r"[!@#$%^&*(),.?\":{}|<>]"

    # Validar solo si se escribió algo
    if len(nombre.strip()) == 0:
        return False
    if not re.match(pattern, nombre):
        return False
    if re.search(patterence, nombre):
        return False
    if len(nombre) < 3 or len(nombre) > 15:
        return False

    return True

def validar_nombre_2(nombre):
    pattern = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$"
    patterence = r"[!@#$%^&*(),.?\":{}|<>]"

    # Validar solo si se escribió algo
    if len(nombre.strip()) == 0:
        return True
    if not re.match(pattern, nombre):
        return False
    if re.search(patterence, nombre):
        return False
    if len(nombre) < 3 or len(nombre) > 15:
        return False

    return True

# Función para solicitar cualquier campo
def solicitar_nombre(campo, obligatorio=True):
    while True:
        try:
            nombre = input(f"Introduce {campo}: ").strip()
            if not nombre:
                if not obligatorio:
                    return ""  # Campo opcional vacío
                else:
                    print(f"{campo} es obligatorio. No puede estar vacío.")
                    continue
            if validar_nombre(nombre) if obligatorio else validar_nombre_2(nombre):
                return nombre
            else:
                print(f"{campo} no es válido. Por favor, ingresa un valor válido.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")


# Función para mostrar el nombre completo final
def imprimir_resultado(nombre_completo, es_valido):
    if es_valido:
        print(f"Nombre completo: {nombre_completo}")
    else:
        print("Uno o más campos obligatorios no son válidos.")

# Función principal
def main():
    # Solicitar datos
    primer_nombre = solicitar_nombre("el primer nombre", obligatorio=True)
    segundo_nombre = solicitar_nombre("el segundo nombre (opcional)", obligatorio=False)
    primer_apellido = solicitar_nombre("el primer apellido", obligatorio=True)
    segundo_apellido = solicitar_nombre("el segundo apellido (opcional)", obligatorio=False)

    es_valido = all([
        validar_nombre(primer_nombre),
        validar_nombre(primer_apellido),
        validar_nombre_2(segundo_nombre),
        validar_nombre_2(segundo_apellido)
    ])

    # nombre completo
    nombre_completo = f"{primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}".strip()

    imprimir_resultado(nombre_completo, es_valido)

if __name__ == "__main__":
    main()

