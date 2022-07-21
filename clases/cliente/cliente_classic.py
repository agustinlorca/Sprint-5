from .cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self,**kwargs) -> None:
        super(ClienteClassic,self).__init__(**kwargs)

    def puede_crear_chequera(self) -> bool:
        return False
    
    def puede_crear_tarjeta_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False
    
    def tiene_cuenta_corriente(self) -> bool:
        return True
    
    def necesita_autorizar_transferencia_recibida(self) -> bool:
        return True