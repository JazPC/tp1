import unittest
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from utils.xml_importer import import_data
from models import Orientacion

class TestImportOrientacion(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        
        # Crear archivo temporal
        self.temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="Windows-1252")
        self.temp.write("""
        <root>
            <_expxml>
                <especialidad>800</especialidad>
		        <plan>2019</plan>
		        <orientacion>0</orientacion>
		        <nombre>Actividades Académicas de Posgrado</nombre>
            </_expxml>
        </root>
        """)
        self.temp.close() 

    def tearDown(self):
        try:
            os.remove(self.temp.name)
        except Exception:
            pass

    def test_importar_Orientacions(self):
        session = self.Session()
        import_data(session, self.temp.name, Orientacion, record_tag="_expxml")
        session.commit()

        resultados = session.query(Orientacion).order_by(Orientacion.especialidad).all()
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].especialidad, 800)
        self.assertEqual(resultados[0].plan, 2019)
        self.assertEqual(resultados[0].orientacion, 0)
        self.assertEqual(resultados[0].nombre, "Actividades Académicas de Posgrado")

        session.close()

if __name__ == '__main__':
    unittest.main()
