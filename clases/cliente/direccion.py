import string

class Direccion:
    calle=string
    ciudad=string
    provincia=string
    pais=string
    def __init__(self,data):
        self.calle=data['calle']
        self.numero=data['numero']
        self.ciudad=data['ciudad']
        self.provincia=data['provincia']
        self.pais=data['pais']
    def __str__(self):
        return f"{self.calle} {self.numero}, {self.ciudad}, {self.provincia}, {self.pais}"
