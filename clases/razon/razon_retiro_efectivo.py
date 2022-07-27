from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento
from cliente.cuenta import Cuenta

class RazonRetiroEfectivo(Razon):
    
    def resolver(self, cliente: Cliente, evento: Evento,cuenta:Cuenta) -> str: 
        if not cliente.tiene_cuenta_corriente():
            if evento.monto > cuenta.limite_extraccion_diario:
                return "La extracción supera el monto de extracción diario"
            if evento.monto > evento.saldoEnCuenta:
                return "El saldo es insufiente para realizar la extracción"
        else:
            #Osea si tiene cuenta corriente
            if evento.monto > cuenta.limite_extraccion_diario:
                return "La extracción supera el monto de extracción diario"
            if evento.monto > evento.saldoEnCuenta:
                return "El saldo es insufiente para realizar la extracción"