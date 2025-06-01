import unittest
from flask import current_app
from app import create_app
from app.models import Especialidad

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_cart(self):
        especialidad = Especialidad()
        especialidad.nombre = 'Nombre de especialdad'
        especialidad.letra = 'Letra de la especialidad'
        especialidad.observacion = 'Observacion de la especialidad' 
        
        
        self.assertEqual(especialidad.nombre, 'Nombre de especialdad')
        self.assertEqual(especialidad.letra, 'Letra de la especialidad')
        self.assertEqual(especialidad.observacion, 'Observacion de la especialidad')
       