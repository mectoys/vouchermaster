from contextlib import  contextmanager
from scr.database.connectDB import get_connection

class model_bank:

    @staticmethod
    @contextmanager
    def get_managed_connection():
        connection =get_connection()
        try:
            yield  connection
        finally:
            if connection:
                connection.close()

    @staticmethod
    def get_bank():
        result= None
        with model_bank.get_managed_connection() as  connection:
            with connection.cursor(dictionary=True)as cursor:
                SQL_SELECT ="SELECT idbco, descripcion FROM Bancos"
                cursor.execute(SQL_SELECT)
                result= cursor.fetchall()
        return  result


