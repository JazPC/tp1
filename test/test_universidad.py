import unittest
from flask import current_app
from app import create_app
from app.models import Universidad
import os

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_cart(self):
        universidad = Universidad()
        universidad.nombre = "Universidad Tecnologica Nacional"
        universidad.sigla = "UTN"
        universidad.tipo = "publica"
        universidad.anoFundacion = "1948"
        self.assertIsNotNone(universidad)
        self.assertEqual(universidad.nombre, "Universidad Tecnologica Nacional")
        self.assertEqual(universidad.sigla, "UTN")
        self.assertEqual(universidad.tipo, "publica")
        self.assertEqual(universidad.anoFundacion, "1948")

if __name__ == '__main__':
    unittest.main()