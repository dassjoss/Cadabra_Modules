import cadabra2
from cadabra2 import rename_dummies, sort_product, eliminate_metric

def eliminar_metricas_bucle(ex, n):
    """
    Elimina métricas de una expresión Cadabra ejecutando un bucle
    de n iteraciones de sort_product y eliminate_metric intercalados.

    Este algoritmo está diseñado para procesar y contraer métricas puente
    (como \eta y g) que han sido inyectadas para subir o bajar índices.
    Dado que Cadabra en ocasiones necesita reordenar los términos algebraicos
    (`sort_product`) para lograr que los índices mudos coincidan posicionalmente
    y puedan ser eliminados (`eliminate_metric`), esta función realiza múltiples
    ciclos de dichas operaciones. También invoca `rename_dummies` para evitar
    conflictos entre índices mudos durante y antes del proceso.

    Parameters
    ----------
    ex : cadabra2.Ex
        La expresión matemática de Cadabra que contiene las métricas a eliminar.
    n : int
        El número máximo de movimientos/contracciones requeridas. Actúa como
        número de iteraciones para el bucle. Debe ser un entero positivo.

    Returns
    -------
    cadabra2.Ex
        La misma expresión de Cadabra recibida pero modificada in-place (mutada)
        con las métricas puente eliminadas.
    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError(
            "El parámetro 'n' debe ser un número entero natural mayor a 0."
        )

    rename_dummies(ex)

    for _ in range(n):

        rename_dummies(ex)

        sort_product(ex)
        eliminate_metric(ex)

        sort_product(ex)
        eliminate_metric(ex)

        sort_product(ex)
        eliminate_metric(ex)

    rename_dummies(ex)

    return ex
