""" 
Nombre: jonathan steven sanchez trilleras 
Tema: 2. Punto Parcial Validaciones Con Unitest y Login. 
Fecha: 16/05/2025
Lineas de condigo 8 al 240
Correo: jssanchezt@sanmateo.edu.co
"""
import re
import unittest

diccionario_usuarios_autorizados = {}

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

def validar_todo(nombre, segundo_nombre, apellido, segundo_apellido, telefono, correo, direccion, fecha, contrasena, nombre_caso=""):
    valores = {
        "nombre": nombre,
        "segundo_nombre": segundo_nombre,
        "apellido": apellido,
        "segundo_apellido": segundo_apellido,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "fecha": fecha,
        "contrasena": contrasena
    }

    validaciones = {
        "nombre": validar_nombre(nombre),
        "segundo_nombre": validar_nombre_2(segundo_nombre),
        "apellido": validar_nombre(apellido),
        "segundo_apellido": validar_nombre_2(segundo_apellido),
        "telefono": es_celular_valido(telefono),
        "correo": validar_correo_valido(correo),
        "direccion": validar_direccion_valida(direccion),
        "fecha": validar_fecha_valida(fecha),
        "contrasena": validar_contrasena(contrasena)
    }

    todo_valido = all(validaciones.values())
    print("")
    print(f"Resultado del {nombre_caso}")
    if todo_valido:
        diccionario_usuarios_autorizados[correo] = contrasena
        print("Todos los datos son validos.")
        print("")
    else:
        print("Se encontraron errores en los sigientes campos:")
        for campo, valido in validaciones.items():
            if not valido:
                print(f"  - Campo invalido: {campo} = {valores[campo]}")
        print()
    return todo_valido

class TestValidaciones(unittest.TestCase):

    def test_01_completo_valido(self):
        self.assertTrue(validar_todo(
            nombre="Ana",
            segundo_nombre="Lucia",
            apellido="Gomez",
            segundo_apellido="Perez",
            telefono="3001234567",
            correo="ana.gomez@gmail.com",
            direccion="Calle 5 #10-22",
            fecha="10/05/25",
            contrasena="Ana1234",
            nombre_caso="CASO 1"
        ))

    def test_02_completo_invalido(self):
        self.assertFalse(validar_todo(
            nombre="153sfds",
            segundo_nombre="!",
            apellido="@@",
            segundo_apellido="##",
            telefono="abcdef",
            correo="correo@invalido.com",
            direccion="por ahí",
            fecha="32/15/99",
            contrasena="abc",
            nombre_caso="CASO 2"
        ))

    def test_03_otra_persona_valido(self):
        self.assertTrue(validar_todo(
            nombre="Carlos",
            segundo_nombre="",
            apellido="Ramírez",
            segundo_apellido="",
            telefono="3124567890",
            correo="carlos.ramirez@hotmail.com",
            direccion="Carrera 12 #45-89",
            fecha="15/08/25",
            contrasena="Car12345",
            nombre_caso="CASO 3"
        ))

    def test_04_datos_mixtos(self):
        self.assertFalse(validar_todo(
            nombre="Luis123",
            segundo_nombre="",
            apellido="Martínez",
            segundo_apellido="@",  
            telefono="3210000000",
            correo="luis.martinez@outlook.com",
            direccion="Av Calle 10 #20-30",
            fecha="01/01/25",
            contrasena="Luisito",  
            nombre_caso="CASO 4"
        ))

def login(usuarios):
    print("")
    print("INICIO DE SESION")
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
            else:
                print("Contraseña incorrecta.")
            print("")
            if intentos_restantes > 0:
                print(f"Te quedan {intentos_restantes} intento.")
            else:
                print("Acceso bloqueado. Numero de intentos sobrepasados.")
                return False

def pedir_dato(campo, funcion_validadora, opcional=False):
    while True:
        valor = input(f"{campo}: ").strip()
        if opcional and valor == "":
            return ""
        if funcion_validadora(valor):
            return valor
        else:
            print(f"El campo '{campo}' no es válido. Inténtelo de nuevo.")
            print("")

def prueba_manual_usuario():
    print("")
    print("REGISTRO MANUAL DE USUARIO")
    nombre = pedir_dato("Nombre", validar_nombre)
    segundo_nombre = pedir_dato("Segundo nombre (opcional)", validar_nombre_2, opcional=True)
    apellido = pedir_dato("Apellido", validar_nombre)
    segundo_apellido = pedir_dato("Segundo apellido (opcional)", validar_nombre_2, opcional=True)
    telefono = pedir_dato("Teléfono", es_celular_valido)
    correo = pedir_dato("Correo electrónico", validar_correo_valido)
    direccion = pedir_dato("Dirección", validar_direccion_valida)
    fecha = pedir_dato("Fecha (dd/mm/aa)", validar_fecha_valida)
    contrasena = pedir_dato("Contraseña", validar_contrasena)
    exito = validar_todo(
        nombre, segundo_nombre, apellido, segundo_apellido,
        telefono, correo, direccion, fecha, contrasena,
        nombre_caso="CASO 5 Usuario ingresado manualmente"
    )
    if exito:
        print("Usuario registrado correctamente.")
    else:
        print("Fallo el registro. Esto no deberia ocurrir.")

if __name__ == "__main__":
    unittest.main(exit=False)

    prueba_manual_usuario() 
    print("")
    print("Usuarios validados (correo = contraseña):")
    if diccionario_usuarios_autorizados:
        for correo, contrasena in diccionario_usuarios_autorizados.items():
            print(f"  - {correo}: {contrasena}")
        login(diccionario_usuarios_autorizados)
    else:
        print("  No se registraron usuarios validos.")
