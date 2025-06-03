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
    for i, r in enumerate(registros, start=1):
        try:
            # Conversión segura: solo convierte strings que sean dígitos completos
            datos_convertidos = {
                k: (int(v) if v is not None and v.isdigit() else v)
                for k, v in r.items()
            }
            obj = model_class(**datos_convertidos)
            session.merge(obj)
        except Exception as e:
            print(f"Error en registro {i}: {r}")
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
