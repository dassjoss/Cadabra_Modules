def get_full_index_name(n):
    """
    Reconstruye el nombre completo de un índice de Cadabra a partir de un
    objeto ``cadabra2.ExNode``.

    ENTRADA
    -------
    n : cadabra2.ExNode
        Nodo de Cadabra que representa un índice.

        Ejemplos válidos:
            α
            β
            λ_{1}
            λ_{4}
            α_{1}

        Para un índice simple, ``n.name`` contiene directamente su nombre.
        Para un índice con subíndice, ``n.name`` contiene el nombre base y
        el primer hijo contiene la representación del subíndice.

    SALIDA
    ------
    str
        Nombre completo del índice en formato textual de Cadabra.

        Ejemplos:
            α       -> '\\alpha'
            β       -> '\\beta'
            λ_{1}   -> '\\lambda_{1}'
            λ_{4}   -> '\\lambda_{4}'
            α_{1}   -> '\\alpha_{1}'

    FUNCIONAMIENTO
    --------------
    - Obtiene el nombre base mediante ``n.name``.
    - Obtiene los hijos mediante ``n.children()``.
    - Si el nodo no tiene hijos, devuelve únicamente ``n.name``.
    - Si tiene hijos, añade el primer hijo como subíndice usando ``str()``.

    LIMITACIONES
    ------------
    - ``n`` debe ser un ``cadabra2.ExNode``.
    - La función está diseñada para nodos que representan índices.
    - Si el nodo tiene varios hijos, solamente se utiliza el primer hijo.
    - No interpreta semánticamente el nodo; simplemente reconstruye el nombre
      a partir de ``name`` y del primer hijo.
    - Para subíndices numéricos, debe utilizarse ``str(children[0])`` y no
      ``children[0].name``, ya que Cadabra puede representar internamente
      todos estos nodos numéricos con el mismo ``name`` aunque su valor sea
      diferente.

    EJEMPLOS
    --------
    ``\\alpha``:
        n.name = '\\alpha'
        hijos = []
        resultado = '\\alpha'

    ``\\lambda_{1}``:
        n.name = '\\lambda'
        primer hijo = '1'
        resultado = '\\lambda_{1}'

    ``\\lambda_{4}``:
        n.name = '\\lambda'
        primer hijo = '4'
        resultado = '\\lambda_{4}'

    NOTA
    ----
    La función no modifica el ``ExNode`` recibido. Únicamente construye y
    devuelve una cadena de texto.
    """
    name = n.name
    children = list(n.children())
    if children:
        # Reconstruye la sintaxis del subindice
        name += "_{" + str(children[0]) + "}"
    return name
