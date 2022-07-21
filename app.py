from clases.buscador_problema import BuscadorProblema
from clases.parser import Parser
from clases.procesador_html import ProcesadorHtml

if __name__ == "__main__":
    parser = Parser()
    cliente, eventos = parser.execute("eventos_black.json")
    salida_html = ProcesadorHtml()
    buscador = BuscadorProblema(cliente)
    for e in eventos:
        salida_html.append(buscador.getResultado(e))

        salida_html.crear_html(cliente)
