import cadabra2
from cadabra2 import Ex
from scripts.eliminar_metricas.eliminar_metricas import eliminar_metricas_bucle


def _obtener_familia_indice(idx_name, indices_familias):
    """
    Identifica la familia matemática a la que pertenece un índice específico.

    Esta función busca en un diccionario de definiciones de familias y retorna
    el nombre de la familia que contiene el índice proporcionado. Garantiza
    que el índice exista y pertenezca a una única familia, levantando errores
    si el índice es desconocido o ambiguo.

    Parameters
    ----------
    idx_name : str
        El nombre del índice que se desea buscar (ej. 'a', '\\mu', 'f_{1}').
    indices_familias : dict of list
        Diccionario que mapea los nombres de las familias con listas de índices
        que pertenecen a dichas familias. Ej: {'lorentz': ['a', 'b', 'c']}.

    Returns
    -------
    str
        El nombre de la familia (ej. 'lorentz', 'spacetime') a la que pertenece
        el índice indicado.
    """
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
    Extrae los factores tensoriales individuales contenidos en un término (Ex).

    Analiza la estructura del término y descompone los factores tensoriales
    en el orden en el que aparecen, extrayendo los índices matemáticos de cada uno
    junto con su posición (arriba o abajo). Esta función tiene la capacidad de 
    recorrer operadores matemáticos de forma recursiva (como las derivadas
    parciales o covariantes) para extraer correctamente los índices de sus argumentos
    y de sí mismos, ignorando coeficientes numéricos y factores escalares.

    Parameters
    ----------
    ex : cadabra2.Ex
        Término individual de Cadabra del que se extraerán los factores.

    Returns
    -------
    list of dict
        Lista donde cada elemento representa un factor tensorial encontrado, 
        conteniendo diccionarios con la siguiente estructura:
        - "base" (str): Nombre base del factor (ej. 'P', '\\partial').
        - "indices" (list of tuple): Lista de tuplas (nombre_indice, posicion).
        - "idx_child" (int): Índice original del factor dentro del término.
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
    Relaciona los factores tensoriales encontrados en un término con las
    instrucciones de ordenamiento deseadas por el usuario.

    Ejecuta una búsqueda de izquierda a derecha en los factores del término
    para hacer "matching" con las instrucciones de `orden_factors`. Para que
    exista una coincidencia, el nombre base del factor y la cantidad de índices
    deben coincidir. Cada instrucción del orden se asocia con el primer factor 
    disponible que coincida estructuralmente.

    Parameters
    ----------
    term_factors : list of dict
        Factores extraídos del término actual (generados por `_obtener_factores_tensoriales`).
    orden_factors : list of dict
        Plantillas de factores tensoriales que dictan la estructura deseada.

    Returns
    -------
    list of dict
        Lista de asociaciones donde cada elemento relaciona un factor del término
        con una instrucción del orden:
        - "idx_term" (int): Índice del factor dentro del término actual.
        - "idx_orden" (int): Índice de la plantilla en el orden especificado.
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
    """
    Obtiene todos los nombres de los índices ya utilizados en la expresión completa.

    Esta función permite identificar todos los índices ocupados para evitar 
    futuras colisiones cuando se necesite inyectar métricas puente o generar
    índices auxiliares.

    Parameters
    ----------
    ex_completa : cadabra2.Ex
        Expresión completa (o término) del que se extraerán los índices en uso.

    Returns
    -------
    set of str
        Un conjunto (set) de los nombres de los índices que ya existen en la expresión.
    """
    from scripts.obtener_indices_libres.obtener_indices_libres import fundamental
    usados = set()
    indices_info = fundamental(ex_completa)
    for idx_name, idx_pos in indices_info:
        usados.add(str(idx_name))
    return usados

