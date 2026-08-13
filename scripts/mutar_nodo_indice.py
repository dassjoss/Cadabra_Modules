from cadabra2 import Ex, parent_rel_t


def mutar_nodo_indice(nodo, nombre_nuevo):
    """
    Muta estructuralmente un nodo de índice libre, modificando el
    propio ExNode (in-place) y conservando su identidad Python.

    ENTRADA
    -------
    nodo : cadabra2.ExNode
        Nodo que representa el índice que se desea modificar.

        Puede ser un índice simple, por ejemplo:
            α
            β
            λ

        o un índice con subíndice numérico:
            λ_{1}
            λ_{25}
            α_{100}

    nombre_nuevo : str
        Representación textual del nuevo índice.

        Ejemplos válidos comprobados:
            r'\alpha'
            r'\beta'
            r'\lambda_{1}'
            r'\lambda_{4}'
            r'\alpha_{2}'
            r'\lambda_{25}'
            r'\alpha_{100}

    OPERACIÓN
    ---------
    1. Construye temporalmente el índice destino mediante Ex().
    2. Obtiene su nombre principal y sus hijos.
    3. Elimina los hijos del índice original.
    4. Cambia el nombre principal del nodo original.
    5. Si el destino posee un subíndice, construye un nuevo ExNode
       para dicho subíndice.
    6. Establece parent_rel_t.sub en el nuevo hijo.
    7. Inserta el nuevo hijo en el nodo original.

    La mutación se realiza IN-PLACE.

    SALIDA
    ------
    cadabra2.ExNode
        Devuelve el mismo objeto `nodo` que recibió como entrada,
        después de haber sido modificado.

        Por tanto:
            resultado is nodo
        debe ser True.

    COMPORTAMIENTO COMPROBADO
    -------------------------
    Índices simples:
        α -> β
        β -> α

    Cambio de subíndice:
        λ_{1} -> λ_{4}
        λ_{4} -> λ_{1}

    Eliminación de subíndice:
        λ_{1} -> α

    Adición de subíndice:
        α -> λ_{1}

    Cambio simultáneo de nombre y subíndice:
        λ_{1} -> α_{2}
        α_{1} -> β_{2}
        α_{10} -> λ_{25}
        λ_{100} -> α_{7}

    LIMITACIONES
    ------------
    - Está diseñada para mutar nodos de índices, no nodos arbitrarios
      del árbol de Cadabra.
    - El destino debe poder construirse mediante Ex(nombre_nuevo).
    - Actualmente solo admite destinos con cero o un hijo.
    - Si el destino tiene más de un hijo, se produce ValueError.
    - Para subíndices numéricos, el valor debe obtenerse mediante
      str(hijo), ya que el nodo numérico puede tener name == '1'
      independientemente de su valor real.
    - El nuevo hijo se fuerza estructuralmente a parent_rel_t.sub.
    - La función no verifica por sí misma que el nodo recibido sea
      realmente un índice libre; esa validación corresponde al código
      que la utiliza.

    IDENTIDAD
    ---------
    La función modifica el nodo existente en lugar de crear un nodo
    de reemplazo. Las pruebas verificaron que:

        id(nodo) antes == id(nodo) después == id(resultado)

    Por tanto, la identidad del ExNode se conserva.
    """
    # ========================================================
    # 1. Construir temporalmente el indice destino
    # ========================================================

    nuevo_ex = Ex(nombre_nuevo)

    nuevo_nodo = None

    for candidato in nuevo_ex:
        nuevo_nodo = candidato
        break

    if nuevo_nodo is None:
        raise RuntimeError(
            f"No se pudo construir el indice destino: {nombre_nuevo}"
        )

    # ========================================================
    # 2. Obtener la estructura del indice destino
    # ========================================================

    nuevo_nombre = nuevo_nodo.name
    nuevos_hijos = list(nuevo_nodo.children())

    if len(nuevos_hijos) > 1:
        raise ValueError(
            f"El indice destino tiene mas de un hijo: {nombre_nuevo}"
        )

    # ========================================================
    # 3. Eliminar los hijos actuales del indice original
    # ========================================================

    hijos_actuales = list(nodo.children())

    for hijo in hijos_actuales:
        hijo.erase()

    # ========================================================
    # 4. Cambiar el nombre principal
    # ========================================================

    nodo.name = nuevo_nombre

    # ========================================================
    # 5. Reconstruir el subindice si existe
    # ========================================================

    if len(nuevos_hijos) == 1:

        hijo_destino = nuevos_hijos[0]

        # ----------------------------------------------------
        # Crear un Ex temporal para obtener un ExNode nuevo
        # ----------------------------------------------------

        # str(hijo_destino) da la representacion real ('4', '2', etc.).
        # hijo_destino.name NO sirve para nodos numericos: para todos
        # ellos vale siempre '1'; el valor real vive en .multiplier.
        hijo_ex = Ex(str(hijo_destino))

        hijo_nuevo = None

        for candidato in hijo_ex:
            hijo_nuevo = candidato
            break

        if hijo_nuevo is None:
            raise RuntimeError(
                f"No se pudo construir el subindice de {nombre_nuevo}"
            )

        # ----------------------------------------------------
        # El hijo debe ser estructuralmente un subindice
        # ----------------------------------------------------

        hijo_nuevo.parent_rel = parent_rel_t.sub

        # ----------------------------------------------------
        # Insertarlo en el nodo original
        # ----------------------------------------------------

        nodo.append_child(hijo_nuevo)

    return nodo
