from cadabra2 import parent_rel_t
from scripts.get_full_index_name import get_full_index_name
from scripts.mutar_nodo_indice import mutar_nodo_indice
from scripts.mutar_indice import mutar_indice


def mutar_indice_dos(expr, nombre_original, nombre_nuevo):
    """
    Busca dentro de 'expr' hasta dos ocurrencias del índice llamado
    'nombre_original' y las muta a 'nombre_nuevo'.

    La función opera llamando repetidamente a `mutar_indice`. Está diseñada
    específicamente para facilitar el cambio de pares de índices (por ejemplo,
    índices mudos contraídos que aparecen dos veces en un término).

    La mutación estructural modifica el árbol de la expresión original de
    forma in-place (no se devuelve una copia).

    Tolerancia a fallos y Comportamiento:
        - Si la expresión contiene 2 o más ocurrencias de 'nombre_original',
          se mutarán exactamente las dos primeras encontradas.
        - Si la expresión contiene exactamente 1 ocurrencia, se mutará esa única
          aparición. El intento de mutar la segunda lanzará un RuntimeError
          internamente en `mutar_indice`, el cual es capturado silenciosamente.
        - Si la expresión no contiene ninguna ocurrencia, lanzará un `RuntimeError`
          desde el primer intento (replicando el comportamiento original de
          `mutar_indice`).

    Args:
        expr: cadabra2.Ex
            Expresión de Cadabra (o iterable de nodos) sobre la cual realizar
            la búsqueda y mutación. El objeto se modifica in-place.

        nombre_original: str
            Nombre completo del índice que se desea buscar.
            Ejemplo: r'\alpha' o r'\lambda_{1}'.

        nombre_nuevo: str
            Nombre completo que tendrá el índice tras la mutación.
            Ejemplo: r'\beta' o r'\mu_{2}'.

    Returns:
        None
            La función opera mediante efectos secundarios (mutación del árbol)
            y no retorna ningún valor.

    Raises:
        ValueError, RuntimeError:
            Cualquier error estructural derivado de `mutar_nodo_indice` (por
            ejemplo, si `nombre_nuevo` tiene una sintaxis de subíndice inválida)
            se propagará normalmente hacia arriba. El `RuntimeError` por no
            encontrar el índice solo se lanza si hay 0 ocurrencias; si hay
            exactamente 1 ocurrencia, el error del segundo intento se silencia.
    """
    mutados = 0
    for i in range(2):
        try:
            mutar_indice(expr, nombre_original, nombre_nuevo)
            mutados += 1
        except RuntimeError as e:
            if mutados == 0:
                # Si no logró mutar ni siquiera 1, propagamos el error
                raise e
            # Si logró mutar 1 y falló en el 2do intento, silenciamos y salimos
            break
    
    
