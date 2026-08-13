# Expansión de Derivadas Covariantes en Cadabra2

Este módulo proporciona herramientas algebraicas para expandir derivadas covariantes (`\nabla`) en términos de derivadas parciales (`\partial`), símbolos de Christoffel (`\Gamma`) para índices curvos (espaciotiempo) y conexiones de espín (`\omega`) para índices planos (Lorentz).

El desarrollo se está realizando de forma incremental, separando las responsabilidades del algoritmo en pequeñas utilidades que trabajan directamente con la estructura de árboles de expresiones (`Ex` / `ExNode`) de Cadabra2.

---

# Estado actual del desarrollo

La primera capa de utilidades está parcialmente completada.

Actualmente se encuentran implementadas y probadas:

```text
get_full_index_name()
obtener_indices_libres()
mutar_nodo_indice()
```

`obtener_nodo_indice()` está definida conceptualmente y requiere una última adaptación para utilizar correctamente la identificación de índices libres proporcionada por Cadabra2.

El flujo conceptual es:

```text
Expresión Cadabra
       │
       ▼
obtener_indices_libres(expr)
       │
       ▼
Índices libres
       │
       ▼
obtener_nodo_indice(expr, nombre)
       │
       ▼
ExNode correspondiente
       │
       ▼
mutar_nodo_indice(...)
```

La función `mutar_nodo_indice()` ya fue probada estructuralmente con índices simples y con índices que contienen subíndices numéricos.

---

# 1. Modelo de datos de Cadabra2

Una expresión de Cadabra puede entenderse como un árbol.

Por ejemplo:

```text
A^{λ₁ λ₂}
```

puede representarse conceptualmente como:

```text
A
├── λ₁
│   └── 1
└── λ₂
    └── 2
```

El índice `λ₁` no es simplemente una cadena de texto.

El nodo correspondiente posee información estructural:

```python
str(nodo)
nodo.name
nodo.children()
nodo.parent_rel
nodo.multiplier
```

Por ejemplo, en las pruebas realizadas:

```text
str(nodo)       → 'λ_{1}'
nodo.name       → '\lambda'
nodo.multiplier → 1
```

y su hijo posee:

```text
str(hijo)       → '1'
hijo.name      → '1'
hijo.multiplier → 1
```

Para valores numéricos diferentes aparece una particularidad importante de Cadabra2:

```text
λ₁ → nodo.name = '\lambda'
     hijo.name = '1'
     hijo.multiplier = 1

λ₄ → nodo.name = '\lambda'
     hijo.name = '1'
     hijo.multiplier = 4
```

Por tanto, **`name` no contiene necesariamente el valor numérico real del subíndice**.

La representación correcta del hijo debe obtenerse mediante:

```python
str(hijo)
```

o mediante su estructura interna, donde el valor aparece en:

```python
hijo.multiplier
```

Esto fue fundamental para corregir `mutar_nodo_indice()`.

---

# 2. `get_full_index_name`

## Función

```python
def get_full_index_name(n):
    """Reconstruye el nombre completo del índice incluyendo sus hijos."""
    name = n.name
    children = list(n.children())

    if children:
        name += "_{" + str(children[0]) + "}"

    return name
```

## Responsabilidad

Reconstruir el nombre completo de un índice a partir del nodo raíz y sus hijos.

Esto es necesario porque:

```python
n.name
```

no necesariamente contiene toda la información del índice.

Para:

```text
λ₁
```

se tiene:

```text
n.name
    ↓
\lambda
```

mientras que el hijo contiene el valor del subíndice.

La función combina ambas partes:

```text
\lambda + _{1}
       ↓
\lambda_{1}
```

## Ejemplo

Para:

```text
A^{λ₁ λ₂ λ₃}
```

la función puede utilizarse para reconstruir:

```text
\lambda_{1}
\lambda_{2}
\lambda_{3}
```

## Retorno

Devuelve un `str`.

Por ejemplo:

```python
get_full_index_name(nodo)
```

produce conceptualmente:

```text
"\lambda_{1}"
```

---

# 3. `obtener_indices_libres`

## Función conceptual actual

La identificación de índices libres debe realizarse utilizando la funcionalidad propia de Cadabra2:

```python
expr.top().free_indices()
```

## Comportamiento comprobado

Las pruebas realizadas directamente sobre Cadabra2 demostraron que:

