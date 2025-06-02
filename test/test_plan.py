import unittest
from flask import current_app
from config import create_app
from app.models import Plan

class PlanTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_plan(self):
        plan = Plan()
        plan.nombre = 'Sistemas'
        plan.fechaInicio = '12 de noviembre 2024'
        plan.fechaFin = '12 de diciembre 2024'
        plan.observacion = 'Se dicta solo un mes'

        self.assertIsNotNone(plan)
        self.assertEqual(plan.nombre, 'Sistemas')
        self.assertEqual(plan.fechaInicio, '12 de noviembre 2024')
        self.assertEqual(plan.fechaFin, '12 de diciembre 2024')
        self.assertEqual(plan.observacion, 'Se dicta solo un mes')

if __name__ == '__main__':
    unittest.main()

