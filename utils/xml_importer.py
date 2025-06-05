from db import Session
import xml.etree.ElementTree as ET

def parse_xml_to_dicts(xml_path, record_tag, encoding="Windows-1252"):
    tree = ET.parse(xml_path, parser=ET.XMLParser(encoding=encoding))
    root = tree.getroot()
    records = []
    for elem in root.findall(record_tag):
        record = {child.tag: child.text for child in elem}
        records.append(record)
    return records

def import_data(session, xml_path, model_class, record_tag):
    registros = parse_xml_to_dicts(xml_path, record_tag)
    for i, diccionario_registro in enumerate(registros, start=1):
        try:
            datos_convertidos = {
                clave: (int(valor) if valor is not None and valor.isdigit() else valor)
                for clave, valor in diccionario_registro.items()
            }
            obj = model_class(**datos_convertidos)
            session.merge(obj)
        except Exception as e:
            print(f"Error en registro {i}: {diccionario_registro}")
            print(f"Detalle del error: {e}")

def with_session(func):
    def wrapper(*args, **kwargs):
        session = Session()
        try:
            result = func(session, *args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            print(f"Error en la sesión: {e}")
            raise
        finally:
            session.close()
    return wrapper


