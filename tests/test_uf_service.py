import unittest
from services.uf_service import UFService
from datetime import date

class TestUFService(unittest.TestCase):
    def test_get_uf_value(self):
        uf_service = UFService()

        # Reemplaza con una fecha y valor de UF válidos para la prueba
        test_date = date(2023, 3, 1)
        expected_uf_value = 35519.79

        uf_value = uf_service.get_uf_value(test_date)
        self.assertEqual(uf_value, expected_uf_value)

    def test_parse_uf_minimum_date(self):
        uf_service = UFService()

        test_date = date(1991, 3, 1)
        # Definimos una fecha anterior a la fecha mínima permitida
        uf_value = uf_service.get_uf_value(test_date)
        self.assertEqual(uf_value, None)

if __name__ == '__main__':
    unittest.main()