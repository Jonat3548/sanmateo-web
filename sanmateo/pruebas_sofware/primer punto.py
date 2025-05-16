""" 
Nombre: jonathan steven sanchez trilleras 
Tema: 1. punto de parcial validar CORREO PERSONAL 
Fecha: 12/04/2025
Lineas de condigo 8 al 25
Correo: jssanchezt@sanmateo.edu.co
"""
import re  

def validar_correo():
    correo = input("Ingrese su correo electrónico personal: ")
    # solo correo sea de Gmail, Outlook o Hotmail si importar si la priomera es mayuscula o miniscula 
    patron = re.compile(r"^[a-zA-Z0-9._%+-]+@(gmail\.com|outlook\.com|hotmail\.com|Gmail\.com|Outlook\.com|Hotmail\.com)$")

    if patron.match(correo):
        print("El correo personal es válido.")
    else:
        print("El correo personal no es válido. Asegúrese de usar Gmail, Outlook o Hotmail.")

def main():
    validar_correo()


if __name__ == '__main__':
    main()

