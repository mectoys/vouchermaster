from scr.database.connectDB import get_connection
import mysql.connector


@staticmethod
def get_Vouchers():
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            SQL_SELECT = """
                SELECT v.idVoucher, 
                       DATE_FORMAT(v.fecha, '%d/%m/%Y') AS fecha,
                       COALESCE(c.NOMBRES, p.NOMBRES) AS Nombres,
                       b.descripcion AS Banco, 
                       v.moneda, 
                       vp.descripcion AS FormaPago, 
                       v.cuenta,   
                       CONCAT(v.moneda, ' ', (v.importePago + v.interes + v.comision)) AS Total, 
                       v.nota,
                       CASE WHEN v.filename IS NULL THEN 0 ELSE 1 END AS hasfilename
                FROM Voucher v
                LEFT JOIN Clientes c ON v.beneficiario = 1 AND c.IDCLIENTE = v.idbeneficiario
                LEFT JOIN Proveedores p ON v.beneficiario = 2 AND p.ID = v.idbeneficiario
                LEFT JOIN Bancos b ON b.idbco = v.idbanco
                LEFT JOIN Voucher_fpago vp ON vp.idfpago = v.idFormaPago
                WHERE v.estado = 1
            """
            cursor.execute(SQL_SELECT)
            result = cursor.fetchall()
            print(result)
            print('asd')
    except mysql.connector.Error as err:
        # Manejar errores específicos de la consulta SQL
        print(f"Error: {err}")
        result = []
    finally:
        connection.close()

    return result