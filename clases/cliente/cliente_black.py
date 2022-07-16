from .cliente import Cliente

class ClienteBlack(Cliente):
    def __init__(self,**kwargs) -> None:
        super(ClienteBlack,self).__init__(**kwargs)

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