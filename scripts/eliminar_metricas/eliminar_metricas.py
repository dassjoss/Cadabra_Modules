import cadabra2
from cadabra2 import rename_dummies, sort_product, collect_factors, eliminate_metric

def eliminar_metricas_bucle(ex, n, indices_familias, metricas_map=None):
    """
    Elimina métricas de una expresión Cadabra ejecutando un bucle
    de n iteraciones de collect_factors y eliminate_metric intercalados.

    Este algoritmo está diseñado para procesar y contraer métricas puente
    (como \eta y g) que han sido inyectadas para subir o bajar índices.
    Realiza inyección explícita del contexto local de Cadabra para que 
    rename_dummies y eliminate_metric funcionen correctamente al ser 
    importados desde otro módulo.

    Parameters
    ----------
    ex : cadabra2.Ex
        La expresión matemática de Cadabra que contiene las métricas a eliminar.
    n : int
        El número de iteraciones para el bucle.
    indices_familias : dict
        Diccionario con las familias de índices.
    metricas_map : dict, opcional
        Diccionario con las métricas correspondientes a cada familia.

    Returns
    -------
    cadabra2.Ex
    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError(
            "El parámetro 'n' debe ser un número entero natural mayor a 0."
        )

    # Inyección de contexto local para Cadabra C++ Kernel
    if indices_familias:
        from cadabra2 import Indices, Metric, InverseMetric, Ex
        for fam_name, fam_vars in indices_familias.items():
            if not fam_vars:
                continue
            
            # 1. Registrar los índices base para la familia
            vars_str = ",".join(fam_vars)
            Indices(Ex(vars_str), Ex(f"name={fam_name}, position=fixed"))
            
            # 2. Registrar la métrica y su inversa para la familia
            if metricas_map and fam_name in metricas_map:
                m_str = metricas_map[fam_name]
                # Construimos la estructura de la metrica localmente usando 
                # dos índices cualesquiera de la familia
                i1, i2 = fam_vars[0], fam_vars[1] if len(fam_vars) > 1 else fam_vars[0]
                
                Metric(Ex(f"{m_str}_{{{i1} {i2}}}"))
                InverseMetric(Ex(f"{m_str}^{{{i1} {i2}}}"))

    for _ in range(n):
        collect_factors(ex)
        eliminate_metric(ex)

        collect_factors(ex)
        eliminate_metric(ex)

        collect_factors(ex)
        eliminate_metric(ex)

    return ex
