from abc import ABC, abstractmethod
from clases.cliente.cliente import Cliente
from clases.evento import Evento

class Razon(ABC):
    @abstractmethod
    def resolver(self, cliente: Cliente, evento: Evento) -> str:
        pass