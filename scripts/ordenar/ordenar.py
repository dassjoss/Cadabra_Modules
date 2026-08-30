import multiprocessing
from cadabra2 import *


def _worker_ordenar(expr_str, sort_order_str):
    import cadabra2
    from cadabra2 import Ex, SortOrder, sort_product

    expr = Ex(expr_str)
    e_order = Ex(sort_order_str)

    # SortOrder requiere al menos dos elementos en una lista
    if e_order.top().name == r'\comma':
        SortOrder(e_order)

    sort_product(expr)
    return str(expr)


def sort_product_with_order(ex, orden_str):
    """
    Ordena un producto utilizando SortOrder dentro de un subproceso
    aislado de Cadabra.
    """
    expr_str = str(ex)

    with multiprocessing.Pool(1) as pool:
        resultado_str = pool.apply(_worker_ordenar, (expr_str, orden_str))

    return Ex(resultado_str)


def ordenar(ex, orden_str):
    """
    Ordena una expresión según el orden proporcionado.

    Si la expresión es una suma, ordena cada término
    independientemente.

    Si no es una suma, delega directamente el ordenamiento
    del producto a sort_product_with_order().
    """

    if ex.top().name == r'\add':
        terminos_ordenados = []

        for term in ex.top().children():
            term_ex = Ex(str(term))
            res_term = ordenar(term_ex, orden_str)
            terminos_ordenados.append(str(res_term))

        return Ex(" + ".join(terminos_ordenados))

    return sort_product_with_order(ex, orden_str)