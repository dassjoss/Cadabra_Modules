import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from cadabra2 import Ex, Derivative
try:
    Derivative(Ex(r'\partial{#}'))
    Derivative(Ex(r'\nabla{#}'))
except Exception:
    pass

from scripts.obtener_indices_libres.obtener_indices_libres import fundamental, eliminar_dummies
from scripts.obtener_indices_libres.test.banco_de_pruebas import TESTS
from scripts.obtener_indices_libres.test.test_obtener_indices_libres import normalizar_resultado

fallidos = []
for nombre_test, expr_str, esperado in TESTS:
    try:
        ex_obj = Ex(expr_str)
        resultado = eliminar_dummies(fundamental(ex_obj))
        if esperado == "INVALID":
            fallidos.append((nombre_test, expr_str, esperado))
        elif normalizar_resultado(resultado) != normalizar_resultado(esperado):
            fallidos.append((nombre_test, expr_str, esperado))
    except Exception:
        if esperado != "INVALID":
            fallidos.append((nombre_test, expr_str, esperado))

out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "casos_fallidos.py"))
with open(out_path, "w", encoding="utf-8") as f:
    f.write("CASOS_FALLIDOS = [\n")
    for nombre, expr, esp in fallidos:
        f.write(f"    ({repr(nombre)}, r\"\"\"{expr}\"\"\", {repr(esp)}),\n")
    f.write("]\n")

print(f"ÉXITO: Se guardaron {len(fallidos)} casos fallidos en {out_path}")
