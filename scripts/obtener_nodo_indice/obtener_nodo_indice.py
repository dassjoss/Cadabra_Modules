from cadabra2 import parent_rel_t
from scripts.get_full_index_name import get_full_index_name


def obtener_nodo_indice(expr, nombre_buscado):
    """
    Busca y devuelve el ExNode correspondiente a un indice libre
    llamado 'nombre_buscado'.

    Primero verifica que 'nombre_buscado' corresponda efectivamente
    a uno de los indices libres reconocidos por Cadabra. Luego recorre
    el arbol de la expresion buscando un nodo cuya relacion con su
    padre sea super o sub y cuyo nombre completo coincida con
    'nombre_buscado'.

    La mutacion real del nodo no se realiza aqui; esta funcion
    unicamente localiza y devuelve el ExNode encontrado.

    Es importante devolver el nodo inmediatamente al encontrar la
    coincidencia, ya que los ExNode obtenidos mediante iter(expr)
    funcionan como cursores mutables. Continuar la iteracion despues
    de encontrar el nodo puede hacer que la referencia pase a apuntar
    a otra posicion del arbol.

    En particular, esto permite conservar correctamente indices con
    subindices numericos, como \\lambda_{1}, sin devolver accidentalmente
    el nodo correspondiente al subindice numerico.

    Parameters
    ----------
    expr : cadabra2.Ex
        Expresion de Cadabra en cuyo arbol se buscara el indice.

    nombre_buscado : str
        Nombre completo del indice libre que se desea localizar.
        Pueden incluir subindices numericos, por ejemplo
        '\\lambda_{1}'.

    Returns
    -------
    cadabra2.ExNode
        Nodo correspondiente al indice libre encontrado en el arbol
        de la expresion.

    Raises
    ------
    ValueError
        Si 'nombre_buscado' no corresponde a un indice libre de la
        expresion.

    RuntimeError
        Si Cadabra reconoce el indice como libre, pero no se encuentra
        el ExNode correspondiente durante el recorrido del arbol.
    """

    nombres_indices_libres = []

    for indice in expr.top().free_indices():
        nombre_completo = get_full_index_name(indice)
        nombres_indices_libres.append(nombre_completo)

    if nombre_buscado not in nombres_indices_libres:
        raise ValueError(
            f"El indice {nombre_buscado} no es un indice libre de la expresion."
        )

    for nodo in iter(expr):
        if nodo.parent_rel not in (
            parent_rel_t.super,
            parent_rel_t.sub
        ):
            continue

        nombre_nodo = get_full_index_name(nodo)

        if nombre_nodo == nombre_buscado:
            return nodo

    raise RuntimeError(
        f"El indice libre {nombre_buscado} fue reconocido por Cadabra, "
        f"pero no se encontro su ExNode en el arbol."
    )
