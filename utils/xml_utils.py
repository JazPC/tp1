import xml.etree.ElementTree as ET
from db import Session

def parse_xml_to_dicts(xml_path, encoding="Windows-1252", record_tag=None):
    tree = ET.parse(xml_path, parser=ET.XMLParser(encoding=encoding))
    root = tree.getroot()

    records = []
    for item in root.findall(record_tag):
        record = {child.tag: child.text for child in item}
        records.append(record)

    return records

def with_session(func):
    def wrapper(*args, **kwargs):
        session = Session()
        try:
            result = func(session, *args, **kwargs)
            session.commit()
            return result
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    return wrapper
