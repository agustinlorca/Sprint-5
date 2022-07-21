from evento import Evento
from .razon.razon_alta_chequera import RazonAltaChequera
from .razon.razon_alta_tarjeta_credito import RazonAltaTarjetaCredito
from .razon.razon_transferencia_enviada import RazonTransferenciaEnviada
from .razon.razon_transferencia_recibida import RazonTransferenciaRecibida
from .razon.razon_compra_dolar import RazonCompraDolar
from .razon.razon_retiro_efectivo import RazonRetiroEfectivo


def BuscadorProblema(t,evento):
    if t.estado == "RECHAZADA":
        match t.tipo.lower():
            case 'transferencia_enviada':
                return RazonTransferenciaEnviada(t, evento).resolver() 
            case 'transferencia_recibida':
                return RazonTransferenciaRecibida(t, evento).resolver()
            case 'alta_tarjeta_credito':
                return RazonAltaTarjetaCredito(t, evento).resolver()
            case 'alta_chequera':
                return RazonAltaChequera(t, evento).resolver()
            case 'compra_dolar':
                return RazonCompraDolar(t, evento).resolver()
            case'retiro_efectivo_cajero_automatico':
                return RazonRetiroEfectivo(t, evento).resolver()