from typing import Any

def agrupar_salidas(*salidas: Any) -> None:
    """
    Agrupa múltiples salidas (textos o expresiones de Cadabra) en un único bloque
    visual dentro de una celda de Jupyter.
    
    Esta función intercepta el renderizado LaTeX nativo de las expresiones de Cadabra
    y concatena sus representaciones Markdown en un único bloque, enviándolo directamente
    al frontend de Jupyter a través del servidor interno de cadabra2.
    
    Args:
        *salidas: Uno o más objetos a mostrar. Pueden ser objetos `cadabra2.Ex`, cadenas de
                 texto, o cualquier objeto que se desee mostrar. Las expresiones de Cadabra
                 se renderizarán matemáticamente con delimitadores LaTeX.
                 
    Ejemplo:
        agrupar_salidas(
            "Primer término:",
            ex1,
            "Segundo término:",
            ex2
        )
    """
    # Intentamos importar server desde el contexto de Jupyter Cadabra
    try:
        from __main__ import server
    except ImportError:
        # Si no estamos en el entorno Jupyter de Cadabra, simplemente imprimimos
        print("Advertencia: `agrupar_salidas` está diseñado para funcionar dentro de cuadernos Jupyter de Cadabra.")
        for s in salidas:
            print(s)
        return

    latex_strs = []
    
    for e in salidas:
        if hasattr(e, '_latex_'):
            # Es una expresión de Cadabra, la envolvemos en notación matemática
            latex_strs.append(f"${e._latex_()}$")
        elif isinstance(e, str):
            # Es texto normal
            latex_strs.append(e)
        else:
            # Otro objeto, lo convertimos a string
            latex_strs.append(str(e))
            
    # Unimos con saltos de línea para renderizarlos uno debajo de otro
    markdown_str = "\n\n".join(latex_strs)
    
    # Enviamos la representación agrupada al frontend usando la API nativa de cadabra2_jupyter
    server.send(markdown_str, "latex_view", "", "", False)
