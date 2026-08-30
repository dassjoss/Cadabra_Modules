def ordenar_estructura(ex,orden):




    """
    Función para ordenar términos en Cadabra de forma ordenada.
    se dará un .ex, que se espera sea una suma o un solo termino. 
    Ordenará sobre cada uno de los eleentos según el orden que se imponga en orden
    y devolverá el resultado como un .ex
    """

    """
    En muchas ocasiones al hacer canonicalise se desordenan los objetos debido a que 
    se multiplica por una metrica. Sin embargo, para comparar terminos a ojo, es fundamental
    Poder ver los terminos con el mismo orden. 
    
    """

    sort_product(ex) # Suponiendo el SortOrtder ya se definió en el kernel para un tratameinto mas rapido, en caso de que no, tomará el defaul
    
    """
    si ex es una suma:
        Iterar sobre cada uno de los elementos
    si no es:
       acá es la parte importante. El objeto tiene que ser un producto, en este producto,se hace lo sigueinte
       se obtienen los factores de ese producto. Además de como este factor tiene por ejemplo sus indices. 
       Por ejemplo: P^{a}_{b c} \epsilon^{c x w z}
       Para este caso los factores son: P^{a}_{b c}, \epsilon^{c x w z}
       El nombre base de cada uno es P, \epsilon. y se debe de crear una lista/diccionario de factores de la forma:
       P: {"arriba": [a], "abajo": [b, c], },
       epsilon: {"arriba": [c, x, w, z], }
       En orden de aparición para los indices, pues si se tiene por ejemplo X^{i}_{a b}^{d}
       se debe poner X: {"arriba": [i,d], "abajo": [a,b], }
       Hay que verificar cuales de estos factores tiene o no indices, si el factor es un escalar, entonces continue
       Luego se hace un split del orden deseado. Es decir, supongamos se tiene en orden $ P_{a}^{b c} \epsilon_{c x w z}$
       Entonces, se comparan los terminos de ex con esta lista que representa el orden deseado.
       Por ejemplo, para el primer factor del orden deseado, en este caso $P_{a}^{b c}$  se comparar con el factor de  $P^{a}_{b c}$ 
       Luego como se encuentra el mismo nombre base entonces se pregunta, El primero de los indices coindice en tener la misma posicion?
       En este caso son distintas, pues el orden deseado es para el primer indice abajo, por tanto hay que introducir una metrica
       Entonces hay que hacer $P^{a}_{b c}->P_{a_{1}}_{b c} \eta^{a a_{1}}$, acaá hay que aclarar que hay que hacer la relacion entre la metrica y los indices, es decir
       Se debe de poder saber cual es la metrica para los indices, y el orden de como se introduce los indices de la metrica \eta^{a a_{1}}, siempre debe de ser ese, 
       pues posteriormente se introducirá un eliminate_metric_bucle, y esa lee el primer indice que ve para eliminarlo de la expreison. 
       Analogamente se tiene que el segundo indice,b, está abajo, pero en el orden deseado se quiere arriba, entonces hay que hacer $P^{a}_{b c}->P^{a}^{b_{1}}_{c} \eta_{b b_{1}}$
       Y luego aplicar nuevamente eliminate_metric_bucle, o se puede hacer la sustitucion masiva
       $P^{a}_{b c}->P_{a}^{b_{1}}^{c_{1}} \eta^{a a_{1}} \eta_{b b_{1}} \eta_{c c_{1}}$  
       Para que no hayan conflictos se debe de dar ex, con un orden establecido, es decir, se desea que haya la misma cantidad de factores
       en ex como en orden, y que estén en orden correcto o en su defecto llamar a la funcion sort_order_with... De esta forma, se desea que
       Para este ejemplo concreto la funcion sea capaz de hacer esto:

       orden:P_{x y}^{y} P^{a}_{b}^{c} \epsilon_{c w x z}
       ex: P^{a b h} P_{v b c} \epsilon_{h z a z }

       P_{x y}^{c} P^{a}_{b}^{c} \epsilon_{c w x z}-> P^{a_{1} b{1} h} P_{v b c} \eta_{x a_{1}} \eta_{y b{1}} ....



       
       


       
           

        

    """






    pass
