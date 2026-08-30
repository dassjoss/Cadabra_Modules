# FUTURAS EXTENSIONES

Este documento registra ideas y mejoras que han sido pospuestas para futuras fases de desarrollo, con el objetivo de mantener la implementación de `order.py` en su forma más simple y estable actualmente.

### Fase futura 1 — Topología
Analizar factores individuales utilizando una representación estructural como:
`(base, topología posicional)`
Estudiar cómo utilizar esta información internamente para construir y abstraer órdenes más expresivos, de modo que el usuario no necesite conocer la topología de los factores al llamar a la función.

### Fase futura 2 — Factores estructuralmente idénticos
Estudiar qué hacer cuando aparecen múltiples factores con exactamente:
`mismo base + misma topología`
Dado que `SortOrder` nativamente agrupa los factores por base, si tienen idéntica estructura local, se requiere una lógica superior para identificar a qué factor específico se refiere el orden.

### Fase futura 3 — Conectividad de dummies
Analizar los índices contraídos para obtener información de conectividad (grafo) entre factores.
Ejemplo:
`P^a_b Q^b_c R^c_d`
Esta conectividad puede utilizarse para diferenciar y ordenar con precisión factores que sean localmente idénticos pero que posean distintas conexiones globales en el producto.

### Fase futura 4 — Resolución de conflictos
Estudiar e implementar mecanismos de identificación temporal de factores en el AST (Abstract Syntax Tree) de Cadabra, en caso de que realmente resulten necesarios para resolver conflictos de instancias.
Posibles aproximaciones a explorar (pero NO implementadas actualmente):
- **TMP** (Renombramiento temporal de nodos AST).
- **DFS** (Búsqueda en Profundidad con Backtracking para emparejar grafos).
- **WL** (Test de Isomorfismo de Weisfeiler-Lehman).
- **Teoría de grafos**.

### Fase futura 5 — Recorrido AST más profundo
Actualmente `order()` extrae los términos de una suma a nivel superior. Se debe estudiar si posteriormente es necesario ordenar productos que aparezcan dentro de estructuras algebraicas mucho más profundas que una suma de términos en la capa más alta (por ejemplo, sumas dentro de derivadas, parentesis no expandidos, etc.).
