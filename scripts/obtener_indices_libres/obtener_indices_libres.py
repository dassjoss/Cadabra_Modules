from cadabra2 import Ex
from .indices_producto import indices_producto
from .eliminar_dummies import eliminar_dummies


def fundamental(expr):
    """
    Recorre recursivamente una expresión y obtiene todos
    sus índices sin eliminar contracciones.
    """

    # =========================================================
    # COPIA INDEPENDIENTE DEL ÁRBOL
    # =========================================================

    copia = Ex(str(expr))
    nodo = copia.top()

    # =========================================================
    # PRODUCTO
    # =========================================================

    factores = list(nodo.factors())

    if len(factores) > 1:

        return indices_producto(nodo, fundamental)

    # =========================================================
    # HOJA
    # =========================================================

    lista_indices = []

    for indice in nodo.indices():

        lista_indices.append(
            (
                str(indice),
                str(indice.parent_rel).split(".")[-1]
            )
        )

    return lista_indices


def obtener_indices_libres(expr):
    """
    Obtiene los índices libres de una expresión de Cadabra.

    Primero recorre recursivamente toda la expresión mediante
    fundamental() y posteriormente elimina los índices dummy.
    """

    # =========================================================
    # RECORRIDO RECURSIVO
    # =========================================================

    lista_indices = fundamental(expr)

    # =========================================================
    # ELIMINAR DUMMIES
    # =========================================================

    lista_indices = eliminar_dummies(lista_indices)

    # =========================================================
    # RESULTADO
    # =========================================================

    return lista_indices