""" 
Nombre: jonathan steven sanchez trilleras 
Tema: validar CORREO PERSONAL O CORPORTATIVO
Fecha: 29/03/2025
Lineas de condigo 8 al 35
Correo: jssanchezt@sanmateo.edu.co
"""
import re  

def validar_correo_personal():
    correo = input("Ingrese su correo electrónico personal: ")
    # Esta expresión valida que el correo sea de Gmail, Outlook o Hotmail
    patron = re.compile(r"^[a-zA-Z0-9._%+-]+@(gmail\.com|outlook\.com|hotmail\.com)$")

    if patron.match(correo):
        print("✅ El correo personal es válido.")
    else:
        print("❌ El correo personal no es válido. Asegúrese de usar Gmail, Outlook o Hotmail.")

def validar_correo_corporativo():
    correo = input("Ingrese su correo electrónico corporativo: ")
    # Esta expresión valida que tenga el formato correcto tipo usuario@empresa.com
    patron = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    if patron.match(correo):
        print("✅ El correo corporativo es válido.")
    else:
        print("❌ El correo corporativo no es válido. Verifique el formato.")

def main():
    validar_correo_personal()
    validar_correo_corporativo()

if __name__ == '__main__':
    main()

