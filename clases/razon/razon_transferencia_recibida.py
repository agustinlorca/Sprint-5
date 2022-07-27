from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento
from cliente.cuenta import Cuenta

class RazonTransferenciaRecibida(Razon):
   def resolver(self, cliente:Cliente,evento:Evento,cuenta:Cuenta) -> str:
       if cliente.necesita_autorizar_transferencia_recibida():
            if evento.monto>cuenta.limite_transferencia_recibida:
                return "El monto recibido es mayor al permitido sin aviso previo"
       
       return "No se pudo determinar la causa de rechazo"