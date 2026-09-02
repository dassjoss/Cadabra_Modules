import cadabra2
from cadabra2 import collect_factors, eliminate_metric


def eliminar_metricas_bucle(ex, n):
    """
    Elimina métricas de una expresión Cadabra ejecutando un bucle
    de n iteraciones de collect_factors y eliminate_metric intercalados.

    Las propiedades de índices y métricas de Cadabra deben haber sido
    declaradas previamente en el kernel. Esta función NO registra
    propiedades globales del kernel.

    Parameters
    ----------
    ex : cadabra2.Ex
        Expresión matemática que contiene las métricas a eliminar.

    n : int
        Número de iteraciones del proceso.

    indices_familias : dict, opcional
        Se conserva por compatibilidad con la API anterior. No se utiliza
        para registrar propiedades del kernel.

    metricas_map : dict, opcional
        Se conserva por compatibilidad con la API anterior. No se utiliza
        para registrar propiedades del kernel.

    Returns
    -------
    cadabra2.Ex
        La expresión con las métricas eliminadas.
    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError(
            "El parámetro 'n' debe ser un número entero natural mayor a 0."
        )

    for _ in range(n):
        collect_factors(ex)
        eliminate_metric(ex)

        collect_factors(ex)
        eliminate_metric(ex)

        collect_factors(ex)
        eliminate_metric(ex)

    return ex