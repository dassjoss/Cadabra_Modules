import cadabra2
from cadabra2 import Ex
from scripts.eliminar_metricas.eliminar_metricas import eliminar_metricas_bucle


def _obtener_familia_indice(idx_name, indices_familias):
    familias_encontradas = []
    for familia, indices in indices_familias.items():
        if idx_name in indices:
            familias_encontradas.append(familia)
            
    if not familias_encontradas:
        raise RuntimeError(f"No se pudo determinar la familia del índice '{idx_name}'. El índice no aparece en ninguna familia de indices_familias.")
        
    if len(familias_encontradas) > 1:
        familias_str = ", ".join(familias_encontradas)
        raise RuntimeError(f"El índice '{idx_name}' pertenece a múltiples familias: {familias_str}. La configuración de indices_familias es ambigua.")
        
    return familias_encontradas[0]

def _obtener_factores_tensoriales(ex):
    """
    Recibe un término (Ex) y extrae sus factores tensoriales en orden.
    Ignora los factores escalares y los exponentes numéricos.
    Retorna una lista de diccionarios con la estructura de cada factor.
    """
    top = ex.top()
    factores = top.children() if top.name == r'\prod' else [top]
        
    def es_operador(n):
        own = list(n.own_indices())
        if len(own) == 0: return False
        args = list(n.args())
        if len(args) == 0: return False
        if str(args[0]).strip() == "": return False
        return True

    def extract_indices(n):
        inds = []
        if es_operador(n):
            for idx in n.own_indices():
                if idx.name != '1':
                    pos = 'abajo' if 'sub' in str(idx.parent_rel) else 'arriba'
                    inds.append((str(idx), pos))
            for arg in n.args():
                inds.extend(extract_indices(arg.ex().top()))
        else:
            if n.name == r'\prod' or n.name == r'\sum' or n.name == r'\add':
                for c in n.children():
                    if c.name != r'\comma':
                        inds.extend(extract_indices(c))
            else:
                for idx in n.indices():
                    if idx.name != '1':
                        pos = 'abajo' if 'sub' in str(idx.parent_rel) else 'arriba'
                        inds.append((str(idx), pos))
        return inds

    resultado = []
    for i_nodo, nodo in enumerate(factores):
        if nodo.name == r'\comma':
            continue
            
        indices = extract_indices(nodo)
                
        # Si tiene índices, se considera un factor tensorial
        if indices:
            resultado.append({"base": nodo.name, "indices": indices, "idx_child": i_nodo})
            
    return resultado

def _asociar_factores(term_factors, orden_factors):
    """
    Asocia factores de un término a las instrucciones del orden.
    El 'orden' es una secuencia de instrucciones de búsqueda de izquierda a derecha.
    Devuelve una lista de diccionarios:
        [{"idx_term": 0, "idx_orden": 0}, {"idx_term": 2, "idx_orden": 1}, ...]
    """
    asociaciones = []
    usados_term = set()
    
    for i_orden, f_orden in enumerate(orden_factors):
        # Búsqueda de izquierda a derecha en los factores del término
        for i_term, f_term in enumerate(term_factors):
            if i_term not in usados_term:
                if f_term["base"] == f_orden["base"] and len(f_term["indices"]) == len(f_orden["indices"]):
                    asociaciones.append({"idx_term": i_term, "idx_orden": i_orden})
                    usados_term.add(i_term)
                    break # Factor encontrado, pasamos a la siguiente instrucción de orden
                    
    return asociaciones

def _get_existing_indices(ex_completa):
    from scripts.obtener_indices_libres.obtener_indices_libres import fundamental
    usados = set()
    indices_info = fundamental(ex_completa)
    for idx_name, idx_pos in indices_info:
        usados.add(str(idx_name))
    return usados

def _generar_indice_seguro(base_name, usados):
    """
    Genera un nombre de índice que no esté en 'usados', preservando
    la raíz de símbolos LaTeX (como '\\mu') y evitando colisiones.
    """
    base_clean = ''.join([c for c in base_name if c.isalpha() or c == '\\'])
    if not base_clean:
        base_clean = "X"
        
    counter = 1
    while True:
        nuevo = f"{base_clean}_{{{counter}}}"
        if nuevo not in usados:
            usados.add(nuevo)
            return nuevo
        counter += 1

