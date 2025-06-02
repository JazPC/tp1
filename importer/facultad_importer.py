from models.facultad import Facultad
from utils.xml_utils import parse_xml_to_dicts, with_session

@with_session
def importar_facultades(session, xml_path):
    registros = parse_xml_to_dicts(xml_path ,record_tag='_expxml')
    for r in registros:
        facultad = Facultad(
            facultad=int(r['facultad']),
            nombre=r['nombre']
        )
        session.merge(facultad)
