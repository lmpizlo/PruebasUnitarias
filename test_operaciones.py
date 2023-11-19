import unittest
from operaciones import restar, multiplicar, dividir

# 3 metodos, uno para cada funcion

class TestOperaciones(unittest.TestCase):
    def test_restar(self):
        # Casos generales
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(-1, 1), -2)
        # Casos con ceros
        self.assertEqual(restar(0, 0), 0)
        self.assertEqual(restar(0, 5), -5)
        self.assertEqual(restar(10, 0), 10)
        # Casos con números negativos
        self.assertEqual(restar(-3, -5), 2)
        self.assertEqual(restar(-10, -7), -3)

    def test_multiplicar(self):
        # Casos generales
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-2, 4), -8)
        # Casos con ceros
        self.assertEqual(multiplicar(0, 5), 0)
        self.assertEqual(multiplicar(10, 0), 0)
        # Casos con números negativos
        self.assertEqual(multiplicar(-3, -5), 15)
        self.assertEqual(multiplicar(-10, 7), -70)

    def test_dividir(self):
        # Casos generales
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(9, 3), 3)
        # Casos con ceros
        with self.assertRaises(ValueError):
            dividir(4, 0)
        self.assertEqual(dividir(0, 5), 0)
        # Casos con números negativos
        self.assertEqual(dividir(-6, 2), -3)
        self.assertEqual(dividir(10, -2), -5)

if __name__ == '__main__':
    unittest.main()