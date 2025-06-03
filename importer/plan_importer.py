from models.plan import Plan
from utils.xml_importer import import_data, with_session

@with_session
def importar_planes(session, xml_path):
    import_data(session, xml_path, Plan, record_tag='_expxml')
