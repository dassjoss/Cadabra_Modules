from cadabra2 import parent_rel_t

from .eliminar_dummies import eliminar_dummies


def indices_operador(nodo, fundamental):
    """
    Obtiene los índices libres de un operador genérico.

    `nodo` pertenece al árbol de una expresión Ex independiente,
    pero no se reconstruye el operador mediante Ex(str(nodo)).

    Los índices propios del operador se obtienen directamente de
    `nodo`, mientras que su argumento se convierte mediante `.ex()`
    antes de pasarlo recursivamente a `fundamental()`.

    Parameters
    ----------
    nodo : cadabra2.ExNode
        El nodo que representa al operador.
    fundamental : callable
        Función recursiva para analizar subexpresiones.

    Returns
    -------
    list of tuple
        La lista de tuplas (representación, posición) con los índices del operador y su argumento.
    """

    # =========================================================
    # ÍNDICES PROPIOS DEL OPERADOR
    # =========================================================

    indices_propios = list(
        nodo.own_indices()
    )

    # =========================================================
    # ARGUMENTOS DEL OPERADOR
    # =========================================================

    argumentos = list(
        nodo.args()
    )

    if len(argumentos) == 0:
        return []

    # =========================================================
    # COPIA INDEPENDIENTE DEL ARGUMENTO
    # =========================================================

    argumento_ex = argumentos[0].ex()

    # =========================================================
    # ANALIZAR RECURSIVAMENTE EL ARGUMENTO
    # =========================================================

    indices_argumento = fundamental(
        argumento_ex
    )

    # =========================================================
    # CONSTRUIR LISTA DE ÍNDICES DEL OPERADOR
    # =========================================================

    lista_indices = []

    for indice in indices_propios:

        if indice.parent_rel == parent_rel_t.super:
            posicion = "super"

        elif indice.parent_rel == parent_rel_t.sub:
            posicion = "sub"

        else:
            raise ValueError(
                "Posición de índice del operador no reconocida: "
                + str(indice.parent_rel)
            )

        lista_indices.append(
            (
                str(indice),
                posicion
            )
        )

    # =========================================================
    # AÑADIR ÍNDICES DEL ARGUMENTO
    # =========================================================

    lista_indices.extend(
        indices_argumento
    )

    # =========================================================
    # ELIMINAR DUMMIES
    # =========================================================

    return eliminar_dummies(
        lista_indices
    )