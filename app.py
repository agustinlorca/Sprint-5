from clases import Parser, BuscadorProblema, ProcesadorHtml

if __name__ == "__main__":
    parser = Parser()
    cliente, eventos = parser.execute("eventos.json")
    salida_html = ProcesadorHtml()
    buscador = BuscadorProblema(cliente)
    for e in eventos:
        salida_html.append(buscador.getResultado(e))

        salida_html.crear_html(cliente)
