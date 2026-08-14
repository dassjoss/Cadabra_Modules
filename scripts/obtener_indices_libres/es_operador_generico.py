from cadabra2 import Ex, parent_rel_t


def es_operador_generico(nodo):
    """
    Determina si un nodo puede interpretarse como un operador
    genérico según el criterio adoptado.

    Un nodo es considerado operador genérico si:

        1. Tiene al menos un índice propio.
        2. Al menos uno de sus índices propios es subíndice (o superíndice).
        3. Tiene un argumento no vacío.

    No se intenta identificar el símbolo del operador.

    Parameters
    ----------
    nodo : cadabra2.ExNode
        El nodo que se va a evaluar.

    Returns
    -------
    bool
        True si el nodo es un operador genérico, False en caso contrario.
    """

    # =========================================================
    # COPIA INDEPENDIENTE DEL ÁRBOL
    # =========================================================

    expr = Ex(str(nodo))
    raiz = expr.top()

    # =========================================================
    # ÍNDICES PROPIOS DE LA RAÍZ
    # =========================================================

    indices_raiz = list(raiz.own_indices())

    # =========================================================
    # DEBE TENER AL MENOS UN ÍNDICE PROPIO
    # =========================================================

    if len(indices_raiz) == 0:
        return False

    # =============================================================================
    # DEBE TENER UN ARGUMENTO
    # =============================================================================

    argumentos = list(raiz.args())

    if len(argumentos) == 0:
        return False

    # =========================================================
    # ARGUMENTO NO VACÍO
    # =========================================================

    argumento = argumentos[0]

    if str(argumento).strip() == "":
        return False

    return True