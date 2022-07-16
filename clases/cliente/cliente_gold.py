from .cliente import Cliente

class ClienteGold(Cliente):
    def __init__(self,**kwargs) -> None:
        super(ClienteGold,self).__init__(**kwargs)
    
    def puede_crear_chequera(self) -> bool:
        return True
    
    def puede_crear_tarjeta_credito(self) -> bool:
        return True

    def puede_comprar_dolar(self) -> bool:
        return True