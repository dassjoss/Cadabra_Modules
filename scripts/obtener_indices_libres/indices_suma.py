from .eliminar_dummies import eliminar_dummies


def indices_suma(nodo, fundamental):
    """
    Procesa un nodo suma sin reconstruir la suma completa mediante Ex().

    Cada término de la suma se extrae mediante termino.ex(),
    obteniendo así una expresión Ex independiente para cada término.

    Luego cada término se procesa recursivamente mediante fundamental().

    Parameters
    ----------
    nodo : cadabra2.ExNode
        El nodo que representa la suma.
    fundamental : callable
        Función recursiva para analizar subexpresiones.

    Returns
    -------
    list of tuple
        La lista de tuplas (representación, posición) con los índices libres comunes de todos los términos de la suma.
    """

    print("NODO SUMA:", nodo)

    indices_terminos = []

    for i, termino in enumerate(nodo.children()):

        print(f"\n--- TÉRMINO {i} ---")
        print("NODO ORIGINAL:")
        print(termino)

        termino_ex = termino.ex()

        print("EX INDEPENDIENTE:")
        print(termino_ex)

        indices = fundamental(termino_ex)

        indices = eliminar_dummies(indices)

        print("ÍNDICES LIBRES:")
        print(indices)

        indices_terminos.append(indices)

    if not indices_terminos:
        return []

    referencia = set(indices_terminos[0])

    for i, indices in enumerate(indices_terminos[1:], start=1):

        conjunto = set(indices)

        if conjunto != referencia:

            raise ValueError(
                "Los términos de la suma no tienen los mismos "
                "índices libres.\n"
                f"Término 0: {indices_terminos[0]}\n"
                f"Término {i}: {indices}"
            )

    return indices_terminos[0]