import sys

from cadabra2 import Ex, LaTeXForm, __cdbkernel__


def definir_objeto_visual(nombre: str, expresion_visual: str, ver: bool = True) -> Ex:
    """
    Crea un objeto cadabra2.Ex con el nombre indicado, registra una
    representación visual personalizada mediante LaTeXForm y lo
    inyecta en el namespace de la celda llamadora.

    Parameters
    ----------
    nombre : str
        El nombre simbólico del objeto en Cadabra (ej. "variacion_prueba").
    expresion_visual : str
        La representación LaTeX personalizada para el objeto.
    ver : bool, optional
        Si es True (por defecto), muestra el mensaje de registro y el objeto
        renderizado utilizando la función display de la celda llamadora.
        Si es False, registra el objeto de forma silenciosa.

    Returns
    -------
    cadabra2.Ex
        El objeto cadabra2.Ex creado y registrado en el kernel.
    """

    sym_ex = Ex(nombre)

    LaTeXForm(sym_ex, Ex(f'"{expresion_visual}"'))

    cell_globals = sys._getframe(1).f_globals

    cell_globals[nombre] = sym_ex

    if ver:
        cell_display = cell_globals["display"]
        cell_display(f"'{nombre}' registrado.")
        cell_display(sym_ex)

    return sym_ex