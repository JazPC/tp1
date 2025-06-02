import unittest
from flask import current_app
from config import create_app
from app.models import Alumno
import os

class AlumnoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_alumno(self):
        alumno = Alumno()
        alumno.nombre = "Nombre"
        alumno.apellido = "Apellido"
        alumno.nroDocumento = "12345678"
        alumno.tipoDocumento = "DNI"
        alumno.fechaNacimiento = "aaaa-mm-dd"
        alumno.sexo = "m=Masculino , f=Femenino"
        alumno.nroLegajo = 10066
        alumno.fechaIngreso = "aaaa-mm-dd"
        alumno.carrera = "Ingenieria en Sistemas"

        self.assertIsNotNone(alumno)
        self.assertEqual(alumno.nombre, "Nombre")
        self.assertEqual(alumno.apellido, "Apellido")
        self.assertEqual(alumno.nroDocumento, "12345678")
        self.assertEqual(alumno.tipoDocumento, "DNI")   
        self.assertEqual(alumno.fechaNacimiento, "aaaa-mm-dd")
        self.assertEqual(alumno.sexo, "m=Masculino , f=Femenino")
        self.assertEqual(alumno.nroLegajo, 10066)
        self.assertEqual(alumno.fechaIngreso, "aaaa-mm-dd")
        self.assertEqual(alumno.carrera, "Ingenieria en Sistemas")

if __name__ == '__main__':
    unittest.main()
    