def _transformar_factor_con_metricas_fase2(ex_completa, term_node, asociaciones, orden_factors, indices_familias, metricas_map):
    term_ex = Ex(str(term_node))
    term_factors = _obtener_factores_tensoriales(term_ex)
    usados = _get_existing_indices(ex_completa)
    
    asoc_map = {a['idx_term']: a for a in asociaciones}
    reemplazos = {}
    
    n_total_movimientos = 0
    
    for i_term, f_term in enumerate(term_factors):
        if i_term not in asoc_map: continue
            
        a = asoc_map[i_term]
        f_orden = orden_factors[a['idx_orden']]
        
        cambios = []
        for j, idx_f in enumerate(f_term["indices"]):
            pos_f = idx_f[1]
            pos_o = f_orden["indices"][j][1]
            if pos_f != pos_o:
                cambios.append({"idx_idx": j, "idx_name": idx_f[0], "from_pos": pos_f, "to_pos": pos_o})
                
        if not cambios: continue
        
        n_total_movimientos += len(cambios)
            
        metricas = []
        nuevos_indices_factor = []
        
        for j, idx_f in enumerate(f_term["indices"]):
            pos_f = idx_f[1]
            cambio = next((c for c in cambios if c["idx_idx"] == j), None)
            
            if cambio:
                nuevo_idx = _generar_indice_seguro(cambio["idx_name"], usados)
                nuevos_indices_factor.append((nuevo_idx, cambio["to_pos"]))
                
                family = _obtener_familia_indice(cambio["idx_name"], indices_familias)
                
                if not metricas_map or family not in metricas_map:
                    raise RuntimeError(f"No se encontró una métrica para la familia '{family}' en metricas_map.")
                
                met_str = metricas_map[family]
                
                if cambio["from_pos"] == "arriba" and cambio["to_pos"] == "abajo":
                    metricas.append(f"{met_str}^{{{cambio['idx_name']} {nuevo_idx}}}")
                elif cambio["from_pos"] == "abajo" and cambio["to_pos"] == "arriba":
                    metricas.append(f"{met_str}_{{{cambio['idx_name']} {nuevo_idx}}}")
            else:
                nuevos_indices_factor.append((idx_f[0], pos_f))
                
        def _pos_to_syntax(idx_name, pos): return f"^{{{idx_name}}}" if pos == "arriba" else f"_{{{idx_name}}}"
            
        nuevo_factor_str = f"{f_term['base']}" + "".join([_pos_to_syntax(n, p) for n, p in nuevos_indices_factor])
        bloque_str = f"{nuevo_factor_str} {' '.join(metricas)}"
        
        reemplazos[f_term["idx_child"]] = Ex(bloque_str)
        
    nuevo_term_ex = Ex(str(term_node))
    top = nuevo_term_ex.top()
    if top.name == r'\prod':
        for i, c in enumerate(top.children()):
            if i in reemplazos:
                c.replace(reemplazos[i])
    else:
        if 0 in reemplazos:
            if top.multiplier != 1:
                nuevo_term_ex = Ex(f"{top.multiplier} {str(reemplazos[0])}")
            else:
                nuevo_term_ex = Ex(str(reemplazos[0]))
        
    return nuevo_term_ex, n_total_movimientos


def ordenar_estructura(ex, orden_str, indices_familias, metricas_map=None):
    """
    Fase 1: Análisis y matching estructural.
    Fase 2: Transformación de factores y métricas puente.
    """
    ex_copy = Ex(str(ex))
    orden_ex = Ex(orden_str)
    top_orden = orden_ex.top()
    
    # Manejar si el orden fue pasado con comas u otro formato
    if top_orden.name == r'\comma' or top_orden.name == r'\prod':
        nodos_orden = top_orden.children()
    else:
        nodos_orden = [top_orden]
        
    orden_factors = []
    for nodo in nodos_orden:
        if nodo.name == r'\comma': continue
        indices = []
        for idx in nodo.indices():
            if idx.name != '1':
                pos = 'abajo' if 'sub' in str(idx.parent_rel) else 'arriba'
                indices.append((str(idx), pos))
        if indices:
            orden_factors.append({"base": nodo.name, "indices": indices})

    top_ex = ex_copy.top()
    if top_ex.name == r'\add' or top_ex.name == r'\sum':
        terminos = []
        for term in top_ex.children():
            curr_ex = Ex(str(term))
            
            for i_ord, f_orden in enumerate(orden_factors):
                tf_s = _obtener_factores_tensoriales(curr_ex)
                if not tf_s:
                    continue
                    
                asoc_s = _asociar_factores(tf_s, orden_factors)
                asoc_actual = [a for a in asoc_s if a['idx_orden'] == i_ord]
                
                if asoc_actual:
                    res_f2, n_movs = _transformar_factor_con_metricas_fase2(
                        curr_ex, curr_ex.top(), asoc_actual, orden_factors, indices_familias, metricas_map
                    )
                    
                    if n_movs > 0:
                        curr_ex = eliminar_metricas_bucle(res_f2, n_movs)
                    else:
                        curr_ex = res_f2
                        
            terminos.append(str(curr_ex))
            
        return Ex(" + ".join(terminos))
        
    else:
        curr_ex = Ex(str(top_ex))
        
        for i_ord, f_orden in enumerate(orden_factors):
            tf_s = _obtener_factores_tensoriales(curr_ex)
            if not tf_s:
                continue
                
            asoc_s = _asociar_factores(tf_s, orden_factors)
            asoc_actual = [a for a in asoc_s if a['idx_orden'] == i_ord]
            
            if asoc_actual:
                res_f2, n_movs = _transformar_factor_con_metricas_fase2(
                    curr_ex, curr_ex.top(), asoc_actual, orden_factors, indices_familias, metricas_map
                )
                
                if n_movs > 0:
                    curr_ex = eliminar_metricas_bucle(res_f2, n_movs)
                else:
                    curr_ex = res_f2
                    
        return curr_ex
