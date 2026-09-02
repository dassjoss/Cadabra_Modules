import multiprocessing
from cadabra2 import *


def _worker_ordenar(expr_str, sort_order_str):
    """
    Ordena un único término de una expresión de Cadabra dentro de un
    subproceso independiente.

    La función recibe tanto la expresión como el orden de los factores
    representados como cadenas de texto. Reconstruye ambas expresiones
    mediante `Ex`, aplica el `SortOrder` especificado y finalmente utiliza
    `sort_product` para ordenar los factores del término.

    Esta función es utilizada internamente por `sort_product_with_order`
    y está diseñada para procesar un único término, no una suma completa.

    Args:
        expr_str: str
            Expresión de Cadabra correspondiente a un único término o
            producto. No debe contener una suma de varios términos.

        sort_order_str: str
            Cadena que representa el orden deseado de los factores.
            Debe tener el formato aceptado por `SortOrder`.
            Ejemplo:
                r'{g**{-1/2},P_{a b}^{l},P^{b}_{c}^{i},\epsilon{#}}'

    Returns:
        str
            Representación en formato de entrada de Cadabra del término
            después de aplicar el ordenamiento.
    """

    # Aquí expr_str representa UN SOLO TÉRMINO
    expr = Ex(expr_str)

    e_order = Ex(sort_order_str)

    # SortOrder requiere al menos dos elementos en la lista
    if e_order.top().name == r'\comma':
        SortOrder(e_order)

    sort_product(expr)

    return str(expr)


def sort_product_with_order(ex, orden_str):
    """
    Ordena un único término o producto de una expresión de Cadabra
    utilizando `SortOrder` dentro de un subproceso aislado.

    La expresión y el orden de los factores se convierten a cadenas de
    texto antes de ser enviados al subproceso. El término es reconstruido
    dentro del subproceso, ordenado mediante `SortOrder` y `sort_product`,
    y posteriormente reconstruido como un objeto `cadabra2.Ex`.

    Esta función está diseñada para trabajar con un único término.
    Cuando `ex` contiene una suma, la función `ordenar` se encarga de
    separar previamente sus términos y procesarlos individualmente.

    Args:
        ex: cadabra2.Ex
            Término o producto de Cadabra que se desea ordenar.

        orden_str: str o cadabra2.Ex
            Orden de los factores que será utilizado por `SortOrder`.
            Puede proporcionarse como una cadena de texto o como una
            expresión de Cadabra.

            Ejemplo:
                r'g**{-1/2},P_{a b}^{l},P^{b}_{c}^{i},\epsilon{#}'

    Returns:
        cadabra2.Ex
            Expresión resultante después de ordenar sus factores según
            el orden especificado.
    """

    expr_str = str(ex)
    sort_order_str = str(orden_str)

    with multiprocessing.Pool(1) as pool:
        resultado_str = pool.apply(
            _worker_ordenar,
            (expr_str, sort_order_str)
        )

    return Ex(resultado_str)


def ordenar(ex, orden_str):
    """
    Ordena los factores de una expresión de Cadabra según el orden
    proporcionado.

    Si la expresión es una suma, separa sus términos y ordena cada uno
    independientemente mediante `sort_product_with_order`. Posteriormente
    reconstruye la suma utilizando los términos ya ordenados.

    Si la expresión no es una suma, se procesa directamente como un único
    término mediante `sort_product_with_order`.

    La separación de los términos de una suma permite evitar problemas
    asociados con el análisis de índices cuando una suma completa se
    reconstruye directamente a partir de una cadena de texto.

    Args:
        ex: cadabra2.Ex
            Expresión de Cadabra que se desea ordenar. Puede corresponder
            tanto a un único producto como a una suma de varios términos.

        orden_str: str o cadabra2.Ex
            Orden de los factores que se utilizará para ordenar cada
            término de la expresión.

            Ejemplo:
                r'g**{-1/2},P_{a b}^{l},P^{b}_{c}^{i},\epsilon{#}'

    Returns:
        cadabra2.Ex
            Expresión con los factores de cada término ordenados según
            `orden_str`.

    Notes:
        Cuando `ex` es una suma, sus términos se extraen como expresiones
        independientes antes de ser procesados. La suma final se
        reconstruye mediante la suma de los objetos `Ex` resultantes.

        No se reconstruye la suma mediante una cadena del tipo
        `Ex("termino1 + termino2 + ...")`, ya que dicha reconstrucción
        puede provocar problemas en el análisis de los índices de los
        diferentes términos.
    """

    # ==========================================================
    # SUMA
    # ==========================================================
    if ex.top().name == r'\sum':

        # Igual que en d_c_g:
        # cada término se convierte en un Ex independiente.
        sumandos = [s.ex() for s in ex.top().args()]

        terminos_ordenados = []

        for sumando in sumandos:
            resultado = sort_product_with_order(
                sumando,
                orden_str
            )

            terminos_ordenados.append(resultado)

        # ======================================================
        # RECONSTRUCCIÓN SEGURA DE LA SUMA
        # ======================================================
        #
        # NO hacemos:
        #
        # Ex(" + ".join(...))
        #
        # porque eso vuelve a parsear toda la suma de una vez.
        #
        if not terminos_ordenados:
            return Ex(r"0")

        resultado = terminos_ordenados[0].copy()

        for termino in terminos_ordenados[1:]:
            resultado = resultado + termino

        return resultado

    # ==========================================================
    # PRODUCTO / TÉRMINO INDIVIDUAL
    # ==========================================================
    return sort_product_with_order(ex, orden_str)