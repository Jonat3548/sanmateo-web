import re  

def validar_nombre(nombre):  
    pattern = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$" 
    simbolos = r"[!@#$%^&*(),.?\":{}|<>]"  
    if len(nombre.strip()) == 0: 
        return False
    if not re.match(pattern, nombre):
        return False
    if re.search(simbolos, nombre): 
        return False
    if len(nombre) < 3 or len(nombre) > 15: 
        return False
    return True 

def validar_nombre_2(nombre):  
    if len(nombre.strip()) == 0:  
        return True
    return validar_nombre(nombre)  

def es_celular_valido(numero: str) -> bool:  
    patron = r'^\d{7,15}$'  
    return bool(re.match(patron, numero))  

def validar_correo_valido(correo: str) -> bool:  
    patron = re.compile(r"^[a-zA-Z0-9._%+-]+@(gmail\.com|outlook\.com|hotmail\.com)$", re.IGNORECASE)
    return patron.match(correo) is not None  

def validar_direccion_valida(dic: str) -> bool:  
    patron = re.compile(
        r"^(Calle|Carrera|Transversal|Diagonal|Avenida|cll|cr|dig|Av\.?\s?(Calle|Carrera)?)"
        r"\s?\d+[A-Z]?\s?#\.?\s?\d+[A-Z]?[-]?\d*$",
        re.IGNORECASE
    )
    return patron.match(dic) is not None  

def validar_fecha_valida(fecha: str) -> bool:
    
    if not re.match(r"^\d{2}/\d{2}/\d{2}$", fecha):
        return False
    dia, mes, año = map(int, fecha.split("/"))  
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes in (1, 3, 5, 7, 8, 10, 12):       
        max_dia = 31
    elif mes in (4, 6, 9, 11):               
        max_dia = 30
    else:                                   
        max_dia = 29
    return dia <= max_dia

def validar_contrasena(contrasena):  
    if len(contrasena) < 4:  
        return False
    if not re.search(r"[A-Z]", contrasena):  
        return False
    if not re.search(r"[a-z]", contrasena):  
        return False
    if not re.search(r"[0-9]", contrasena):  
        return False
    return True 

def validar_todo(nombre, segundo_nombre, apellido, segundo_apellido, telefono, correo, direccion, fecha):
    return all([  
        validar_nombre(nombre),
        validar_nombre(apellido),
        validar_nombre_2(segundo_nombre),
        validar_nombre_2(segundo_apellido),
        es_celular_valido(telefono),
        validar_correo_valido(correo),
        validar_direccion_valida(direccion),
        validar_fecha_valida(fecha)
    ])

def pedir_dato(mensaje, funcion_validadora, obligatorio=True):  # Pide datos y los valida con una función dada
    while True:
        valor = input(mensaje)  # Solicita el valor al usuario
        if not obligatorio and valor.strip() == "":  # Si no es obligatorio y está vacío, se acepta
            return ""
        if funcion_validadora(valor):  # Si es válido, se retorna
            return valor
        else:
            print("Dato inválido. Inténtalo de nuevo.")  # Si no es válido, se repite

def imprimir_datos(datos):  
    print("")
    print("Datos utilizados:")
    for clave, valor in datos.items():  
        print(f"  - {clave}: {valor}")
    print()
    
def validar_con_datos(nombre, segundo_nombre, apellido, segundo_apellido, telefono, correo, direccion, fecha, esperado_valido=True, mensaje=""):
    datos = {
        "nombre": nombre,
        "segundo_nombre": segundo_nombre,
        "apellido": apellido,
        "segundo_apellido": segundo_apellido,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "fecha": fecha
    }

    resultado = validar_todo(**datos)  # Aplica la validación unificada
    assert resultado == esperado_valido, f"{mensaje or 'El caso no pasó la validación como se esperaba.'}"
    
    if resultado:
        print(f"{mensaje or 'Validación completa exitosa'}")
    else:
        print(f"{mensaje or 'Validación fallida correctamente detectada'}")

    imprimir_datos(datos)  # Muestra los datos validados
    return correo if resultado else None  # Retorna el correo si fue válido


def login(usuarios):  
    print("")
    print("INICIO DE SESIÓN")
    intentos_restantes = 3
    while intentos_restantes > 0:  
        correo = input("Correo: ").strip()
        contrasena = input("Contraseña: ").strip()
        if correo in usuarios and usuarios[correo] == contrasena: 
            print(f"Bienvenido, {correo}")
            return True
        else:
            intentos_restantes -= 1  
            if correo not in usuarios:
                print("Correo no registrado.")
                print("")
            else:
                print("Contraseña incorrecta.")
                print("")
            if intentos_restantes > 0:
                print(f"Te quedan {intentos_restantes} intento.")
            else:
                print("Acceso bloqueado. Excediste el número de intentos.")
                return False

if __name__ == "__main__":  
    usuarios_validos = {}  

    print("CASO 1: Ingreso manual desde consola")
    print("")
    nombre = pedir_dato("Nombre: ", validar_nombre)
    segundo_nombre = pedir_dato("Segundo nombre (opcional): ", validar_nombre_2, obligatorio=False)
    apellido = pedir_dato("Apellido: ", validar_nombre)
    segundo_apellido = pedir_dato("Segundo apellido (opcional): ", validar_nombre_2, obligatorio=False)
    telefono = pedir_dato("Teléfono (7 a 15 dígitos): ", es_celular_valido)
    correo = pedir_dato("Correo (gmail, hotmail, outlook): ", validar_correo_valido)
    direccion = pedir_dato("Dirección (formato Calle/Carrera ej: calle 38f # 15-18): ", validar_direccion_valida)
    fecha = pedir_dato("Fecha (formato dd/mm/aa): ", validar_fecha_valida)

    if validar_todo(nombre, segundo_nombre, apellido, segundo_apellido, telefono, correo, direccion, fecha):
        contrasena = pedir_dato("Contraseña (mínimo 4 caracteres, mayúscula, minúscula y número): ", validar_contrasena)
        usuarios_validos[correo] = contrasena
        print("Usuario registrado con éxito.")
        print("")

    print("CASO 2: Todos los datos inválidos")
    validar_con_datos(
        nombre="123",
        segundo_nombre="!!!",
        apellido="@@@",
        segundo_apellido="###",
        telefono="abcde",
        correo="correo@invalido.com",
        direccion="direccion falsa",
        fecha="10-05-2025",
        esperado_valido=False,
        mensaje="Todos los datos son inválidos"
    )

    print("CASO 3: Datos mixtos (algunos válidos, otros inválidos)")
    validar_con_datos(
        nombre="Jonathan",
        segundo_nombre="123",
        apellido="Sanchez",
        segundo_apellido="*",
        telefono="abc123",
        correo="jssanchezt@gmail.com",
        direccion="direccion falsa",
        fecha="10/05/25",
        esperado_valido=False,
        mensaje="Algunos datos inválidos"
    )

    print("CASO 4: Todos los datos válidos, otro escenario")
    correo4 = validar_con_datos(
        nombre="Ana",
        segundo_nombre="",
        apellido="Gómez",
        segundo_apellido="Lopez",
        telefono="3001234567",
        correo="ana.gomez@outlook.com",
        direccion="Carrera 8 #34-56",
        fecha="05/10/25",
        esperado_valido=True,
        mensaje="Todos los datos válidos en otra estructura"
    )
    if correo4:
        usuarios_validos[correo4] = "Ana12345"

    print("Usuarios registrados:")
    for user, pwd in usuarios_validos.items():  
        print(f"  - {user}: {pwd}")

    login(usuarios_validos)  
