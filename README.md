# Cadabra Modules

A modular Python toolkit for programmatically manipulating **Cadabra2** expression trees (`Ex` / `ExNode`). Designed for algebraic tensor operations, index mutation, free index extraction, and operator expansions in differential geometry, general relativity, and 3+1 Hamiltonian formulations.

---

## Overview

[Cadabra2](https://cadabra.science/) is a computer algebra system tailored for field theory and tensor calculus. While Cadabra2 provides built-in algorithms for canonicalization and substitution, programmatic manipulation of expression trees (AST) requires careful handling of tensor index nodes (`ExNode`), numeric sub-indices ($\lambda_1, \lambda_2$), and dummy index contractions.

`Cadabra_Modules` provides a collection of reusable Python utilities built directly on Cadabra2's Python API. It enables researchers and developers to analyze, mutate, contract, and format complex tensor expressions at the AST node level without resorting to fragile string manipulation.

---

## Key Features

- **Free Index Resolution**: Extract free vs. contracted (dummy) indices across sums, products, and generic operators (`obtener_indices_libres`), preserving sub-index structure.
- **AST Node & Index Mutation**: Directly mutate index nodes (`mutar_nodo_indice`) and replace subtrees by tree path (`mutar_nodo_completo`) within Cadabra expression trees.
- **Metric Contraction & Delta Elimination**: Contract indices across metric tensors ($\eta_{ab}, \eta^{ab}$) and Kronecker deltas ($\delta^a_b$) via `eliminar_metricas`.
- **Covariant Derivative Expansion**: Expand covariant derivative operators ($\nabla_\mu$, $D_i$) into partial derivatives and connection terms using a user-specified connection symbol via `d_c_g`.
- **Tensor Canonicalization & Symmetries**: Structurally sort product factors (`ordenar_estructura`), handle Schouten identities (`shouten_indices`), and manage tensor symmetries.
- **Rich Display Formatting**: Render LaTeX tensor expressions cleanly in Jupyter Notebooks using `agrupar_salidas` and `definir_objeto_visual`.

---

## Project Structure

```text
scripts/
├── derivadas/                  # Covariant derivative expansion algorithms (d_c_g)
├── obtener_indices_libres/     # Free and dummy index extraction rules
├── mutar_nodo_indice/          # AST index node mutation utilities
├── mutar_todos_indices/        # Global index replacement across sums and products
├── mutar_nodo_completo/        # Deep AST node replacement by tree path
├── eliminar_metricas/          # Metric tensor contraction and delta elimination
├── ordenar_estructura/         # Structural term sorting and canonicalization
├── ordenar/                    # High-level factor sorting wrappers
├── shouten_indices/            # Schouten identity applications
├── definir_objeto_visual/      # Custom LaTeX visual representation rules
├── agrupar_salidas/            # Multi-expression LaTeX display helpers for Jupyter
├── ejecutar_cadabra.py         # Subprocess runner for Cadabra CLI execution
└── utils.py                    # Package exports and utility entry point
```

---

## Usage Examples

### 1. Expanding Covariant Derivatives

The `d_c_g` module expands covariant derivative operators ($D_i$) acting on multi-indexed tensors into partial derivatives ($\partial_i$) and connection terms. The connection symbol is supplied by the user; here, `\omega` is used as an example to represent a spin connection. For each free Lorentz index on the target tensor, `d_c_g` generates a connection term and automatically selects contracted dummy indices (`c`, `d`) from the supplied Lorentz-index pool:

$$
D_i P^{ab} \longrightarrow \partial_i P^{ab} + \omega_{ic}{}^{a} P^{cb} + \omega_{id}{}^{b} P^{ad}
$$

Note that `d_c_g` mutates the input `Ex` expression in place while returning the updated `Ex` instance:

```python
from cadabra2 import Ex, Indices
from scripts import d_c_g

# Declare index families
lorentz_indices = ["a", "b", "c", "d", "e"]
Indices(Ex("a, b, c, d, e"), Ex("name=lorentz, position=fixed"))
Indices(Ex("i, j, k"), Ex("name=space, position=fixed"))

# Expand gauge covariant derivative D_i on tensor P^{a b}
expr = Ex(r"D_{i}{P^{a b}}")
result = d_c_g(expr, r"D", r"\omega", lorentz_indices)
print(result)
# Output:
# \partial_{i}(P^{a b}) + ω_{i c}^{a} P^{c b} + ω_{i d}^{b} P^{a d}
```

### 2. AST Node Mutation by Path

To modify expressions deterministically without relying on string substitution, `mutar_nodo_completo` navigates the Cadabra AST by child index path and replaces target nodes directly:

$$
A^{ab} B_{bc} \longrightarrow A^{ab} C_{bc}
$$

```python
from cadabra2 import Ex
from scripts import mutar_nodo_completo

expr = Ex(r"A^{a b} B_{b c}")

# Replace the second factor node (B_{b c}) at child path "1"
mutar_nodo_completo(expr, Ex(r"C_{b c}"), path="1")
print(expr)
# Output: A^{a b} C_{b c}
```

### 3. Extracting Free Indices across Nested Operators

Native Cadabra2 index queries inspect top-level expression nodes, but when tensors are wrapped inside nested operators (e.g., nested covariant derivatives), shallow queries do not recursively inspect the internal argument hierarchy. `obtener_indices_libres` recursively traverses operator arguments to recover all free indices and their positions (`super`/`sub`):

```python
from cadabra2 import Ex
from scripts import obtener_indices_libres

# Nested covariant derivative acting on a tensor
expr = Ex(r"\nabla_{\mu}{\nabla_{\nu}{T^{i j k}_{l m}}}")

# Recursively extract free indices through the operator hierarchy
free_indices = obtener_indices_libres(expr)
print(free_indices)
# Output: [('μ', 'sub'), ('ν', 'sub'), ('i', 'super'), ('j', 'super'), ('k', 'super'), ('l', 'sub'), ('m', 'sub')]
```

---

## Installation & Prerequisites

### Prerequisites

- **Cadabra2**: Must be installed on the system (via AppImage, system package, or built from source). See [Cadabra2 Installation](https://cadabra.science/notebooks/installation.html).
- **Python 3.8+**

### Setup

Clone the repository and install optional Python dependencies:

```bash
git clone https://github.com/dassjoss/Cadabra_Modules.git
cd Cadabra_Modules
pip install -r requirements.txt
```

---

## Scientific Context

`Cadabra_Modules` was developed to support symbolic tensor computations in **differential geometry** and **theoretical gravitational physics**. Key applications include:

- **3+1 Hamiltonian Formulations of General Relativity** (e.g., Ashtekar–Peldan variables, ADM decomposition).
- Covariant derivative expansions for mixed spacetime and internal Lorentz indices.
- Frame fields (tetrads/vierbeins) and spin connection manipulations.

---

## Development Status

The core utilities for free index resolution, AST manipulation, metric contraction, and output display are implemented and under active validation, with automated unit test coverage established for free index resolution (`obtener_indices_libres`). Higher-level derivative expansions (`d_c_g`) and structural term sorting algorithms (`ordenar_estructura`) continue to be refined for specialized tensor identities.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
