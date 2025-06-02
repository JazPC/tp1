import unittest
from flask import current_app
from config import create_app
from app.models import Departamento

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_departamento(self):
        departamento = Departamento()
        departamento.nombre = 'Ingenieria'
          
        self.assertEqual(departamento.nombre, 'Ingenieria')


if __name__ == '__main__':
    unittest.main()