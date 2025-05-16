""" 
Nombre: jonathan steven sanchez trilleras 
Tema: validar NUMERO CON COGIGO POSTAL
Fecha: 29/03/2025
Lineas de condigo 8 al 49
Correo: jssanchezt@sanmateo.edu.co
"""
import re  # Importa el módulo 're' para trabajar con expresiones regulares

def es_numero_celular_valido(numero: str) -> bool:
    """
    Valida si el número de celular tiene el formato correcto: +código_pais número
    Ejemplo válido: +57 3001234567 o +573001234567
    """
    try:
        if not isinstance(numero, str):
            #Asegura que el número ingresado sea un texto, no un número entero o float.
            raise ValueError("El número debe ser una cadena de texto.")

        # Expresión regular: + seguido del código de país (1-3 dígitos) y el número (7-15 dígitos)
        patron = r'^\+\d{1,3}\s?\d{7,15}$'
        return bool(re.match(patron, numero))
    except Exception as e:
        print(f"❌ Error en la validación: {e}")
        return False

def solicitar_numero_celular():
    """
    Solicita al usuario que ingrese un número de celular y valida el formato.
    Repite la solicitud hasta que se ingrese un número válido.
    """
    while True:
        try:
            numero = input("📱 Ingrese un número de celular (+código_pais número): ").strip()
            if es_numero_celular_valido(numero):
                print("✅ El número de celular es válido.")
                return numero
            else:
                print("❌ El número de celular no es válido. Intente nuevamente.")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

def main():
    numero_validado = solicitar_numero_celular()
    # Aquí puedes usar el número si lo necesitas en el programa


if __name__ == "__main__":
    main()
