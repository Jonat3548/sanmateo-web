""" 
Nombre: jonathan steven sanchez trilleras 
Tema: validar correo y numero con assert
Fecha: 29/03/2025
Lineas de condigo 9 al 63
Correo: jssanchezt@sanmateo.edu.co
"""
import re

def validar_correo(correo: str) -> bool:
    """
    Valida si el correo electrónico ingresado cumple con el formato estándar.
    """
    patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(patron, correo) is not None


def validar_telefono(numero: str) -> bool:
    """
    Valida si el número telefónico ingresado tiene entre 7 y 10 dígitos numéricos.
    """
    patron = r"^\d{7,10}$"
    return re.match(patron, numero) is not None


def validar_datos_assert(correo: str, telefono: str, esperado_exito: bool):
    """
    Valida el correo y teléfono usando assert/assert not, según se espere éxito o fallo.
    
    Parámetros:
        esperado_exito (bool): True si se espera validación exitosa, False si se espera fallo.
    """
    print("DATOS INGRESADOS")
    print(f"Correo: {correo}")
    print(f"Teléfono: {telefono}")

    correo_valido = validar_correo(correo)
    telefono_valido = validar_telefono(telefono)

    if esperado_exito:
        # Validación exitosa esperada: ambos deben ser válidos
        assert correo_valido, "Error: correo válido no fue aceptado."
        assert telefono_valido, "Error: teléfono válido no fue aceptado."
        print("Resultado: Validación exitosa.\n")
    else:
        # Validación fallida esperada: al menos uno debe ser inválido
        assert not (correo_valido and telefono_valido), "Error: datos inválidos fueron aceptados."
        print("Resultado: Validación fallida correctamente detectada.")
        if not correo_valido:
            print("Motivo: El correo no es válido.")
        if not telefono_valido:
            print("Motivo: El teléfono no es válido.")
        print()

def validar_datos():
    """
    Solicita correo y teléfono al usuario, los valida e informa si son válidos o no.
    No se usa 'assert', solo muestra resultados.
    """
    correo = input("Ingrese un correo electrónico: ").strip()
    telefono = input("Ingrese un número de celular : ").strip()

    print("\nDATOS INGRESADOS")
    print(f"Correo: {correo}")
    print(f"Teléfono: {telefono}")

    correo_valido = validar_correo(correo)
    telefono_valido = validar_telefono(telefono)

    print("\nRESULTADOS DE VALIDACIÓN:")
    if correo_valido:
        print("Correo válido.")
    else:
        print("Correo NO válido.")

    if telefono_valido:
        print("Teléfono válido.")
    else:
        print("Teléfono NO válido.")

def main():
    # Caso insertado por pantalla
    validar_datos()

    # Caso exitoso
    #validar_datos_assert("usuario@example.com", "3123456789", esperado_exito=True)

    # Caso fallido
    #validar_datos_assert("usuarioexample.com", "abc1234", esperado_exito=False)
    

if __name__ == "__main__":
    main()

