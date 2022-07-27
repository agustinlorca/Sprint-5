from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento
from cliente.cuenta import Cuenta

class RazonTransferenciaEnviada(Razon):
   def resolver(self, cliente:Cliente,evento:Evento,cuenta:Cuenta) -> str:
        if not cliente.tiene_cuenta_corriente():
            if evento.monto + evento.monto * cuenta.costo_transferencias > evento.saldoEnCuenta:
                return "El saldo en su cuenta es insuficiente para realizar la transferencia"
        else:
            #Osea si tiene cuenta corriente
            if evento.monto + evento.monto * cuenta.costo_transferencias > evento.saldoEnCuenta + cuenta.saldo_descubierto_disponible:
                return "El saldo y el descubierto en su cuenta es insuficiente para realizar la transferencia"
       
       