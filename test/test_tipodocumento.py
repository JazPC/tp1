
import unittest
from flask import current_app
from config import create_app
from app.models import TipoDocumento

class TipoDocumentoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_tipodocumento(self):
        tipo_documento = TipoDocumento()
        tipo_documento.libretacivica = 'Libreta Civica'
        tipo_documento.libretaenrolamiento = 'Libreta de Enrolamiento'
        tipo_documento.pasaporte = 'Pasaporte'
 
        self.assertEqual(tipo_documento.libretacivica, 'Libreta Civica')
        self.assertEqual(tipo_documento.libretaenrolamiento, 'Libreta de Enrolamiento')
        self.assertEqual(tipo_documento.pasaporte, 'Pasaporte')
        

if __name__ == '__main__':
    unittest.main()