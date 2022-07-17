from .razon import Razon
from ..cliente import Cliente
from ..evento import Evento


class RazonAltaTarjetaCredito(Razon):
    def resolver(self, cliente: Cliente, evento: Evento) -> str:
        if not cliente.puede_crear_tarjeta_credito():
            return "Al cliente no se le permite tener tarjeta de credito"

        if cliente.cuenta.total_tarjetas_credito < (evento.totalTarjetasDeCreditoActualmente + 1):
            return "Ya se tiene el cupo de tarjetas de credito disponibles"

        return "No se pudo determinar la razon de por qué no se puede dar de alta tarjeta de credito "
