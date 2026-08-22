from cadabra2 import Ex, substitute

def obtener_factor_multiplicativo(expr, termino):
    """
    Extrae el factor que multiplica a un 'termino' específico dentro de un producto.
    
    Args:
        expr: Expresión completa (debe ser un producto).
        termino: El término o conjunto de términos (producto parcial) que queremos aislar.
                 
    Returns:
        El factor multiplicativo restante (lo que sobra al quitar 'termino').
        
    Raises:
        Exception: Si el término no se encuentra en la expresión.
    """
    if expr.top().name != r'\prod':
        raise ValueError("La expresión de entrada debe ser un producto para extraer su factor.")
        
    # 1. Comprobar existencia usando una MARCA
    ex_check = Ex(str(expr.input_form()))
    substitute(ex_check, Ex(r"@(termino) -> MARCA{1}"))
    
    encontrado = False
    for nodo in ex_check:
        if nodo.name == 'MARCA':
            encontrado = True
            break
            
    if not encontrado:
        raise Exception(f'No se encontró el termino {termino.input_form()} en la expresión')
        
    # 2. Si existe, extraer el factor multiplicativo reemplazando el término por 1
    # Esto preserva escalares (ej. 1/2), tensores y derivadas que no forman parte del término.
    ex_factor = Ex(str(expr.input_form()))
    substitute(ex_factor, Ex(r"@(termino) -> 1"))
    
    return ex_factor