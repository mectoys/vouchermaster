class Voucher:
    def __init__(self, fecha, beneficiario, idbeneficiario, idbanco, moneda, idFormaPago, cuenta, importePago, interes,
                 comision, nota, idVoucher = None):
        self.fecha = fecha
        self.beneficiario = beneficiario
        self.idbeneficiario = int(idbeneficiario)
        self.idbanco = int(idbanco)
        self.moneda = moneda
        self.idFormaPago = int(idFormaPago)
        self.cuenta = cuenta
        self.importePago = float(importePago)
        self.interes = float(interes)
        self.comision = float(comision)
        self.nota=nota
        self.idVoucher = int(idVoucher)
