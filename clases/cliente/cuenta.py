
"""kwargs = {
    'limite_extraccion_diario':[10000,20000,100000],
    'limite_transferencia_recibida':[150000,500000,None],
    'costo_transferencia':[0.01,0.005,None],
    'total_tarjetas_credito':[0,1,5],
    'total_chequeras':[0,1,2],
    'saldo_descubierto_disponible':[0,10000,10000]
}
class Cuenta:
    def __init__(self, **kwargs) -> None:
        self.limite_extraccion_diario = kwargs.get('limite_extraccion_diario',[2])
        self.limite_transferencia_recibida = kwargs.get('limite_transferencia_recibida',[2])
        self.costo_transferencia = kwargs.get('costo_transferencia',[2])
        self.total_tarjetas_credito = kwargs.get('total_tarjetas_credito',[2])
        self.total_chequeras = kwargs.get('total_chequeras',[2])
        self.saldo_descubierto_disponible= kwargs.get('saldo_descubierto_disponible',[2])"""

class Cuenta(object):
    def __init__(self,  limite_extraccion_diario, limite_transferencia_recibida,   costo_transferencias,  saldo_descubierto_disponible,   total_tarjetas_credito,   total_chequeras):
        self.limite_extraccion_diario = limite_extraccion_diario
        self.limite_transferencia_recibida = limite_transferencia_recibida
        self.costo_transferencias = costo_transferencias
        self.saldo_descubierto_disponible =saldo_descubierto_disponible
        self.total_tarjetas_credito =total_tarjetas_credito
        self.total_chequeras =total_chequeras
        

