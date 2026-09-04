from scripts.mutar_indices_multiples.mutar_indices_multiples import mutar_indices_multiples




def mutar_todos_indices_dummies(ex, indices_originales, indices_nuevos):
    """
    Muta índices dummy término por término en una suma de Cadabra.

    La función recorre todos los términos directos de una suma y, para cada
    término, intenta realizar las sustituciones indicadas en
    `indices_originales` -> `indices_nuevos`.

    Cada mutación se realiza mediante `mutar_indices_multiples` con
    `repetido=True`, por lo que esta función está pensada específicamente
    para índices dummy (índices repetidos/contraídos), no para índices libres.

    Si uno de los índices originales no aparece como dummy en un término
    determinado y `mutar_indices_multiples`/`mutar_indice_dos` genera un
    TypeError, ese índice se ignora únicamente para ese término y se continúa
    con los demás índices.

    La expresión original no se modifica. Se trabaja sobre una copia y se
    retorna la expresión resultante.

    Args:
        ex: cadabra2.Ex
            Expresión de Cadabra que debe ser una suma.

        indices_originales: str
            Índices dummy originales separados por comas.
            Ejemplo:
                r'a,b,c'

        indices_nuevos: str
            Nuevos nombres de los índices, separados por comas.
            Debe contener la misma cantidad de elementos que
            `indices_originales`.
            Ejemplo:
                r'a_{1},b_{1},c_{1}'

    Returns:
        cadabra2.Ex
            Nueva expresión con las mutaciones aplicadas término por término.

    Raises:
        ValueError:
            Si la cantidad de índices originales y nuevos no coincide.

        TypeError:
            Si `ex` no es una suma.
    """

    # 1. Separar y limpiar los índices.
    lista_indices_originales = [
        indice.strip()
        for indice in indices_originales.split(',')
    ]

    lista_indices_nuevos = [
        indice.strip()
        for indice in indices_nuevos.split(',')
    ]

    # 2. Comprobar que ambos conjuntos tengan el mismo tamaño.
    if len(lista_indices_originales) != len(lista_indices_nuevos):
        raise ValueError(
            "La cantidad de índices originales "
            f"({len(lista_indices_originales)}) no coincide con la cantidad "
            f"de índices nuevos ({len(lista_indices_nuevos)})."
        )

    # 3. Esta función está diseñada para trabajar sobre una suma.
    if ex.top().name != r'\sum':
        raise TypeError(
            "mutar_todos_indices_dummies requiere una expresión de tipo suma."
        )

    # 4. Trabajar sobre una copia para no modificar la expresión original.
    retorno = ex.copy()

    # 5. Contar los términos sin almacenar los children().
    #
    # No usamos:
    #
    #     list(retorno.top().children())
    #
    # porque el wrapper C++ de Cadabra puede reutilizar los punteros/nodos
    # durante la iteración.
    numero_terminos = sum(
        1 for _ in retorno.top().children()
    )

    # 6. Recorrer cada término por su posición.
    for termino_suma in range(numero_terminos):

        # 7. Para este término, intentar cada cambio de índice.
        for indice_original, indice_nuevo in zip(
            lista_indices_originales,
            lista_indices_nuevos
        ):
            try:
                mutar_indices_multiples(
                    retorno,
                    indice_original,
                    indice_nuevo,
                    termino_suma=termino_suma,
                    repetido=True
                )

            except RuntimeError:
                # Ese índice no puede mutarse en este término.
                # Continuamos con el siguiente índice.
                pass

    return retorno