from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento

class RazonTransferenciaEnviada(Razon):
   def resolver(self, cliente:Cliente,evento:Evento) -> str:
       if evento.monto>evento.saldoEnCuenta:
           return "El monto a enviar es menor al saldo en cuenta disponible"
       
       return "No se pudo determinar la causa de rechazo"