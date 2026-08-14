def indices_producto(nodo, fundamental):
    """
    Procesa un nodo producto.

    Cada factor se convierte en un Ex independiente mediante .ex()
    antes de ser enviado recursivamente a fundamental().

    No se reconstruye el producto completo mediante Ex(str(nodo)).

    Parameters
    ----------
    nodo : cadabra2.ExNode
        El nodo que representa el producto.
    fundamental : callable
        Función recursiva para analizar subexpresiones.

    Returns
    -------
    list of tuple
        La lista de tuplas (representación, posición) con todos los índices acumulados de los factores.
    """

    lista_indices = []

    for factor in nodo.factors():

        # Copia independiente del factor
        factor_ex = factor.ex()

        # Análisis recursivo
        indices = fundamental(factor_ex)

        # Acumular índices sin eliminar dummies
        lista_indices.extend(indices)

    return lista_indices