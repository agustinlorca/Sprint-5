from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento

class RazonRetiroEfectivo(Razon):
    
    def resolver(self, cliente: Cliente, evento: Evento) -> str:
        if evento.monto > evento.saldoEnCuenta:
            return "No posee fondos suficientes para la extracción"

        return "No se pudo determinar la razon de retiro de efectivo"