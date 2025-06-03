import unittest
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from utils.xml_importer import import_data
from models import Materia

class TestImportMaterias(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        
        # Crear archivo temporal
        self.temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="Windows-1252")
        self.temp.write("""
        <root>
            <_expxml>
                <especialidad>1</especialidad>
                <plan>1</plan>
                <materia>1</materia>
                <nombre>Matemáticas</nombre>
                <ano>1</ano>
            </_expxml>
            <_expxml>
                <especialidad>2</especialidad>
                <plan>2</plan>
                <materia>2</materia>
                <nombre>Lengua</nombre>
                <ano>2</ano>
            </_expxml>
        </root>
        """)
        self.temp.close() 

    def tearDown(self):
        try:
            os.remove(self.temp.name)
        except Exception:
            pass

    def test_importar_materias(self):
        session = self.Session()
        import_data(session, self.temp.name, Materia, record_tag="_expxml")
        session.commit()

        resultados = session.query(Materia).order_by(Materia.especialidad).all()
        self.assertEqual(len(resultados), 2)
        self.assertEqual(resultados[0].especialidad, 1)
        self.assertEqual(resultados[0].nombre, "Matemáticas")
        self.assertEqual(resultados[1].especialidad, 2)
        self.assertEqual(resultados[1].nombre, "Lengua")

        session.close()

if __name__ == '__main__':
    unittest.main()
