from .obtener_factor_multiplicativo.obtener_factor_multiplicativo import obtener_factor_multiplicativo
from .obtener_factor_exacto.obtener_factor_exacto import obtener_factor_exacto

def obtener_factor(expr, termino, exacto=False):
    """
    Función unificada para extraer factores multiplicativos en Cadabra.
    
    Si exacto es False, llama a obtener_factor_multiplicativo, el cual admite 
    comodines físicos (?) y respeta las reglas de covariancia.
    
    Si exacto es True, llama a obtener_factor_exacto, el cual borra el nodo 
    matemático basándose puramente en coincidencia de strings exactos (ideal para 
    evadir conflictos de índices sin dejar residuos numéricos).
    """
    if exacto:
        return obtener_factor_exacto(expr, termino)
    else:
        return obtener_factor_multiplicativo(expr, termino)
