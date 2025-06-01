import unittest
from flask import current_app
from app import create_app
from app.models import Orientacion

class OrientacionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_orientacion(self):
        orientacion = Orientacion()
        orientacion.nombre = 'Sistemas'
        
          
        self.assertEqual(orientacion.nombre, 'Sistemas')
        

if __name__ == '__main__':
    unittest.main()