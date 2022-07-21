from .cuenta import Cuenta
from .direccion import Direccion

BLACK = "BLACK"
GOLD = "GOLD"
CLASSIC ="CLASSIC"

class Cliente:
    def __init__(self, **kwargs) -> None:
        self.cuenta = Cuenta(**kwargs)
    
    def inicializar(self, datos):
        self.numero = datos["numero"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.dni = datos["dni"]
        self.direccion = Direccion(**datos["direccion"])

    def puede_crear_chequera(self) -> bool:
        return False
    def puede_crear_tarjeta_credito(self) -> bool:
        return False
    def puede_comprar_dolar(self) -> bool:
        return False
    def get_costo_transferencia(self,monto: int) -> int:
        return monto * self.cuenta.costo_transferencia
    
    def tiene_cuenta_corriente(self) -> bool:
        return False
    def necesita_autorizar_transferencia_recibida(self) -> bool:
        return True
