from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento

class RazonTransferenciaRecibida(Razon):
   def resolver(self, cliente:Cliente,evento:Evento) -> str:
       if evento.monto>cliente.limite_transferencia_recibida:
           return "El monto recibido es mayor al permitido sin aviso previo"
       
       return "No se pudo determinar la causa de rechazo"