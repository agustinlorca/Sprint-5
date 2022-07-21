from cliente.cliente import CLASSIC, BLACK, GOLD, Cliente
from cliente.cliente_black import ClienteBlack
from cliente.cliente_gold import ClienteGold
from cliente.cliente_classic import ClienteClassic
from cliente.builderCliente import BuilderCliente
from evento import Evento
import json


class Parser:

    def execute(self,file_name:str) -> tuple[Cliente,'list[Evento]']:
        transacciones= []
        with open(file_name) as jsonFile:
            eventos = json.load(jsonFile)
            cliente = self.parsearCliente(eventos)
            for t in eventos["transacciones"]:
                transacciones.append(Evento(**t))
        return (cliente,transacciones)

    def parsearCliente(self,datos) -> Cliente:
        tipo = datos["tipo"]

        if (tipo == CLASSIC):
            cliente = ClienteClassic(**BuilderCliente.getDatosClienteClassic())
        elif (tipo == GOLD):
            cliente = ClienteGold(**BuilderCliente.getDatosClienteGold())
        elif (tipo == BLACK):
            cliente = ClienteBlack(**BuilderCliente.getDatosClienteBlack())
        else:
            raise Exception("Tipo de cliente no existe")
        
        cliente.inicializar(datos)
        
        return cliente