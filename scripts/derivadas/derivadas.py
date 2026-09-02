from cadabra2 import Ex, parent_rel_t
from scripts.get_full_index_name.get_full_index_name import get_full_index_name
from scripts.obtener_indices_libres.obtener_indices_libres import obtener_indices_libres, fundamental
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
    top_name = ex.top().name
    es_suma = (top_name == r'\sum')

    if es_suma:
        sumandos = [s.ex() for s in ex.top().args()]
    else:
        sumandos = [Ex(str(ex))]

    for sumando in sumandos:
        indices_ocupados = set(idx[0] for idx in fundamental(sumando))
        familia_disponible = [f for f in familia if f not in indices_ocupados]

        while True:
            try:
                derivada_node = next(sumando[derivada])
            except StopIteration:
                break

            derivada_node_copia = derivada_node.ex().top()
            argumento = next(derivada_node_copia.args())

            indices_libres = obtener_indices_libres(argumento.ex())

            indices_libres_referencia = []
            for indice, posicion in indices_libres:
                nodo_indice = next(
                    nodo for nodo in argumento.ex()
                    if nodo.parent_rel in (parent_rel_t.super, parent_rel_t.sub)
                    and str(nodo) == indice
                )
                nombre_indice = get_full_index_name(nodo_indice)
                indices_libres_referencia.append((nombre_indice, posicion))

            indice_derivada = next(derivada_node_copia.indices())
            indice_derivada_nombre = str(indice_derivada.name)
            
            argumento_ex = argumento.ex()
            derivada_parcial = Ex(f"\\partial_{{{indice_derivada_nombre}}}{{{argumento_ex.input_form()}}}")

            termino_conexion = Ex(r'0')

            for nombre_indice, posicion in indices_libres_referencia:
                if nombre_indice not in familia:
                    continue
                if not familia_disponible:
                    raise ValueError(
                        "No quedan índices disponibles en la familia para construir "
                        "los términos de conexión."
                    )

                indice_nuevo = familia_disponible.pop(0)

                argumento_copia = argumento.ex()
                nodo_indice = obtener_nodo_indice(argumento_copia, nombre_indice)
                mutar_nodo_indice(nodo_indice, indice_nuevo)

                t1 = argumento_copia

                if posicion == 'super':
                    t2 = Ex(f"{conexion}_{{{indice_derivada_nombre} {indice_nuevo}}}^{{{nombre_indice}}}")
                    signo = Ex(r'1')
                elif posicion == 'sub':
                    t2 = Ex(f"{conexion}_{{{indice_derivada_nombre} {nombre_indice}}}^{{{indice_nuevo}}}")
                    signo = Ex(r'-1')
                else:
                    raise ValueError("Posición de índice desconocida: " + str(posicion))

                termino = signo * t2 * t1
                termino_conexion = termino_conexion + termino

            resultado = derivada_parcial + termino_conexion
            derivada_node.replace(resultado)

    if es_suma:
        suma_total = Ex(r"0")
        for s in sumandos:
            suma_total = suma_total + s
    else:
        suma_total = sumandos[0]

    root_it = next(ex[top_name])
    root_it.replace(suma_total)

    return ex