```python
expr.top().free_indices()
```

identifica correctamente los índices libres.

### Un índice libre

Para:

```text
A^{α}
```

Cadabra devuelve:

```text
α
```

como índice libre.

### Índice dummy

Para:

```text
A^{α} B_{α}
```

no devuelve ningún índice libre:

```text
TOTAL INDICES LIBRES: 0
```

### Dos índices libres

Para:

```text
A^{α} B_{β}
```

devuelve:

```text
α
β
```

### Dummy con subíndice numérico

Para:

```text
A^{λ₁} B_{λ₁}
```

no devuelve índices libres.

### Índice numérico libre

Para:

```text
A^{λ₁} B_{β}
```

devuelve:

```text
λ₁
β
```

Por tanto, Cadabra2 reconoce correctamente la diferencia entre índices libres y dummy incluso cuando los índices contienen subíndices numéricos.

---

## Importante: `free_indices()` frente a `get_free_indices()`

Durante las pruebas se comprobó que:

```python
expr.get_free_indices()
```

**no existe** para objetos `cadabra2.Ex`.

Cadabra produjo:

```text
AttributeError:
'cadabra2.Ex' object has no attribute 'get_free_indices'
```

En cambio:

```python
expr.top().free_indices()
```

sí funciona.

Por tanto, no debe documentarse:

```python
expr.get_free_indices()
```

como una API disponible de `Ex`.

La función `obtener_indices_libres()` debe utilizar la interfaz que realmente proporciona Cadabra2.

---

# 4. `obtener_nodo_indice`

## Objetivo

`obtener_nodo_indice()` recibe:

```python
expr
nombre_buscado
```

y debe devolver el `ExNode` correspondiente al índice libre solicitado.

Conceptualmente:

```text
expr
 │
 ├── índice libre 1
 ├── índice libre 2
 ├── índice dummy
 └── índice libre 3
```

La función debe distinguir entre ellos.

---

## Primera etapa: verificar que el índice sea libre

La primera operación será:

```python
indices_libres = obtener_indices_libres(expr)
```

Después debe comprobarse si:

```text
nombre_buscado
```

corresponde realmente a uno de esos índices libres.

Esto es importante porque un índice dummy aparece en dos posiciones del árbol.

Por ejemplo:

```text
A^{α} B_{α}
```

contiene dos nodos asociados a `α`, pero `α` **no es un índice libre**.

Por tanto:

```python
obtener_nodo_indice(expr, r"\alpha")
```

no debe devolver arbitrariamente uno de esos nodos.

Debe detectar primero que `α` no es libre.

---

## Segunda etapa: localizar el `ExNode`

Una vez confirmado que el índice es libre, se recorre el árbol de `expr`.

Para cada nodo se debe determinar si representa el índice buscado.

La comparación no debe depender únicamente de:

```python
nodo.name
```

porque:

```text
λ₁
λ₂
λ₃
λ₄
```

pueden compartir:

```text
nodo.name = \lambda
```

La comparación debe considerar la estructura completa del índice.

Por ejemplo:

```text
\lambda_{1}
\lambda_{2}
\lambda_{3}
```

son índices distintos aunque tengan el mismo `name`.

---

## Caso con subíndice

Para un índice como:

```text
λ₁
```

la lógica debe considerar:

```text
nombre principal → \lambda
                    │
                    └── hijo → 1
```

Por tanto, no basta con preguntar:

```python
nodo.name == "\lambda"
```

porque eso no distingue entre:

```text
λ₁
λ₂
λ₃
```

La función `get_full_index_name()` proporciona un mecanismo para comparar la estructura completa.

---

## Estado actual

La lógica de `obtener_nodo_indice()` está prácticamente definida, pero debe terminar de implementarse y probarse directamente contra:

```python
expr.top().free_indices()
```

antes de considerarla cerrada.

---

# 5. `mutar_nodo_indice`

## Estado

**Implementada y probada.**

Esta función modifica estructuralmente un índice que ya existe en el árbol.

Su firma es:

```python
def mutar_nodo_indice(nodo, nombre_nuevo):
```

Recibe:

```text
nodo
    ↓
ExNode existente

nombre_nuevo
    ↓
representación del índice destino
```

Por ejemplo:

```text
λ₁ → λ₄
```

o:

```text
λ₁ → α
```

---

# 6. Funcionamiento de `mutar_nodo_indice`

