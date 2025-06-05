import unittest
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from utils.xml_importer import import_data
from models import Plan

class TestImportPlan(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        
        self.temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="Windows-1252")
        self.temp.write("""
        <root>
            <_expxml>
                <especialidad>274</especialidad>
		        <plan>2009</plan>
		        <nombre/>
            </_expxml>
        </root>
        """)
        self.temp.close() 

    def tearDown(self):
        try:
            os.remove(self.temp.name)
        except Exception:
            pass

    def test_importar_Plans(self):
        session = self.Session()
        import_data(session, self.temp.name, Plan, record_tag="_expxml")
        session.commit()

        resultados = session.query(Plan).order_by(Plan.plan).all()
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].especialidad, 274)
        self.assertEqual(resultados[0].plan, 2009)
        self.assertEqual(resultados[0].nombre, None)

        session.close()

if __name__ == '__main__':
    unittest.main()

