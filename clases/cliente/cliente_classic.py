from .cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self):
        self.limite_extraccion_diario = 10000
        self.limite_transferencia_recibida = 150000
        self.costo_transferencias =0.01
        self.saldo_descubierto_disponible =0
        self.total_tarjetas_credito =0
        self.total_chequeras =0
    
    def puede_crear_chequera(self) -> bool:
        return False
    
    def puede_crear_tarjeta_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False
    
    def tiene_cuenta_corriente(self) -> bool:
        return True
    
    