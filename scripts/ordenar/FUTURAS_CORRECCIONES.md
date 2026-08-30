# FUTURAS EXTENSIONES Y CORRECCIONES PARA EL ORDENADOR

Este documento registra ideas comprobadas experimentalmente que han sido pospuestas para futuras fases de desarrollo. Su objetivo es mantener el ordenador principal simple mientras trazamos el camino de su evolución.

### 1. Ordenamiento por topología

Posteriormente podremos analizar cada factor individual mediante su estructura exacta:
`(base, topología posicional de índices)`

Esta información se utilizará para construir dinámicamente patrones específicos para `SortOrder`. Por ejemplo, distinguir `P^a_b^c` de `P_a^{bc}` extrayendo su topología `['super', 'sub', 'super']` y construyendo un patrón como `P_{x0?}^{x1?}^{x2?}` que fuerza a Cadabra a reconocer esa estructura.

### 2. Factores con misma base y misma topología

Existe un problema inherente cuando dos factores en un producto comparten estructura:
`P^a_b P^c_d`

Ambos factores tienen exactamente la misma base (`P`) y la misma topología posicional (`['super', 'sub']`). La topología por sí sola no permite a Cadabra (ni a nuestro ordenador) distinguir a cuál instancia se refiere una regla.

### 3. Conectividad mediante índices dummy

Como futura extensión, incorporaremos el análisis topológico del grafo para descubrir qué factores están conectados mediante índices contraídos.

Ejemplo conceptual:
`P^a_b Q^b_c R^c_d`

La conectividad (las "aristas" dadas por los índices dummy) entre estos factores podría utilizarse posteriormente como criterio de desambiguación y ordenamiento avanzado, superando las limitaciones exclusivas de la estructura local.

### 4. Resolución de conflictos

Si en el futuro necesitamos distinguir y ordenar instancias individuales de factores que sean estructuralmente idénticos, será necesario introducir identificadores temporales o algún mecanismo equivalente que aísle las identidades en el AST de Cadabra (por ejemplo, renombramientos temporales del tipo `TMP`).

- **NO implementar TMP ahora.**
- **NO implementar DFS ahora.**
- **NO implementar WL ahora.**

La resolución de colisiones queda estrictamente delegada a una fase posterior que integre el análisis de grafos.

### 5. Sumas

Actualmente `order()` ya maneja sumas a nivel superior separando los términos y enviando cada término recursivamente al ordenador principal. 

Sin embargo, posteriormente puede estudiarse si existen estructuras matemáticas o tensores mucho más profundamente anidados (sumas dentro de derivadas, paréntesis o integrales complejas) que requieran un recorrido de Árbol Sintáctico (AST) más general e intrusivo para ordenarse correctamente.
