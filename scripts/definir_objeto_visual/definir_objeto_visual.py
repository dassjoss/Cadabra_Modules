from cadabra2 import Ex, LaTeXForm, LaTeXString

def definir_objeto_visual(nombre, expresion_visual, ver=True):
    """
    Crea un objeto cadabra2.Ex con el nombre indicado, registra una 
    representación visual personalizada mediante LaTeXForm e inyecta el objeto 
    como variable Python en el globals() del contexto donde se ejecuta.

    Parameters
    ----------
    nombre : str
        El nombre simbólico del objeto en Cadabra (ej. "variacion_prueba").
    expresion_visual : str
        La representación LaTeX personalizada para el objeto.
    ver : bool, optional
        Si es True (por defecto), muestra el mensaje de registro y el objeto 
        renderizado mediante los mecanismos display disponibles en el entorno 
        Cadabra/Jupyter. Si es False, registra el objeto silenciosamente.

    Returns
    -------
    cadabra2.Ex
        El objeto cadabra2.Ex creado y registrado en el kernel.
    """
    sym_ex = Ex(nombre)

    latex_str = f'"{expresion_visual}"'
    LaTeXForm(sym_ex, Ex(latex_str))

    globals()[nombre] = sym_ex

    if ver == True:
        display(f"'{nombre}' registrado.")
        display(sym_ex)

    return sym_ex