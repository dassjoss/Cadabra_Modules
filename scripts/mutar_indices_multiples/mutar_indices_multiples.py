from cadabra2 import parent_rel_t
from scripts.get_full_index_name import get_full_index_name
from scripts.mutar_nodo_indice import mutar_nodo_indice
from scripts.mutar_indice.mutar_indice import mutar_indice
from scripts.mutar_indices_dos.mutar_indice_dos import mutar_indice_dos

def mutar_indices_multiples(expr, conjunto_original, conjunto_nuevo, repetido=False):
    """
    Muta múltiples índices libres dentro de una expresión de Cadabra a partir
    de cadenas separadas por comas.

    Esta función procesa dos strings (conjuntos) de índices separados por comas,
    limpia los espacios en blanco, y muta uno por uno llamando internamente a
    `mutar_indice` o `mutar_indice_dos` dependiendo del parámetro `repetido`.

    Es especialmente útil cuando se necesita hacer un cambio masivo de nombres
    de índices en una expresión (ej. cambiar '\\alpha, \\beta, \\gamma' por
    '\\mu, \\nu, \\rho').

    Args:
        expr: cadabra2.Ex
            Expresión de Cadabra (o iterable de nodos) sobre la cual realizar
            la mutación. El objeto se modifica in-place.

        conjunto_original: str
            Cadena de texto con los nombres completos de los índices originales,
            separados por comas.
            Ejemplo: r'\\alpha, \\beta_{1}, \\gamma'

        conjunto_nuevo: str
            Cadena de texto con los nombres completos de los nuevos índices,
            separados por comas. Debe tener la misma cantidad de elementos
            que `conjunto_original`.
            Ejemplo: r'\\mu, \\nu_{1}, \\rho'

        repetido: bool, opcional (por defecto False)
            - Si es False, utilizará `mutar_indice` (cambiará 1 ocurrencia de
              cada índice).
            - Si es True, utilizará `mutar_indice_dos` (cambiará hasta 2
              ocurrencias de cada índice, útil para índices mudos contraídos).

    Returns:
        None
            La función opera mediante efectos secundarios (mutación del árbol)
            y no retorna ningún valor.

    Raises:
        ValueError:
            Si la cantidad de índices en `conjunto_original` no coincide con
            la cantidad de índices en `conjunto_nuevo`.
        RuntimeError:
            Propagado por `mutar_indice` si `repetido=False` y el índice no se
            encuentra en la expresión.
    """
    # 1. Separar las cadenas por comas y limpiar espacios en blanco (strip)
    lista_original = [idx.strip() for idx in conjunto_original.split(',')]
    lista_nuevo = [idx.strip() for idx in conjunto_nuevo.split(',')]

    # 2. Validar que las listas tengan la misma longitud
    if len(lista_original) != len(lista_nuevo):
        raise ValueError(
            f"Error: La cantidad de índices originales ({len(lista_original)}) no "
            f"coincide con la cantidad de índices nuevos ({len(lista_nuevo)})."
        )

    # 3. Iterar y aplicar la mutación correspondiente
    for i in range(len(lista_original)):
        if repetido:
            mutar_indice_dos(expr, lista_original[i], lista_nuevo[i])
        else:
            mutar_indice(expr, lista_original[i], lista_nuevo[i])
