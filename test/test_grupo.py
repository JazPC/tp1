import unittest
from flask import current_app
from config import create_app
from app.models import Grupo

class GrupoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_cart(self):
        grupo = Grupo()
        grupo.nombre = 'Nombre del grupo'
        
        self.assertEqual(grupo.nombre, 'Nombre del grupo')
      