from cadabra2 import Ex


def obtener_indices_libres(expr):
    """
    Obtiene los índices libres de una expresión de Cadabra.

    PARÁMETRO DE ENTRADA
    --------------------
    expr : cadabra2.Ex
        Expresión de Cadabra sobre la cual se desean identificar
        los índices libres.

        La función requiere que 'expr' posea el método:
            expr.top()

        Por tanto, la entrada esperada es un objeto cadabra2.Ex
        (o un objeto compatible que proporcione .top()).


    OPERACIÓN
    ---------
    La identificación de los índices libres se delega en la API
    nativa de Cadabra mediante:

        expr.top().free_indices()

    Primero se obtiene el nodo superior de la expresión mediante
    expr.top(). Luego free_indices() identifica los índices que
    Cadabra considera libres.

    Los elementos producidos por free_indices() se materializan
    individualmente mediante:

        Ex(str(indice))

    y posteriormente se obtiene el ExNode correspondiente a cada
    expresión temporal.

    Esta materialización es necesaria porque los objetos ExNode
    producidos directamente durante la iteración de free_indices()
    se comportan como cursores mutables del iterador interno de
    Cadabra.

    Por ejemplo, al recorrer:

        A^{alpha beta}

    puede observarse que el mismo objeto Python utilizado por el
    iterador cambia de:

        alpha
        beta

    Por tanto, conservar directamente referencias a los elementos
    producidos por free_indices() puede provocar que varias
    referencias terminen mostrando el último elemento visitado.

    La materialización mediante:

        Ex(str(indice))

    crea una expresión independiente y permite obtener un ExNode
    independiente para cada índice.


    SALIDA
    ------
    list[cadabra2.ExNode]

        La función devuelve una lista Python cuyos elementos son
        ExNode independientes.

        Cada elemento de la lista representa uno de los índices
        libres identificados originalmente por Cadabra.

        La lista permite recorrer los índices mediante:

            for indice in obtener_indices_libres(expr):
                ...

        Los ExNode contenidos en la lista no son referencias al
        cursor interno de free_indices(). Cada uno ha sido
        materializado independientemente mediante:

            Ex(str(indice))

        Por tanto, los elementos de la lista conservan su identidad
        y representación de forma independiente entre sí.

        IMPORTANTE:
        El tipo de cada elemento continúa siendo cadabra2.ExNode.
        Lo que cambia respecto a la implementación original es el
        contenedor que los agrupa: anteriormente se retornaba
        directamente el ExNode utilizado como iterador por
        free_indices(); actualmente se devuelve una lista Python
        de ExNode independientes.


    EJEMPLOS
    --------
    Para:

        expr = Ex(r'A^{\alpha\beta}')

    Cadabra reconoce:

        \alpha, \beta

    como índices libres.

    El resultado tiene conceptualmente la forma:

        [
            ExNode(\alpha),
            ExNode(\beta)
        ]

    Para:

        expr = Ex(r'A^{\alpha}B_{\alpha}')

    el índice \alpha está contraído, por lo que no aparece como
    índice libre.

    El resultado es una lista vacía:

        []

    Para:

        expr = Ex(r'A^{\alpha}B^{\beta}')

    los índices libres son:

        \alpha, \beta


    LIMITACIONES
    ------------
    1. La función no acepta directamente una cadena de texto.

       Esto:

           obtener_indices_libres(r'\alpha')

       produce un AttributeError porque un str no posee
       el método .top().

       Debe construirse primero:

           expr = Ex(r'\alpha')
           obtener_indices_libres(expr)


    2. La función no implementa un algoritmo independiente para
       determinar qué índices son libres.

       La determinación de qué índices son libres continúa
       dependiendo de:

           expr.top().free_indices()

       de Cadabra.

       Esta función únicamente materializa de forma independiente
       los índices identificados por Cadabra.


    3. El resultado depende de la implementación de
       free_indices() de Cadabra.

       La función no calcula independientemente:

           - contracciones
           - índices dummy
           - simetrías
           - equivalencia entre índices
           - compatibilidad de índices entre términos


    4. Los índices contraídos no se consideran índices libres
       por free_indices() y, por tanto, no deberían aparecer
       en el resultado.


    5. La función no modifica la expresión original.

       Las expresiones temporales utilizadas para materializar
       los índices son independientes de la expresión original.


    6. La función no cambia los nombres, posiciones, orientación
       (super/subíndice) ni estructura de los índices reconocidos
       por Cadabra.

       La representación textual utilizada para materializar
       cada índice es:

           str(indice)

       Por tanto, para índices como:

           \lambda_1
           \lambda_4

       se conserva correctamente el valor del subíndice.


    7. Para índices con subíndices numéricos no debe utilizarse
       únicamente:

           indice.name

       para reconstruir el índice.

       Cadabra puede representar internamente distintos valores
       numéricos con el mismo name. Por ejemplo, el valor real del
       subíndice puede estar representado mediante la estructura
       interna y su multiplier.

       Por esta razón se utiliza:

           str(indice)

       para materializar el índice completo.


    8. En expresiones con estructuras anidadas, como:

           \nabla_{\mu}(A^{\alpha\beta})

       la identificación de índices libres continúa siendo
       realizada por Cadabra mediante free_indices().

       Esta función no sustituye el algoritmo de Cadabra para
       determinar la libertad del índice.


    9. Una expresión sin índices puede devolver una lista vacía
       según el comportamiento de free_indices() de Cadabra.


    10. Las expresiones deben ser sintácticamente válidas para
        Cadabra.

        Por ejemplo, una suma cuyos términos tengan conjuntos
        incompatibles de índices libres puede producir un error
        al construir el Ex antes de ejecutar esta función.


    11. La función no debe confundirse con get_full_index_name().

        obtener_indices_libres() determina y materializa los
        índices libres.

        get_full_index_name() reconstruye posteriormente el
        nombre completo de un ExNode.


    COMPORTAMIENTO OBSERVADO EN LAS PRUEBAS
    ---------------------------------------
    Tipo de entrada:

        cadabra2.Ex


    Tipo del objeto retornado directamente por:

        expr.top().free_indices()

    observado:

        cadabra2.ExNode


    Se comprobó que dicho ExNode funciona como un iterador/cursor.
    Durante la iteración pueden producirse referencias Python que
    no son independientes entre sí.

    Por ejemplo, al recorrer:

        A^{\alpha\beta}

    se observó:

        iteración 0 -> \alpha
        iteración 1 -> \beta

    pero las referencias guardadas directamente desde el iterador
    podían terminar mostrando el último índice visitado.

    Por esta razón, el resultado de free_indices() no se conserva
    directamente.


    MATERIALIZACIÓN COMPROBADA
    --------------------------
    Para cada índice obtenido del iterador se realiza:

        indice_ex = Ex(str(indice))

    y posteriormente:

        for candidato in indice_ex:
            indice_materializado = candidato
            break

    Los ExNode materializados se almacenan en una lista Python.

    Las pruebas demostraron que los ExNode materializados:

        \alpha
        \beta

    poseen identidades Python independientes.

    Se comprobó:

        indice_0 is indice_1
        -> False

    y:

        id(indice_0) == id(indice_1)
        -> False

    Además, después de terminar la iteración original, ambos
    objetos conservaron correctamente sus respectivos valores.


    INDICES CON SUBINDICES NUMERICOS
    --------------------------------
    También se comprobó la materialización independiente de:

        \lambda_1
        \lambda_4

    conservando correctamente:

        \lambda_1 -> \lambda_1
        \lambda_4 -> \lambda_4

    Por tanto, la materialización mediante:

        Ex(str(indice))

    conserva correctamente la representación textual completa
    del índice.


    COMPATIBILIDAD CON get_full_index_name()
    ----------------------------------------
    Los ExNode almacenados en la lista pueden ser procesados
    directamente por:

        get_full_index_name()

    obteniendo correctamente:

        \alpha
        \beta
        \lambda_1
        \lambda_4

    según corresponda.


    EJEMPLO DE RECORRIDO
    --------------------
    El resultado puede consumirse mediante iteración:

        resultado = obtener_indices_libres(expr)

        for indice in resultado:
            print(indice)

    Cada 'indice' obtenido en el recorrido es un
    cadabra2.ExNode independiente.

    También puede accederse individualmente:

        resultado[0]
        resultado[1]

    siempre que existan suficientes índices libres.


    COMPATIBILIDAD CON LAS UTILIDADES EXISTENTES
    ---------------------------------------------
    La función forma parte de una cadena de utilidades:

        obtener_indices_libres()
                |
                v
        get_full_index_name()
                |
                v
        obtener_nodo_indice()
                |
                v
        mutar_nodo_indice()

    La modificación introducida en esta función afecta únicamente
    a la forma en que los índices obtenidos de free_indices() son
    materializados y almacenados.

    Los elementos individuales continúan siendo:

        cadabra2.ExNode

    por lo que las funciones que trabajan sobre un índice individual
    pueden continuar recibiendo ExNode.

    En particular, no se modifica la interfaz de:

        get_full_index_name()
        mutar_nodo_indice()
        mutar_indice()

    La única diferencia relevante es que el conjunto de índices
    libres ya no es el cursor ExNode retornado directamente por
    free_indices(), sino una lista Python de ExNode independientes.


    RESUMEN
    -------
    Entrada:

        cadabra2.Ex


    Identificación:

        expr.top().free_indices()


    Materialización de cada índice:

        Ex(str(indice))


    Elemento de salida:

        cadabra2.ExNode independiente


    Contenedor de salida:

        list


    Objetivo:

        Obtener representaciones independientes de cada índice
        libre, evitando conservar referencias dependientes del
        cursor interno de free_indices().


    PRINCIPIO FUNDAMENTAL
    ---------------------
    Los índices de Cadabra deben tratarse como estructuras de
    árbol y no simplemente como cadenas de texto.

    Sin embargo, para romper la dependencia con el cursor de
    free_indices(), se utiliza temporalmente:

        Ex(str(indice))

    para reconstruir cada índice completo.

    Esto permite conservar correctamente estructuras como:

        \alpha
        \beta
        \lambda_1
        \lambda_4

    sin depender de la posición que ocupa el cursor interno del
    iterador de free_indices().
    """

    indices_originales = expr.top().free_indices()

    indices_materializados = []

    for indice in indices_originales:

        indice_ex = Ex(str(indice))

        indice_materializado = None

        for candidato in indice_ex:
            indice_materializado = candidato
            break

        if indice_materializado is None:
            raise RuntimeError(
                f"No se pudo materializar el índice libre: {indice}"
            )

        indices_materializados.append(indice_materializado)

    return indices_materializados
