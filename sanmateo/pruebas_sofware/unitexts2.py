import re
import unittest

def validar_correo(correo: str) -> bool:
    patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(patron, correo) is not None

def validar_telefono(numero: str) -> bool:
    patron = r"^\d{7,10}$"
    return re.match(patron, numero) is not None

class TestValidaciones(unittest.TestCase):

    def test_correo_valido(self):
        self.assertTrue(validar_correo(input("ingresar correo  valido ")))

    def test_correo_invalido(self):
        self.assertFalse(validar_correo("correo@dominio"))

    def test_telefono_valido(self):
        self.assertTrue(validar_telefono("3123456789"))

    def test_telefono_invalido_corto(self):
        self.assertFalse(validar_telefono("12345"))

    def test_telefono_invalido_letras(self):
        self.assertFalse(validar_telefono("abc1234567"))

    def test_telefono_invalido_largo(self):
        self.assertFalse(validar_telefono("12345678901"))

if __name__ == '__main__':
    unittest.main()
""" 

"""