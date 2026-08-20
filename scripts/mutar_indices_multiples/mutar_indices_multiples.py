from cadabra2 import parent_rel_t
from scripts.get_full_index_name import get_full_index_name
from scripts.mutar_nodo_indice import mutar_nodo_indice
from scripts.mutar_indice.mutar_indice import mutar_indice
from scripts.mutar_indices_dos.mutar_indice_dos import mutar_indice_dos

def mutar_indices_multiples(expr, conjunto_original, conjunto_nuevo, termino_suma=None, repetido=False):
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
            Expresión de Cadabra sobre la cual realizar la mutación. El objeto
            se modifica in-place.

        conjunto_original: str
            Cadena de texto con los nombres completos de los índices originales,
            separados por comas.
            Ejemplo: r'\\alpha, \\beta_{1}, \\gamma'

        conjunto_nuevo: str
            Cadena de texto con los nombres completos de los nuevos índices,
            separados por comas. Debe tener la misma cantidad de elementos
            que `conjunto_original`.
            Ejemplo: r'\\mu, \\nu_{1}, \\rho'

        termino_suma: int, opcional (por defecto None)
            Si se proporciona un número entero (0, 1, 2...), la mutación se
            aplicará ÚNICAMENTE a ese término de la suma. Si es None, la
            mutación se aplicará a toda la expresión `expr`.
            Asume que `expr` es una suma y extrae sus hijos directos.

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
        IndexError:
            Si `termino_suma` se sale del rango de los términos disponibles.
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
    if termino_suma is not None:
        termino_encontrado = False
        # Debemos iterar manualmente y detenernos en el índice deseado.
        # En la API de Cadabra (C++ wrapper), usar list(children()) crea copias del
        # mismo puntero que termina apuntando siempre al último elemento.
        for idx, child in enumerate(expr.top().children()):
            if idx == termino_suma:
                termino_encontrado = True
                
                # Crear copia independiente del término (.ex() devuelve un objeto Ex)
                termino_independiente = child.ex()
                
                # Aplicar la mutación sobre la copia independiente
                for i in range(len(lista_original)):
                    if repetido:
                        mutar_indice_dos(termino_independiente, lista_original[i], lista_nuevo[i])
                    else:
                        mutar_indice(termino_independiente, lista_original[i], lista_nuevo[i])
                        
                # Reemplazar el nodo original con el término mutado en el árbol principal
                child.replace(termino_independiente)
                
                # Rompemos el ciclo inmediatamente para evitar que el iterador se corrompa
                break
                
        if not termino_encontrado:
            raise IndexError(f"El término {termino_suma} está fuera de rango.")
        
    else:
        # Comportamiento original: mutar toda la expresión globalmente
        for i in range(len(lista_original)):
            if repetido:
                mutar_indice_dos(expr, lista_original[i], lista_nuevo[i])
            else:
                mutar_indice(expr, lista_original[i], lista_nuevo[i])
