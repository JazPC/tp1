from models.grado import Grado
from utils.xml_utils import parse_xml_to_dicts, with_session

@with_session
def importar_grados(session, xml_path):
    registros = parse_xml_to_dicts(xml_path, record_tag='_expxml') 
    for r in registros:
        grado = Grado(
            grado=int(r['grado']),
            nombre=r['nombre']
        )
        session.merge(grado)
