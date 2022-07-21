from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento

class RazonCompraDolar(Razon):
    
    def resolver(self, cliente: Cliente, evento: Evento) -> str:
        if not cliente.puede_comprar_dolar():
            return "Este tipo de cuentas no puede comprar dolares"
        if evento.monto > evento.saldoEnCuenta:
            return "No tiene saldo suficiente para comprar los dólares"

        return "No se pudo determinar la razon de compra de dólares"