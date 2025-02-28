from contextlib import contextmanager
from scr.database.connectDB import get_connection

class model_Beneficiario:
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
    def get_beneficiario(tipoBeneficiaro):
        result=None
        with model_Beneficiario.get_managed_connection() as connection:
            with connection.cursor(dictionary=True)as cursor:
                SQL_SELECT=""" SELECT AA.Codigo, AA.Nombres , AA.Beneficiario FROM 
                            (SELECT IDCLIENTE AS Codigo, NOMBRES, 'Cliente' as Beneficiario 
                            FROM Clientes
                            UNION
                            SELECT ID as Codigo, NOMBRES , 'Proveedores'AS Beneficiario 
                            FROM Proveedores)AA
                            where AA.Beneficiario=%s order by AA.Nombres
                                            """
                val=(tipoBeneficiaro,)
                cursor.execute(SQL_SELECT,val)
                result= cursor.fetchall()
        return  result