from contextlib import contextmanager
from scr.database.connectDB import get_connection

class model_fpago:
    @staticmethod
    @contextmanager
    def get_managed_connection():
        connection= get_connection()
        try:
            yield connection
        finally:
            if connection:
                connection.close()


    @staticmethod
    def get_fpago():
        result=None
        with model_fpago.get_managed_connection() as connection:
            with connection.cursor(dictionary=True)as cursor:
                SQL_SELECT="SELECT idfpago, descripcion FROM Voucher_fpago"
                cursor.execute(SQL_SELECT)
                result= cursor.fetchall()
        return  result