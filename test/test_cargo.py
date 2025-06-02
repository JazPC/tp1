import unittest
from flask import current_app
from config import create_app
from app.models import Cargo

class CargoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_cargo(self):
        cargo = Cargo()
        cargo.nombre = 'Decano'
        cargo.puntos = 2

        self.assertIsNotNone(cargo)
        self.assertEqual(cargo.nombre, 'Decano')
        self.assertEqual(cargo.puntos, 2)

if __name__ == '__main__':
    unittest.main()

