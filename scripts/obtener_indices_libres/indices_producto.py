def indices_producto(nodo, fundamental):
    """
    Procesa un nodo que corresponde a un producto.

    Recorre cada factor y utiliza fundamental()
    para procesarlo recursivamente.
    """

    print("NODO PRODUCTO:", nodo)

    lista_indices = []

    for i, factor in enumerate(nodo.factors()):

        factor_ex = factor.ex()

        indices = fundamental(factor_ex)

        lista_indices.extend(indices)

    return lista_indices