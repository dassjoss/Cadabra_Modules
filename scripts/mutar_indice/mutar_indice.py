from cadabra2 import parent_rel_t
from scripts.get_full_index_name import get_full_index_name
from scripts.mutar_nodo_indice import mutar_nodo_indice


def mutar_indice(expr, nombre_original, nombre_nuevo):
    """
    Busca dentro de 'expr' la primera ocurrencia del indice libre
    llamado 'nombre_original' y la muta a 'nombre_nuevo'.

    La busqueda se realiza recorriendo la expresion y considerando
    unicamente nodos cuya relacion estructural sea 'super' o 'sub'.
    La identificacion completa del indice se obtiene mediante
    get_full_index_name().

    La mutacion estructural se delega en mutar_nodo_indice(), que
    conserva la posicion estructural del indice y reconstruye
    correctamente los subindices numericos mediante .multiplier.

    La funcion acepta expresiones que expongan un metodo .ex(),
    asi como iterables de nodos directamente.

    Importante:
        - Solo se muta la primera coincidencia encontrada.
        - No se mutan automaticamente todas las ocurrencias del mismo
          nombre de indice.
        - Si el indice no existe, se lanza RuntimeError.
        - 'nombre_original' y 'nombre_nuevo' se comparan utilizando
          el nombre completo reconstruido por get_full_index_name().
        - La funcion modifica la expresion recibida mediante la
          mutacion estructural realizada por mutar_nodo_indice().
        - El objeto Python devuelto por la funcion no debe utilizarse
          como garantia de identidad del ExNode original, ya que las
          operaciones de Cadabra pueden reconstruir los wrappers
          Python de los nodos.

    Ejemplos conceptuales:
        alpha       -> beta
        lambda_1    -> lambda_4
        lambda_1    -> alpha
        alpha       -> lambda_1
        alpha_10    -> lambda_25

    Args:
        expr:
            Expresion Cadabra o iterable de ExNode sobre el cual
            realizar la busqueda.

        nombre_original:
            Nombre completo del indice que se desea encontrar.

        nombre_nuevo:
            Nombre completo que tendra el indice encontrado.

    Returns:
        ExNode:
            El nodo sobre el cual se solicito la mutacion.

    Raises:
        RuntimeError:
            Si no se encuentra ninguna ocurrencia de
            'nombre_original'.
    """

    iterador = expr.ex() if hasattr(expr, "ex") else expr

    for nodo in iterador:
        if nodo.parent_rel not in (parent_rel_t.super, parent_rel_t.sub):
            continue

        if get_full_index_name(nodo) == nombre_original:
            mutar_nodo_indice(nodo, nombre_nuevo)
            return nodo

    raise RuntimeError(
        f"No se encontro el indice {nombre_original} para mutar."
    )
