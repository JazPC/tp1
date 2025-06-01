#borren comentarios puros, comentarios de codigo a modificar
import unittest
import os
from flask import current_app
from app import create_app, db
from app.models import Materia
#from app.models import Autoridad 
#from app.models import Categoria

class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_materia_creation(self):
        materia = Materia()
        materia.nombre = 'Algebra y geometria'
        materia.diseno_curricular = 'diseno curricular'
        materia.correlativas = []   
        materia.horas_dictadas = '36'   
        materia.promocional = True  
        materia.nivel = '1' 
          
        self.assertEqual(materia.nombre, 'Algebra y geometria')
        self.assertEqual(materia.diseno_curricular, 'diseno curricular')
        self.assertEqual(materia.correlativas, [])
        self.assertEqual(materia.horas_dictadas, '36')
        self.assertEqual(materia.promocional, True)
        self.assertEqual(materia.nivel, '1')


    def __nuevaMateria(self):
        materia = Materia()
        materia.nombre = 'Algebra y geometria'
        materia.codigo = 'diseno curricular'
        materia.observacion = ""  
        materia.asociar_autoridad(self.__nuevaAutoridad()) #agrega muchas materias porque es muchos a muchos  
        materia.orientacion = self.__nuevaOrientacion()
        return materia
    
    def __nuevaOrientacion(self):
        orientacion = Orientacion()
        orientacion.nombre = 'Matematica'
        return orientacion
    
    def test_crear_materia(self):
        materia = self.__nuevaMateria()
        db.session.add(materia)
        db.session.commit()
        self._assert_materia(materia, 'Mate', 'mt01', 'mat basica') #el chico hizo una funcion assert
    
    def __nuevaAutoridad(self):
        autoridad = Autoridad()
        autoridad.nombre = 'Juan Perez'
        autoridad.telefono = 'Docente'
        autoridad.email = 'du'
        autoridad.cargo = self.__nuevoCargo
        return autoridad
    
    def __nuevoCargo(self):
        cargo = Cargo()
        cargo.nombre = 'Profesor'
        cargo.categoria_cargo = self.__categoriaCargo()
        cargo.tipo_dedicacion = self.__tipoDedicacion()
        return cargo
    
    def __tipoDeCargo(self):
        tipo_cargo = TipoDedicacion()
        tipo_cargo.nombre = 'Tiempo completo'
        
        return tipo_cargo
    
if __name__ == '__main__':
    unittest.main()