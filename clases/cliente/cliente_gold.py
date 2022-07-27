from .cliente import Cliente

class ClienteGold(Cliente):
    def __init__(self):
        self.limite_extraccion_diario = 20000
        self.limite_transferencia_recibida = 500000
        self.costo_transferencias =0.005
        self.saldo_descubierto_disponible =0
        self.total_tarjetas_credito =1
        self.total_chequeras =1
    

    #def __init__(self,**kwargs) -> None:
     #   super(ClienteGold,self).__init__(**kwargs)
    
    def puede_crear_chequera(self) -> bool:
        return True
    
    def puede_crear_tarjeta_credito(self) -> bool:
        return True

    def puede_comprar_dolar(self) -> bool:
        return True

    