def _generar_indice_seguro(base_name, usados):
    """
    Genera de forma dinámica un nombre de índice auxiliar que no colisione
    con los índices previamente utilizados, conservando su familia semántica.

    Crea un nuevo índice añadiéndole un subíndice numérico a su nombre base
    (ej. 'f' -> 'f_{1}', '\\mu' -> '\\mu_{1}'). Al preservar el nombre base
    exacto, incluyendo las barras invertidas de raíces LaTeX, el motor de 
    Cadabra deduce inherentemente que el índice auxiliar pertenece a la misma
    familia (lorentz, spacetime, etc.) que el índice original sin necesidad
    de que sea declarado explícitamente. Adicionalmente, el nuevo índice
    es registrado en la lista de índices 'usados' para evitar re-colisiones
    subsecuentes.

    Parameters
    ----------
    base_name : str
        Nombre original del índice del cual se desea derivar un auxiliar.
    usados : set of str
        Conjunto de los índices actualmente utilizados en la expresión.

    Returns
    -------
    str
        Nombre generado de un índice auxiliar 100% seguro contra colisiones.
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
    """
    Modifica posicionalmente los índices de un factor e inyecta métricas puente.

    Para las asociaciones detectadas, analiza si un índice del término actual 
    difiere posicionalmente (subíndice vs superíndice) respecto al requerimiento
    de orden especificado. Si existe una diferencia:
    1. Genera un índice auxiliar seguro con `_generar_indice_seguro()`.
    2. Cambia la posición del índice original en el factor por el índice auxiliar.
    3. Construye e inyecta la métrica adecuada de acuerdo a la familia del índice
       para realizar el "levantamiento" o "bajada" algebraica del mismo.

    Acumula estas operaciones, reconstruye el término con todas sus métricas 
    puente insertadas al final de la expresión y devuelve la expresión mutada
    junto con la cantidad de movimientos realizados. 

    Parameters
    ----------
    ex_completa : cadabra2.Ex
        La expresión algebraica completa (usada para evitar colisiones de índices).
    term_node : cadabra2.Ex
        Nodo del término local que será transformado.
    asociaciones : list of dict
        Relación entre los factores del término local y la estructura objetivo.
    orden_factors : list of dict
        Estructura tensorial meta (plantillas extraídas del `orden_str`).
    indices_familias : dict of list
        Declaraciones de familias para determinar la métrica puente a aplicar.
    metricas_map : dict of str
        Mapa que vincula el nombre de cada familia con su métrica matemática (ej. 'lorentz': '\\eta').

    Returns
    -------
    tuple (cadabra2.Ex, int)
        Retorna el nuevo término de Cadabra conteniendo el factor transformado
        y todas las métricas inyectadas, acompañado por el número entero total
        de movimientos tensoriales (inyecciones) requeridos.
    """
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
    Rearregla y organiza la estructura tensorial de una expresión de Cadabra
    basándose en un orden secuencial arbitrario definido por el usuario.

    Esta es la función principal del módulo. Coordina internamente tres etapas
    conceptuales de manera estricta y secuencial por factor:
    - Análisis (Fase 1): Extrae y asocia cada factor tensorial del término
      con las instrucciones deseadas por el usuario en `orden_str`.
    - Transformación (Fase 2): Modifica las posiciones de los índices 
      inyectando métricas puente a un solo factor a la vez.
    - Eliminación (Fase 3): Contrae matemáticamente las métricas inyectadas
      inmediatamente después del procesamiento de dicho factor usando
      `eliminar_metricas_bucle()`.

    Al operar secuencialmente de izquierda a derecha (procesar y eliminar
    métricas de cada factor individual antes de pasar al siguiente), la 
    arquitectura elude la interacción cruzada de tensores de Kronecker 
    residuales, manteniendo una manipulación matemática limpia y purista.

    Parameters
    ----------
    ex : cadabra2.Ex
        La expresión de Cadabra a ordenar matemáticamente.
    orden_str : str
        Plantilla estructural a igualar en formato cadena (ej. 'P^{a}_{b c} \\epsilon_{d e f h}').
    indices_familias : dict of list
        Declaraciones de configuración donde las claves son familias y los valores las listas de índices.
    metricas_map : dict of str, optional
        Mapeo de la familia de un índice a su símbolo métrico fundamental (ej. {'lorentz': '\\eta'}).

    Returns
    -------
    cadabra2.Ex
        Una nueva expresión de Cadabra matemáticamente equivalente donde los
        factores tensoriales y sus posiciones indiciales obedecen estrictamente
        al formato indicado en `orden_str`.
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
