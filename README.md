Proyecto SYSACAD – Importador de Datos XML
Este proyecto tiene como objetivo importar datos desde archivos XML del sistema heredado y almacenarlos en la base de datos DEV_SYSACAD.
 Funcionalidades
Importación de los siguientes archivos XML:


grados.xml
universidad.xml
facultades.xml
materias.xml
localidades.xml
especialidades.xml
orientaciones.xml
planes.xml
paises.xml


Conversión de los datos XML a objetos Python.


Persistencia de registros en la base de datos DEV_SYSACAD mediante SQLAlchemy.


Validación de identificadores únicos utilizando session.merge().


Codificación soportada: Windows-1252.


Requisitos
Python 3.10 o superior


Base de datos compatible (PostgreSQL)


Archivos XML con codificación Windows-1252
 Instrucciones de instalación y ejecución
1_Clonar el repositorio
git clone https://github.com/JazPC/tp1_importacion_de_xml.git

2_(Opcional) Crear un entorno virtual
python -m venv venv
source venv/Scripts/activate  # En Windows: venv\Scripts\activate

3_Instalar los requerimientos
pip install -r requirements.txt

4_Configurar las variables de entorno en archivo .env:
DB_USER=tu_user
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5443
DB_NAME=DEV_SYSACAD

5_Ejecutar la aplicación
python main.py
Pruebas automáticas (TDD)

Para correr las pruebas desarrolladas siguiendo TDD:
python -m unittest discover

Autores
Jazmín Pérez Castro
Celeste Choquevillca
