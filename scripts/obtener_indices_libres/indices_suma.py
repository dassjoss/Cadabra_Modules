from .eliminar_dummies import eliminar_dummies


def indices_suma(nodo, fundamental):
    """
    Procesa una suma término por término.

    fundamental() debe conservar todos los índices de cada término.
    eliminar_dummies() se utiliza únicamente para determinar los índices
    libres de cada término y verificar que la suma sea tensorialmente válida.

    Para el resultado de fundamental(), los índices libres se conservan
    y cada índice dummy se representa mediante un único par sub/super,
    independientemente de cuántas veces aparezca en distintos términos.
    """

    indices_terminos = []
    libres_terminos = []

    # =========================================================
    # PROCESAR CADA TÉRMINO INDEPENDIENTEMENTE
    # =========================================================

    for termino in nodo.children():

        termino_ex = termino.ex()

        # fundamental() devuelve TODOS los índices.
        indices = fundamental(termino_ex)

        # eliminar_dummies() se usa solamente para obtener
        # los índices libres del término.
        libres = eliminar_dummies(indices)

        indices_terminos.append(indices)
        libres_terminos.append(libres)

    if not indices_terminos:
        return []

    # =========================================================
    # VALIDAR ÍNDICES LIBRES DE LA SUMA
    # =========================================================

    referencia = set(libres_terminos[0])

    for i, libres in enumerate(libres_terminos[1:], start=1):

        conjunto = set(libres)

        if conjunto != referencia:

            raise ValueError(
                "Los términos de la suma no tienen los mismos "
                "índices libres.\n"
                f"Término 0: {libres_terminos[0]}\n"
                f"Término {i}: {libres}"
            )

    # =========================================================
    # CONSTRUIR RESULTADO DE fundamental()
    # =========================================================

    resultado = list(libres_terminos[0])

    dummies = {}

    for indices, libres in zip(indices_terminos, libres_terminos):

        libres_set = set(libres)

        for nombre, posicion in indices:

            # Los índices libres ya están en resultado.
            if (nombre, posicion) in libres_set:
                continue

            if nombre not in dummies:
                dummies[nombre] = {
                    "sub": 0,
                    "super": 0
                }

            dummies[nombre][posicion] += 1

    # =========================================================
    # CONSOLIDAR DUMMIES
    # =========================================================

    for nombre, posiciones in dummies.items():

        n_sub = posiciones["sub"]
        n_super = posiciones["super"]

        # Convención de Einstein:
        # todo dummy debe aparecer con igual número de índices
        # arriba y abajo.
        if n_sub != n_super:

            raise ValueError(
                f"El índice dummy '{nombre}' no cumple la "
                "convención de Einstein: "
                f"{n_sub} sub y {n_super} super."
            )

        # Para fundamental() solamente conservamos
        # un par representativo del dummy.
        if n_sub > 0:
            resultado.append((nombre, "sub"))
            resultado.append((nombre, "super"))

    return resultado