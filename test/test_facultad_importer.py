import pytest
from unittest.mock import patch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.facultad import Facultad
from importer.facultad_importer import importar_facultades

@pytest.fixture(scope="function")
def test_session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session

def test_importa_datos_desde_xml(tmp_path, test_session):
    xml_content = """<?xml version="1.0" encoding="Windows-1252"?>
    <VFPData>
        <_expxml>
            <facultad>1</facultad>
            <nombre>Facultad Regional Avellaneda</nombre>
        </_expxml>
        <_expxml>
            <facultad>2</facultad>
            <nombre>Facultad Regional Bahía Blanca</nombre>
        </_expxml>
    </VFPData>
    """
    xml_file = tmp_path / "facultades.xml"
    xml_file.write_text(xml_content, encoding="Windows-1252")

    # Patch para que el decorador use la sesión de prueba
    with patch('importer.facultad_importer.Session', test_session):
        importar_facultades(str(xml_file))

    # Verificamos con la sesión de prueba
    session = test_session()
    resultados = session.query(Facultad).order_by(Facultad.facultad).all()
    session.close()

    assert len(resultados) == 2
    assert resultados[0].facultad == 1
    assert resultados[0].nombre == "Facultad Regional Avellaneda"
    assert resultados[1].facultad == 2
    assert resultados[1].nombre == "Facultad Regional Bahía Blanca"
