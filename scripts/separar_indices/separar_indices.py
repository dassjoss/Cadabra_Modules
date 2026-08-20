from cadabra2 import Ex
from scripts.mutar_indice.mutar_indice import mutar_indice
from scripts.mutar_indices_dos.mutar_indice_dos import mutar_indice_dos
from scripts.obtener_indices_libres.obtener_indices_libres import obtener_indices_libres

def separar_indices(expr, algo):
    """
    Separa un índice en dos, creando una suma de dos términos nuevos.

    Toma una expresión y la duplica. En la primera copia, reemplaza 
    el índice inicial por el intermedio. En la segunda copia, reemplaza
    el índice inicial por el final. Luego suma ambas copias y reemplaza
    la expresión original in-place.

    Detecta automáticamente si el índice es libre o dummy (mudo) usando
    `obtener_indices_libres` para aplicar la mutación adecuada.

    Args:
        expr: cadabra2.Ex
            La expresión a modificar. Se modificará in-place.
        algo: str
            Cadena con el formato r'indice_inicial, indice_intermedio, indice_final'.
            Ejemplo: r'\mu, 0, i' separará \mu en sus componentes 0 y espaciales i.
            
    Returns:
        None
    """
    # 1. Parsear el string 'algo'
    partes = [idx.strip() for idx in algo.split(',')]
    if len(partes) != 3:
        raise ValueError("El argumento 'algo' debe contener exactamente 3 índices separados por comas.")
    
    indice_inicial = partes[0]
    indice_intermedio = partes[1]
    indice_final = partes[2]
    
    # 2. Crear dos copias separadas e independientes de la expresión original
    # Es necesario llamar a .top() para obtener el ExNode raíz, el cual posee el método .ex()
    t1 = expr.top().ex()
    t2 = expr.top().ex()

    # 3. Determinar si es índice libre o dummy
    indices_libres = obtener_indices_libres(expr)
    # obtener_indices_libres retorna una lista de tuplas (nombre, posicion)
    nombres_libres = [idx[0] for idx in indices_libres]

    es_libre = indice_inicial in nombres_libres

    # 4. Mutar las copias
    if es_libre:
        # Si es libre, mutamos solo la única ocurrencia
        mutar_indice(t1, indice_inicial, indice_intermedio)
        mutar_indice(t2, indice_inicial, indice_final)
    else:
        # Si es dummy, mutamos las dos ocurrencias de la contracción
        mutar_indice_dos(t1, indice_inicial, indice_intermedio)
        mutar_indice_dos(t2, indice_inicial, indice_final)
    
    
    # 5. Sumar t1 + t2
    nueva_expr = t1 + t2
    print(nueva_expr)
    
    # 6. Reemplazar la expresión original con la nueva suma in-place
    expr.top().replace(nueva_expr)

    