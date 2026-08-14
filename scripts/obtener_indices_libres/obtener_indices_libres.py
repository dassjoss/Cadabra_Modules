from cadabra2 import Ex

from .indices_producto import indices_producto
from .indices_suma import indices_suma
from .indices_operador import indices_operador
from .eliminar_dummies import eliminar_dummies
from .es_operador_generico import es_operador_generico


def fundamental(expr):
    """
    Recorre recursivamente una expresión Ex independiente y obtiene
    todos sus índices sin eliminar contracciones.

    IMPORTANTE
    ----------
    `expr` debe ser siempre un objeto `cadabra2.Ex` independiente.

    Esta función NO reconstruye expresiones mediante Ex(str(expr)).
    Las subestructuras obtenidas durante la recursión deben convertirse
    en Ex independientes antes de volver a llamar a fundamental().
    """

    # =========================================================
    # EL OBJETO RECIBIDO YA ES UN Ex INDEPENDIENTE
    # =========================================================

    nodo = expr.top()

    # =========================================================
    # PRODUCTO
    # =========================================================

    if nodo.name == r'\prod':

        return indices_producto(
            nodo,
            fundamental
        )

    # =========================================================
    # SUMA
    # =========================================================

    if nodo.name == r'\sum':

        return indices_suma(
            nodo,
            fundamental
        )

    # =========================================================
    # OPERADOR GENÉRICO
    # =========================================================

    if es_operador_generico(nodo):

        return indices_operador(
            nodo,
            fundamental
        )

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

    Si `expr` ya es un objeto Ex independiente, se utiliza directamente
    sin reconstruirlo mediante Ex(str(expr)).

    Si `expr` no es un Ex, se crea una única copia independiente.

    A partir de ese momento, todo el recorrido recursivo trabaja
    exclusivamente con objetos Ex independientes.
    """

    # =========================================================
    # OBTENER EXPRESIÓN INDEPENDIENTE
    # =========================================================

    if isinstance(expr, Ex):

        expresion_independiente = expr

    else:

        expresion_independiente = Ex(
            str(expr)
        )

    # =========================================================
    # RECORRIDO RECURSIVO
    # =========================================================

    lista_indices = fundamental(
        expresion_independiente
    )

    # =========================================================
    # ELIMINAR DUMMIES
    # =========================================================

    lista_indices = eliminar_dummies(
        lista_indices
    )

    # =========================================================
    # RESULTADO
    # =========================================================

    return lista_indices