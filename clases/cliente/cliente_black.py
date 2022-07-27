from .cliente import Cliente

class ClienteBlack(Cliente):
    def __init__(self):
        self.limite_extraccion_diario = 100000
        self.limite_transferencia_recibida = None
        self.costo_transferencias =None
        self.saldo_descubierto_disponible =5
        self.total_tarjetas_credito =2
        self.total_chequeras =10000
    

    def puede_crear_chequera(self) -> bool:
        return True
    
    def puede_crear_tarjeta_credito(self) -> bool:
        return True

    def puede_comprar_dolar(self) -> bool:
        return True
    
    def tiene_cuenta_corriente(self) -> bool:
        return True
    
    def necesita_autorizar_transferencia_recibida(self) -> bool:
        return False