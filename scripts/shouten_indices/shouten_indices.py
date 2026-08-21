from cadabra2 import Ex
from scripts.mutar_indices_multiples.mutar_indices_multiples import mutar_indices_multiples

def shouten_indices(expr, indices, indice_intercambio):
    """
    Aplica la identidad de Schouten sobre una expresión en Cadabra, expandiendo
    un tensor antisimétrico mediante el intercambio secuencial de uno de sus
    índices con el resto de los índices especificados.

    La identidad de Schouten en un espacio de dimensión n-1 establece que
    antisimetrizar n índices da cero: [x1, x2, ..., xn] = 0.
    Esta función aísla el `indice_intercambio` y lo expande como una suma
    de permutaciones con los demás índices del conjunto, respetando los
    signos correspondientes a las transposiciones.

    Args:
        expr: cadabra2.Ex
            Expresión de Cadabra sobre la cual aplicar la identidad.
        indices: str
            Cadena con los índices involucrados en la identidad, separados por comas.
            Ejemplo: r'\\alpha, \\beta, a, b'
        indice_intercambio: str
            El índice que será intercambiado secuencialmente. Debe pertenecer al
            conjunto definido en `indices`.

    Returns:
        cadabra2.Ex
            Una nueva expresión de Cadabra correspondiente a la expansión de Schouten.

    Raises:
        ValueError:
            Si `indice_intercambio` no se encuentra en el conjunto `indices`.
    """
    lista_indices = [idx.strip() for idx in indices.split(',')]
    
    if indice_intercambio not in lista_indices:
        raise ValueError(f"El índice '{indice_intercambio}' no está en la lista de índices proporcionada.")
    
    k_0 = lista_indices.index(indice_intercambio)
    k = k_0 + 1
    
    signos = []
    conjuntos_mutados = []
    
    signo_secuencia = -1
    
    for i in range(len(lista_indices)):
        if i == k_0:
            continue
            
        signo_final = -signo_secuencia if (k % 2 == 0) else signo_secuencia
        signos.append(signo_final)
        
        signo_secuencia *= -1
        
        nuevo_conjunto = lista_indices.copy()
        nuevo_conjunto[k_0], nuevo_conjunto[i] = nuevo_conjunto[i], nuevo_conjunto[k_0]
        
        conjuntos_mutados.append(", ".join(nuevo_conjunto))

    resultado = Ex(r'0')

    indices_a_intercambiar = []
    for j in range(len(lista_indices)):
        if j == k_0: continue
        indices_a_intercambiar.append(lista_indices[j])

    for signo_int, idx_i in zip(signos, indices_a_intercambiar):
        copia = expr.top().ex()
        
        idx_k = lista_indices[k_0]
        temp_name = "ZTEMPZ"
        
        mutar_indices_multiples(copia, idx_k, temp_name)
        mutar_indices_multiples(copia, idx_i, idx_k)
        mutar_indices_multiples(copia, temp_name, idx_i)
        
        signo_ex = Ex(str(signo_int))
        termino = signo_ex * copia
        resultado = resultado + termino

    return resultado