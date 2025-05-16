""" 
Nombre: jonathan steven sanchez trilleras 
Tema: 3. punto de parcial validar nonbre apellido domimicilio numero fecha
Fecha: 12/04/2025
Lineas de condigo 8 al 153
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

def es_celular_valido(numero: str) -> bool:
    try:
        if not isinstance(numero, str):
            raise ValueError("El número debe ser una cadena de texto.")
        patron = r'^\d{7,15}$'

        return bool(re.match(patron, numero))
    
    except Exception as error:
        print(f"Error en la validación: {error}")
        return False

def solicitar_celular():
    numero = input("Ingrese un número de celular (solo dígitos, entre 7 y 15 caracteres): ").strip()

    if es_celular_valido(numero):
        print("El número de celular es válido.")
        return numero
    else:
        print("El número de celular no es válido.")

def validar_correo():
    correo = input("Ingrese su correo electrónico personal: ")
    # solo correo sea de Gmail, Outlook o Hotmail si importar si la priomera es mayuscula o miniscula 
    patron = re.compile(r"^[a-zA-Z0-9._%+-]+@(gmail\.com|outlook\.com|hotmail\.com|Gmail\.com|Outlook\.com|Hotmail\.com)$")

    if patron.match(correo):
        print("El correo personal es válido.")
    else:
        print("El correo personal no es válido. Asegúrese de usar Gmail, Outlook o Hotmail.")

def validar_dirreccion():
    dic = input("Ingrese su dirrecion de de domicilio : ")

    patron = re.compile(
        r"^(Calle|Carrera|Transversal|Diagonal|Avenida|cll|cr|dig|Av\.?\s?(Calle|Carrera)?)"  
        r"\s?\d+[A-Z]?"                     
        r"(?:\s?#\.?)"                   
        r"\s?\d+[A-Z]?[-]?\d*$",            
        re.IGNORECASE                      
    )

    if patron.match(dic):
        print("la dirrecion de domicielio es correcta.")
    else:
        print("a dirrecion de domicielio es incorrecta ingrese bien los parametros .")

def validar_fecha():
    fec = input("Ingrese su fecha de nacimiento ej 18/03/25: ")

    patron = re.compile(
        r"^\d+[/]+\d+[/]+\d"                              
    )

    if patron.match(fec):
        print("fecha correcta ")
    else:
        print("ingreso mal la fecha.")

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
    validar_fecha()
    validar_correo()
    validar_dirreccion()
    solicitar_celular()

if __name__ == '__main__':
    main()
