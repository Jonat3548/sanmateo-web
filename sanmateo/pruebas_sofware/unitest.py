import unittest  

# Función 
def suma(a, b):
    return a + b

# Clase de prueba 
class TestSuma(unittest.TestCase):

    # Método de prueba
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)  # Verifica que 2 + 3 = 5

    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -1), -2)

    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