La función construye temporalmente el índice destino:

```python
nuevo_ex = Ex(nombre_nuevo)
```

Después obtiene el primer `ExNode` de esa expresión temporal.

La estructura del índice destino se separa en:

```text
nombre principal
+
hijos
```

Los hijos existentes del nodo original se eliminan:

```python
hijos_actuales = list(nodo.children())

for hijo in hijos_actuales:
    hijo.erase()
```

Luego se modifica:

```python
nodo.name = nuevo_nombre
```

donde `nuevo_nombre` representa únicamente el nombre principal del nodo.

Finalmente, si el índice destino posee un subíndice, se construye un nuevo `ExNode` para dicho hijo y se asigna:

```python
hijo_nuevo.parent_rel = parent_rel_t.sub
```

antes de insertarlo:

```python
nodo.append_child(hijo_nuevo)
```

---

# 7. Corrección importante para subíndices numéricos

Durante las primeras pruebas apareció un comportamiento importante de Cadabra2.

Para:

```text
λ₄
```

el hijo tiene:

```text
str(hijo)       → '4'
hijo.name       → '1'
hijo.multiplier  → 4
```

Por tanto, utilizar:

```python
Ex(hijo_destino.name)
```

era incorrecto para reconstruir el valor numérico.

Esto producía:

```text
λ₁
```

cuando se esperaba:

```text
λ₄
```

La corrección implementada fue:

```python
hijo_ex = Ex(str(hijo_destino))
```

De esta forma se conserva el valor real:

```text
hijo_destino = 4
        ↓
str(hijo_destino)
        ↓
"4"
        ↓
Ex("4")
```

Esto también permite transformar correctamente:

```text
λ₁ → α₂
```

y:

```text
α₁ → β₂
```

---

# 8. Pruebas de `mutar_nodo_indice`

La versión actual fue sometida a seis pruebas:

```text
TEST 1
α → β

TEST 2
λ₁ → λ₄

TEST 3
λ₁ → α

TEST 4
α → λ₁

TEST 5
λ₁ → α₂

TEST 6
α₁ → β₂
```

Resultados:

```text
[OK] alpha -> beta
[OK] lambda_1 -> lambda_4
[OK] lambda_1 -> alpha
[OK] alpha -> lambda_1
[OK] lambda_1 -> alpha_2
[OK] alpha_1 -> beta_2

6/6 pruebas exitosas
```

Por tanto, actualmente se considera validada para estos casos.

---

# 9. Implementación actual de `mutar_nodo_indice`

La versión validada es:

```python
def mutar_nodo_indice(nodo, nombre_nuevo):

    """
    Muta estructuralmente un indice libre.

    Ejemplos:
        alpha    -> beta
        lambda_1 -> lambda_4
        lambda_1 -> alpha
        alpha    -> lambda_1
        lambda_1 -> alpha_2
        alpha_1  -> beta_2
    """

    # ========================================================
    # 1. Construir temporalmente el indice destino
    # ========================================================

    nuevo_ex = Ex(nombre_nuevo)

    nuevo_nodo = None

    for candidato in nuevo_ex:
        nuevo_nodo = candidato
        break

    if nuevo_nodo is None:
        raise RuntimeError(
            f"No se pudo construir el indice destino: {nombre_nuevo}"
        )

    # ========================================================
    # 2. Obtener la estructura del indice destino
    # ========================================================

    nuevo_nombre = nuevo_nodo.name
    nuevos_hijos = list(nuevo_nodo.children())

    if len(nuevos_hijos) > 1:
        raise ValueError(
            f"El indice destino tiene mas de un hijo: {nombre_nuevo}"
        )

    # ========================================================
    # 3. Eliminar los hijos actuales del indice original
    # ========================================================

    hijos_actuales = list(nodo.children())

    for hijo in hijos_actuales:
        hijo.erase()

    # ========================================================
    # 4. Cambiar el nombre principal
    # ========================================================

    nodo.name = nuevo_nombre

    # ========================================================
    # 5. Reconstruir el subindice si existe
    # ========================================================

    if len(nuevos_hijos) == 1:

        hijo_destino = nuevos_hijos[0]

        # str(hijo_destino) conserva el valor real del
        # subindice numerico. hijo_destino.name puede ser
        # '1' aunque multiplier contenga otro valor.

        hijo_ex = Ex(str(hijo_destino))

        hijo_nuevo = None

        for candidato in hijo_ex:
            hijo_nuevo = candidato
            break

        if hijo_nuevo is None:
            raise RuntimeError(
                f"No se pudo construir el subindice de {nombre_nuevo}"
            )

        hijo_nuevo.parent_rel = parent_rel_t.sub

        nodo.append_child(hijo_nuevo)

    return nodo
```

