from scr.database.connectDB import get_connection


class model_Voucher:

    @staticmethod
    def get_Vouchers():

        try:
            with get_connection() as connection:

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
                            FROM voucher v
                                LEFT JOIN clientes c ON v.beneficiario = 1 AND c.IDCLIENTE = v.idbeneficiario
                                LEFT JOIN proveedores p ON v.beneficiario = 2 AND p.ID = v.idbeneficiario
                                LEFT JOIN bancos b ON b.idbco = v.idbanco
                                LEFT JOIN voucher_fpago vp ON vp.idfpago = v.idFormaPago
                            WHERE v.estado = 1
                    """
                    cursor.execute(SQL_SELECT)
                    result = cursor.fetchall()
                    print(SQL_SELECT)
                    print(result)
                    print(connection.database)
                    return result

        except Exception as err:

            print(f"Error al obtener los vouchers:{err}")
            return []
