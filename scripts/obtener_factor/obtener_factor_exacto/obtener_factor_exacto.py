from cadabra2 import Ex

def obtener_factor_exacto(expr, termino):
    """
    Extrae el factor que multiplica a un conjunto de factores exactos.
    A diferencia de obtener_factor_multiplicativo, esta función no admite comodines,
    pero es capaz de borrar múltiples componentes (como e^{c}_{\\lambda} y e^{d}_{\\rho})
    sin generar conflictos de índices ni dejar unos ('1') residuales.
    
    Args:
        expr: cadabra2.Ex
            Expresión de la que se extraerá el factor.
        termino: cadabra2.Ex
            El factor o producto exacto de factores a eliminar.
            
    Returns:
        cadabra2.Ex
            La expresión con los factores borrados limpiamente.
    """
    if expr.top().name != r'\prod':
        raise ValueError("La expresión de entrada debe ser un producto para extraer su factor.")
        
    ex_copia = Ex(str(expr.input_form()))
    
    if termino.top().name == r'\prod':
        factores_a_borrar = [str(f.ex().input_form()).strip() for f in termino.top().children()]
    else:
        factores_a_borrar = [str(termino.input_form()).strip()]
        
    if ex_copia.top().name == r'\prod':
        for factor_borrar in factores_a_borrar:
            encontrado = False
            for factor_original in ex_copia.top().children():
                if factor_borrar == str(factor_original.ex().input_form()).strip():
                    factor_original.erase()
                    encontrado = True
                    break 
            if not encontrado:
                raise ValueError(f"No se encontró el factor exacto '{factor_borrar}' en la expresión.")
    else:
        if str(expr.input_form()).strip() == str(termino.input_form()).strip():
            return Ex("1")
        else:
            raise ValueError("La expresión no coincide con el término buscado.")

    return ex_copia
