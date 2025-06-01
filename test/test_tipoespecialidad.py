import unittest
from flask import current_app
from app import create_app
from app.models import TipoEspecialidad

class TipoEspecialidadTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_cart(self):
        tipoespecialidad = TipoEspecialidad()
        tipoespecialidad.nombre = 'Nombre del tipo de especialdad'
        tipoespecialidad.nivel = 'Nivel del Tipo de especialidad'
        
        self.assertEqual(tipoespecialidad.nombre, 'Nombre del tipo de especialdad')
        self.assertEqual(tipoespecialidad.nivel, 'Nivel del Tipo de especialidad')
         
       