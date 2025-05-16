""" 
Nombre: jonathan steven sanchez trilleras 
Tema: validar NUMERO SIN COGIGO POSTAL
Fecha: 29/03/2025
Lineas de condigo 8 al 48
Correo: jssanchezt@sanmateo.edu.co
"""
import re  #

def es_celular_valido(numero: str) -> bool:
    """
    Verifica si el número de celular ingresado contiene entre 7 y 15 dígitos.
    """
    try:
        if not isinstance(numero, str):
            raise ValueError("⚠️ El número debe ser una cadena de texto.")

        # Patrón para aceptar solo números de 7 a 15 dígitos (sin letras ni símbolos)
        patron = r'^\d{7,15}$'

        # Validación del número con la expresión regular
        return bool(re.match(patron, numero))
    
    except Exception as error:
        print(f"❌ Error en la validación: {error}")
        return False

def solicitar_celular():
    """
    Solicita al usuario un número de celular y valida su formato.
    """
    numero = input("📱 Ingrese un número de celular (solo dígitos, entre 7 y 15 caracteres): ").strip()

    if es_celular_valido(numero):
        print("✅ El número de celular es válido.")
        return numero
    else:
        print("❌ El número de celular no es válido.")

def main():
    """
    Función principal del programa.
    """
    numero_validado = solicitar_celular()

if __name__ == "__main__":
    main()
