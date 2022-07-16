
from .cliente import Cliente
from ..evento import Evento

class ClienteClassic(Cliente):
    def __init__(self,**kwargs) -> None:
        super(ClienteClassic,self).__init__(**kwargs)
    
    def get_razon_compra_visa(self, evento:Evento):
        return "Este cliente no puede tener tarjetas de crédito"