---

# 10. Relación entre las utilidades

La arquitectura actual queda:

```text
                    EXPRESIÓN
                        │
                        ▼
              obtener_indices_libres()
                        │
                        ▼
              índices libres de Cadabra
                        │
                        ▼
              obtener_nodo_indice()
                        │
                        ▼
                    ExNode
                        │
                        ▼
              mutar_nodo_indice()
                        │
                        ▼
             árbol estructural modificado
```

Cada función tiene una responsabilidad diferente:

```text
get_full_index_name()
        │
        └── Identificar/reconstruir un índice completo

obtener_indices_libres()
        │
        └── Determinar qué índices son libres

obtener_nodo_indice()
        │
        └── Localizar el ExNode correspondiente

mutar_nodo_indice()
        │
        └── Modificar estructuralmente ese ExNode
```

---

# 11. Índices libres frente a índices dummy

Es fundamental mantener esta distinción.

## Índice libre

```text
A^{α}
```

Cadabra identifica:

```text
α
```

como libre.

Puede localizarse y modificarse mediante las utilidades correspondientes.

## Índice dummy

```text
A^{α} B_{α}
```

Cadabra identifica:

```text
0 índices libres
```

aunque existan dos nodos `α` en el árbol.

Por tanto, `obtener_nodo_indice()` no debe tratar simplemente:

```text
"α aparece en el árbol"
```

como equivalente a:

```text
"α es un índice libre"
```

La libertad del índice debe determinarse mediante Cadabra2.

---

# 12. Índices existentes frente a índices nuevos

También debe distinguirse entre dos operaciones.

## Índice existente

Por ejemplo:

```text
A^{λ₁}
```

`λ₁` ya está presente en la expresión.

La operación correspondiente es:

```python
obtener_nodo_indice(expr, nombre)
```

seguida, si es necesario, de:

```python
mutar_nodo_indice(nodo, nuevo_nombre)
```

## Índice nuevo

Al generar términos de una derivada covariante pueden ser necesarios índices auxiliares.

Por ejemplo, al construir términos de conexión:

```text
Γ^{λ₁}_{μ λ₂} A^{λ₂}
```

puede ser necesario crear un índice que todavía no existe en la expresión.

Esto es una operación diferente y **no debe realizarse mediante `obtener_nodo_indice()`**.

Será necesario implementar una utilidad independiente para crear índices nuevos y garantizar que no entren en conflicto con índices existentes.

---

# 13. Problemas históricos encontrados

## 13.1. `.name` no representa necesariamente el índice completo

Para:

```text
λ₁
```

el nodo raíz puede tener:

```text
name = \lambda
```

pero el índice completo es:

```text
\lambda_{1}
```

Por eso no se debe utilizar únicamente `.name` para identificar índices con subíndices.

---

## 13.2. Los nodos numéricos tienen una representación particular

Para el hijo de:

```text
λ₄
```

se observó:

```text
str(hijo)       = '4'
name            = '1'
multiplier      = 4
```

Esto significa que `.name` no debe utilizarse para recuperar directamente el valor numérico del subíndice.

La solución validada es:

```python
str(hijo)
```

---

## 13.3. `Ex` no posee `.get_free_indices()`

Se probó:

```python
expr.get_free_indices()
```

y Cadabra produjo:

```text
AttributeError:
'cadabra2.Ex' object has no attribute 'get_free_indices'
```

La interfaz que se comprobó funcionalmente es:

```python
expr.top().free_indices()
```

---

## 13.4. `Ex` y `ExNode` son objetos diferentes

Cuando se construye:

```python
Ex(r"\lambda_4")
```

se obtiene una expresión:

```text
Ex
│
└── ExNode
```

El `ExNode` es el elemento que pertenece al árbol y posee propiedades como:

```python
node.name
node.children()
node.parent_rel
node.multiplier
```

Esto explica por qué, al construir índices temporalmente, se utiliza un recorrido como:

