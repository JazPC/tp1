# utils/xml_importer.py

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
    for r in registros:
        obj = model_class(**{k: (int(v) if v.isdigit() else v) for k,v in r.items()})
        session.merge(obj)

def with_session(func):
    def wrapper(*args, **kwargs):
        session = Session()
        try:
            result = func(session, *args, **kwargs)
            session.commit()
            return result
        except:
            session.rollback()
            raise
        finally:
            session.close()
    return wrapper
