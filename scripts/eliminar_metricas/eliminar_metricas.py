from cadabra2 import rename_dummies, sort_product, eliminate_metric

def eliminar_metricas(ex, n=1):
    """
    Elimina métricas de una expresión Cadabra ejecutando un bucle de n iteraciones
    de sort_product y eliminate_metric intercalados.

    Parameters
    ----------
    ex : cadabra2.Ex
        Expresión de Cadabra a modificar (se modifica in-place).
    n : int, optional
        Número entero natural mayor a 0 (n > 0).

    Returns
    -------
    cadabra2.Ex
        La expresión resultante con las métricas eliminadas.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("El parámetro 'n' debe ser un número entero natural mayor a 0.")

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
