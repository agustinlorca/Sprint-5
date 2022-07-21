
class Evento():
    def __init__(self, evento):
        self.estado = evento['estado']
        self.tipo = evento['tipo']
        self.cuentaNumero = evento['cuentaNumero']
        self.cupoDiarioRestante = evento['cupoDiarioRestante']
        self.cantidadExtraccionesHechas = evento['cantidadExtraccionesHechas']
        self.monto = evento['monto']
        self.fecha = evento['fecha']
        self.numero= evento['numero']
        self.saldoEnCuenta = evento['saldoEnCuenta']
        self.totalTarjetasDeCreditoActualmente = evento['totalTarjetasDeCreditoActualmente']
        self.totalChequerasActualmente = evento['totalChequerasActualmente']
