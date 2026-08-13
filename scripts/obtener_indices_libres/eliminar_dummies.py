def eliminar_dummies(lista_indices):
    """
    Elimina de lista_indices los pares de índices contraídos.

    Cada índice tiene la forma:

        (representacion, posicion)

    donde posicion es 'super' o 'sub'.

    Reglas
    ------
    1. Una aparición:
       -> índice libre.

    2. Dos apariciones:
       -> posiciones opuestas: dummy, se eliminan ambas.

       -> misma posición: error.

    3. Tres o más apariciones:
       -> error.
    """

    # =========================================================
    # CONTAR APARICIONES
    # =========================================================

    apariciones = {}

    for indice in lista_indices:

        identidad = indice[0]

        if identidad not in apariciones:
            apariciones[identidad] = 0

        apariciones[identidad] += 1

    print("APARICIONES:")
    print(apariciones)

    # =========================================================
    # VERIFICAR MULTIPLICIDADES
    # =========================================================

    for identidad, cantidad in apariciones.items():

        print(
            "ÍNDICE:",
            identidad,
            "| APARICIONES:",
            cantidad
        )

        if cantidad > 2:

            raise ValueError(
                "El índice aparece más de dos veces: "
                + identidad
            )

    # =========================================================
    # CONSTRUIR RESULTADO
    # =========================================================

    lista_resultado = []

    for identidad, cantidad in apariciones.items():

        # -----------------------------------------------------
        # UNA SOLA APARICIÓN → LIBRE
        # -----------------------------------------------------

        if cantidad == 1:

            for indice in lista_indices:

                if indice[0] == identidad:
                    lista_resultado.append(indice)
                    break

        # -----------------------------------------------------
        # DOS APARICIONES
        # -----------------------------------------------------

        elif cantidad == 2:

            indices_encontrados = []

            for indice in lista_indices:

                if indice[0] == identidad:
                    indices_encontrados.append(indice)

            indice_a = indices_encontrados[0]
            indice_b = indices_encontrados[1]

            posicion_a = indice_a[1]
            posicion_b = indice_b[1]

            print(
                "COMPARANDO DUMMY:",
                indice_a,
                "CON",
                indice_b
            )

            # -------------------------------------------------
            # POSICIONES OPUESTAS → DUMMY
            # -------------------------------------------------

            if posicion_a != posicion_b:

                print(
                    "  >>> CONTRACCIÓN: ELIMINANDO DUMMY"
                )

                continue

            # -------------------------------------------------
            # MISMA POSICIÓN → ERROR
            # -------------------------------------------------

            else:

                raise ValueError(
                    "Índice repetido en la misma posición: "
                    + identidad
                )

    return lista_resultado