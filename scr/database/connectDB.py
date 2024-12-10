import os.path
import logging
from dotenv import load_dotenv
from mysql.connector.pooling import MySQLConnectionPool, Error

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s- %(levelname)s-%(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

script_dir = os.path.dirname(__file__)

dotenv_path = os.path.join(script_dir, '..', '..', 'parameters.env')

load_dotenv(dotenv_path)

if not all([os.getenv("MY_SQL_HOST"), os.getenv("MY_SQL_USER"), os.getenv("MY_SQL_PASSWORD"),
            os.getenv("MY_SQL_DATABASE")]):
    logger.critical("Flata variables de entorno necesarias para la conexión a la base de datos.")

    raise Exception("Falta variables de entorno necesarias.")
#Configurar el pool de conexiones
try:
    connection_pool = MySQLConnectionPool(
        pool_name="mypoolname",
        pool_size=5,
        pool_reset_session=True,
        host=os.getenv("MY_SQL_HOST"),
        user=os.getenv("MY_SQL_USER"),
        password=os.getenv("MY_SQL_PASSWORD"),
        database=os.getenv("MY_SQL_DATABASE")
    )
    logger.info("Pool de conexiones configurador correctamente.")
except Error as err:
    logger.critical(f"Error al configurar el pool de conexión: {err}")


#Funcion para obtener una conexión del pool
def get_connection():
    try:
        # Intenta obtener una conexión pool.
        logger.info("Intentando obtener una conexión del pool.")
        return connection_pool.get_connection()
    except  Error as err:
        #Maneja posibles errores al obtener la conexión.
        if err.errno == 1045:  # Error de autentificación
            logger.error("Error de autentificación con la base de datos.")
        elif err.errno == 2003:  #Error al conectarse al servidor MYSQL
            logger.error("no se puede conectar a la base de datos.")
        else:
            #Cualquier otro error se registra en el log.
            logger.error(f"Error desconocido: {err}")
        #Lanza de nueco el error para manejarlo en otro lugar si es necesario
        raise err
