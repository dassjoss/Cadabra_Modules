from cadabra2 import Ex
from scripts.mutar_indices_multiples.mutar_indices_multiples import mutar_indices_multiples
import itertools

def get_parity(p):
    """Devuelve 1 si la permutación p es par, -1 si es impar."""
    n = len(p)
    visited = [False] * n
    swaps = 0
    for i in range(n):
        if not visited[i]:
            j = i
            cycle_len = 0
            while not visited[j]:
                visited[j] = True
                j = p[j]
                cycle_len += 1
            if cycle_len > 1:
                swaps += cycle_len - 1
    return 1 if swaps % 2 == 0 else -1

def shouten_indices(expr, indices):
    """
    Aplica la identidad de Schouten sobre una expresión en Cadabra, expandiendo
    un término mediante TODAS las n! permutaciones de los índices especificados.

    La identidad de Schouten establece que antisimetrizar n índices da cero:
    [x1, x2, ..., xn] = 0
    Por lo tanto: T_{x1...xn} = - \sum_{\pi \neq id} sgn(\pi) T_{\pi(x1)...\pi(xn)}

    Esta función devuelve la suma de todas las permutaciones (OMITIENDO la original),
    multiplicadas por -sgn(pi) para reemplazar matemáticamente el término original.

    Args:
        expr: cadabra2.Ex
            Expresión de Cadabra sobre la cual aplicar la identidad.
        indices: str
            Cadena con los índices involucrados en la identidad, separados por comas.
            Ejemplo: r'a, b, c, d'

    Returns:
        cadabra2.Ex
            Una nueva expresión de Cadabra correspondiente al lado derecho de la identidad.
    """
    lista_indices = [idx.strip() for idx in indices.split(',')]
    n = len(lista_indices)
    
    # Generar todas las permutaciones de las posiciones (0..n-1)
    indices_originales = list(range(n))
    permutaciones = list(itertools.permutations(indices_originales))
    
    resultado = Ex(r'0')
    
    for p in permutaciones:
        if list(p) == indices_originales:
            continue # Omitir la permutación identidad (el término original)
            
        signo = get_parity(list(p))
        # Como T_id + sum(sgn * T_pi) = 0 => T_id = sum(-sgn * T_pi)
        signo_final = -signo
        
        copia = expr.top().ex()
        
        # Para hacer las mutaciones simultáneas de forma segura,
        # primero pasamos todos los índices a nombres temporales.
        # Usamos repetido=True para mutar ambas ocurrencias si son índices mudos.
        nombres_temp = [f"ZTEMPZ{i}" for i in range(n)]
        for idx_orig, temp in zip(lista_indices, nombres_temp):
            mutar_indices_multiples(copia, idx_orig, temp)
            
        # Ahora pasamos de los nombres temporales a los índices permutados
        for i, idx_dest_pos in enumerate(p):
            idx_dest_name = lista_indices[idx_dest_pos]
            mutar_indices_multiples(copia, nombres_temp[i], idx_dest_name)
            
        signo_ex = Ex(str(signo_final))
        termino = signo_ex * copia
        resultado = resultado + termino

    return resultado