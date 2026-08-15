from cadabra2 import Ex, parent_rel_t
from scripts.get_full_index_name.get_full_index_name import get_full_index_name
from scripts.obtener_indices_libres.obtener_indices_libres import obtener_indices_libres
from scripts.mutar_nodo_indice.mutar_nodo_indice import mutar_nodo_indice
from scripts.obtener_nodo_indice.obtener_nodo_indice import obtener_nodo_indice
from scripts.mutar_indice.mutar_indice import mutar_indice

def d_c_g(ex, derivada, conexion, familia):
    """
    Expande de forma generalizada las derivadas covariantes presentes en la
    expresión `ex`, reemplazándolas por derivadas parciales y sus respectivos
    términos de conexión (símbolos de Christoffel o conexión de espín).

    Parameters
    ----------
    ex : cadabra2.Ex
        La expresión a expandir (se modifica in-place).
    derivada : str
        El nombre del operador de derivada covariante (ej. '\\nabla' o 'D').
    conexion : str
        El nombre del símbolo de conexión (ej. '\\Gamma' o '\\omega').
    familia : list of str
        Lista de nombres de índices disponibles para su uso como índices mudos.

    Returns
    -------
    cadabra2.Ex
        La expresión con las derivadas covariantes completamente expandidas.
    """
    while True:
        iterador = ex[derivada]
        try:
            derivada_node = next(iterador)
        except StopIteration:
            return ex

        derivada_ex = derivada_node.ex()
        derivada_node_copia = derivada_ex.top()

        indice_derivada = next(derivada_node_copia.indices())
        indice_derivada_nombre = str(indice_derivada.name)

        argumento = next(derivada_node_copia.args())

        indices_libres = obtener_indices_libres(argumento.ex())

        familia_disponible = familia.copy()

        indices_libres_referencia = []
        for indice, posicion in indices_libres:
            nodo_indice = next(
                nodo for nodo in argumento.ex()
                if nodo.parent_rel in (parent_rel_t.super, parent_rel_t.sub)
                and str(nodo) == indice
            )
            nombre_indice = get_full_index_name(nodo_indice)
            indices_libres_referencia.append((nombre_indice, posicion))

        for nombre_indice, posicion in indices_libres_referencia:
            # Verificación segura para evitar errores en derivadas dobles
            if nombre_indice in familia_disponible:
                familia_disponible.remove(nombre_indice)

        # Verificación segura para evitar errores en derivadas dobles
        if indice_derivada_nombre in familia_disponible:
            familia_disponible.remove(indice_derivada_nombre)

        argumento_ex = argumento.ex()
        derivada_parcial = Ex(f"\\partial_{{{indice_derivada_nombre}}}{{{argumento_ex.input_form()}}}")

        termino_conexion = Ex(r'0')

        for nombre_indice, posicion in indices_libres_referencia:
            if not familia_disponible:
                raise ValueError("No quedan índices disponibles en la familia para construir los términos de conexión.")

            indice_nuevo = familia_disponible.pop(0)

            argumento_copia = argumento.ex()
            nodo_indice = obtener_nodo_indice(argumento_copia, nombre_indice)
            mutar_nodo_indice(nodo_indice, indice_nuevo)

            t1 = argumento_copia

            if posicion == 'super':
                t2 = Ex(f"{conexion}^{{{nombre_indice}}}_{{{indice_derivada_nombre} {indice_nuevo}}}")
                signo = Ex(r'1')
            elif posicion == 'sub':
                t2 = Ex(f"{conexion}^{{{indice_nuevo}}}_{{{indice_derivada_nombre} {nombre_indice}}}")
                signo = Ex(r'-1')
            else:
                raise ValueError("Posición de índice desconocida: " + str(posicion))

            termino = signo * t2 * t1
            termino_conexion = termino_conexion + termino

        resultado = derivada_parcial + termino_conexion
        derivada_node.replace(resultado)
        familia = familia_disponible