```python
for candidato in nuevo_ex:
    nuevo_nodo = candidato
    break
```

El objetivo es obtener el `ExNode` raíz contenido en la expresión temporal.

No significa que `Ex` sea una lista de un solo elemento; `Ex` es el contenedor/expresión y la iteración permite acceder a sus nodos.

---

# 14. Próximos objetivos

La siguiente etapa es finalizar `obtener_nodo_indice()`.

La lógica propuesta es:

```text
                    expr
                     │
                     ▼
          obtener_indices_libres()
                     │
                     ▼
        ¿nombre_buscado es libre?
               /           \
             NO             SÍ
             │               │
             ▼               ▼
          None       recorrer árbol
                             │
                             ▼
                   localizar ExNode
                             │
                             ▼
                        devolver nodo
```

La localización deberá considerar tanto:

```text
nombre principal
```

como:

```text
estructura de subíndices
```

para diferenciar correctamente:

```text
λ₁
λ₂
λ₃
```

aunque todos tengan:

```text
name = \lambda
```

---

# 15. Utilidades pendientes

Una vez terminada `obtener_nodo_indice()`, la capa de utilidades deberá continuar aproximadamente en este orden:

```text
1. get_full_index_name()
        ↓
2. obtener_indices_libres()
        ↓
3. obtener_nodo_indice()
        ↓
4. mutar_nodo_indice()             ← COMPLETADO
        ↓
5. creación segura de índices nuevos
        ↓
6. construcción de términos Γ
        ↓
7. construcción de términos ω
        ↓
8. d_c_g()
```

---

# 16. Integración futura con `d_c_g`

Una vez completadas las utilidades de manipulación de índices, podrán utilizarse para construir la expansión de la derivada covariante.

Conceptualmente:

```text
∇
│
├── derivada parcial
│
├── términos Γ
│
└── términos ω
```

Para índices curvos se generarán términos asociados a:

```text
Γ
```

mientras que para índices planos se utilizarán:

```text
ω
```

La construcción de estos términos deberá utilizar las utilidades de índices en lugar de manipular directamente cadenas de texto.

---

# Estado del módulo

## Completado y probado

* `get_full_index_name()`
* identificación de índices libres mediante `expr.top().free_indices()`
* `mutar_nodo_indice()`
* mutaciones de índices simples
* mutaciones de índices con subíndices numéricos
* reconstrucción estructural de subíndices
* pruebas `alpha → beta`
* pruebas `lambda_1 → lambda_4`
* pruebas `lambda_1 → alpha`
* pruebas `alpha → lambda_1`
* pruebas `lambda_1 → alpha_2`
* pruebas `alpha_1 → beta_2`

Resultado de la batería actual:

```text
6/6 pruebas exitosas
```

## En implementación

* `obtener_nodo_indice()`

Debe validarse específicamente con:

```text
índice libre simple
índice libre con subíndice
múltiples índices libres
índice dummy
índice dummy con subíndice numérico
índice inexistente
```

## Pendiente

* creación segura de índices auxiliares
* generación de términos de Christoffel `Γ`
* generación de conexiones de espín `ω`
* integración final en `d_c_g`
* pruebas con tensores de rango superior
* pruebas con múltiples índices libres
* pruebas de derivadas covariantes anidadas
* pruebas de sumas y productos
* validación de índices libres y dummy después de las transformaciones
* validación con `canonicalise()`
* validación con `rename_dummies()`
* validación con `sort_product()`

---

# Estado general

La capa de manipulación básica de índices ya ha demostrado que es posible modificar índices directamente sobre el árbol de Cadabra2 conservando su estructura.

El punto más importante aprendido durante las pruebas es que **los índices deben tratarse como estructuras de árbol y no como cadenas de texto**.

En particular:

```text
λ₁
```

no debe entenderse simplemente como:

```text
"\lambda_1"
```

sino como:

```text
ExNode(\lambda)
    │
    └── ExNode(1)
```

y la diferencia entre índices numéricos como:

```text
λ₁
λ₂
λ₄
```

se encuentra en la estructura del hijo y su `multiplier`.

La siguiente tarea concreta es terminar `obtener_nodo_indice()` utilizando la identificación de índices libres de Cadabra2 y posteriormente validar su comportamiento antes de avanzar hacia la creación de índices auxiliares y la construcción de los términos `Γ` y `ω`.
