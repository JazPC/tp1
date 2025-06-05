import unittest
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from utils.xml_importer import import_data
from models import Localidad

class TestImportLocalidades(unittest.TestCase):
    def setUp(self):
        
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

        self.temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="Windows-1252")
        self.temp.write("""
        <root>
            <_expxml>
                <codigo>1</codigo>
                <ciudad>Ciudad Autónoma de Buenos Aires</ciudad>
                <provincia>Capital Federal</provincia>
                <pais_del_c>Argentina</pais_del_c>
            </_expxml>
        </root>
        """)
        self.temp.close()

    def tearDown(self):
        try:
            os.remove(self.temp.name)
        except Exception:
            pass

    def test_importar_Localidades(self):
        session = self.Session()
        import_data(session, self.temp.name, Localidad, record_tag="_expxml")
        session.commit()

        resultados = session.query(Localidad).order_by(Localidad.codigo).all()
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].codigo, 1)
        self.assertEqual(resultados[0].ciudad, "Ciudad Autónoma de Buenos Aires")
        self.assertEqual(resultados[0].provincia, "Capital Federal")
        self.assertEqual(resultados[0].pais_del_c, "Argentina")

        session.close()

if __name__ == '__main__':
    unittest.main()
      