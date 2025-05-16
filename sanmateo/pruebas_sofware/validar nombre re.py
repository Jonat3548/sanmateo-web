import re

def capturar_nombre():
    nombre = input("Por favor, ingresa tu nombre: ")
    return nombre

def validar_nombre(nombre):
    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'  
    if re.match(patron, nombre):
        return True
    else:
        return False
def mostrar_nombre(nombre):
    print("El nombre capturado es:", nombre)

def main():
    nombre_usuario = capturar_nombre()
    if validar_nombre(nombre_usuario):
        mostrar_nombre(nombre_usuario)
    else:
        print("El nombre ingresado no es valido caracteres esciales solo letras y espacios")
main()