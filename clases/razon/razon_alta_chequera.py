from .razon import Razon
from ..cliente import Cliente
from ..evento import Evento

class RazonAltaChequera(Razon):
    def resolver (self, cliente: Cliente, evento: Evento) -> str:
        if not cliente.puede_crear_chequera():
            return "Al cliente no se le permite tener chequeras"

        if cliente.cuenta.total_chequeras < (evento.totalChequerasActualmente +1):
            return "Ya se tiene el cupo de chequeras disponibles"
        
        return "No se pudo determinar la razon de por qué no se creó la chequera"
