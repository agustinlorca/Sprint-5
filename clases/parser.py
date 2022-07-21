import json
from cliente.cliente import Cliente


class Parser:

    def execute(self,file_name:str) -> Tuple[Cliente,'list[Evento]']:
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
            cliente = ClienteCLassic(**BuilderCliente.getDatosClienteClassic())
        elif (tipo == GOLD):
            cliente = ClienteGold(**BuilderCliente.getDatosClienteGold())