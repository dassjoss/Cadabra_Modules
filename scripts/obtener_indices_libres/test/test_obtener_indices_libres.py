"""
Suite de pruebas automatizadas para obtener_indices_libres.
Muestra ÚNICAMENTE el resumen y las pruebas que fallaron en el output.
"""

import sys
import os

# Asegurar que la raíz del proyecto esté en sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

try:
    from cadabra2 import Ex, Derivative
    from scripts.obtener_indices_libres.obtener_indices_libres import fundamental, eliminar_dummies
    from .banco_de_pruebas import TESTS
except ImportError:
    from cadabra2 import Ex, Derivative
    from scripts.obtener_indices_libres.obtener_indices_libres import fundamental, eliminar_dummies
    from banco_de_pruebas import TESTS

GREEK_MAP = {
    'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta', 'ε': 'epsilon', 'ζ': 'zeta',
    'η': 'eta', 'θ': 'theta', 'ι': 'iota', 'κ': 'kappa', 'λ': 'lambda', 'μ': 'mu',
    'ν': 'nu', 'ξ': 'xi', 'ο': 'omicron', 'π': 'pi', 'ρ': 'rho', 'σ': 'sigma',
    'τ': 'tau', 'υ': 'upsilon', 'φ': 'phi', 'χ': 'chi', 'ψ': 'psi', 'ω': 'omega',
    'Γ': 'Gamma', 'Δ': 'Delta', 'Θ': 'Theta', 'Λ': 'Lambda', 'Ξ': 'Xi', 'Π': 'Pi',
    'Σ': 'Sigma', 'Υ': 'Upsilon', 'Φ': 'Phi', 'Ψ': 'Psi', 'Ω': 'Omega'
}


def normalizar_resultado(resultado):
    """
    Normaliza las tuplas de índices convirtiendo letras griegas unicode/TeX
    a nombres de identificador estándar (p. ej. 'μ' y '\\mu' -> 'mu').
    """
    if isinstance(resultado, str):
        return resultado

    normalizados = []
    for item in resultado:
        nombre, pos = item
        nombre_clean = nombre.lstrip("\\")
        nombre_norm = GREEK_MAP.get(nombre_clean, nombre_clean)
        normalizados.append((nombre_norm, pos))

    return set(normalizados)


def ejecutar_banco_de_pruebas(mostrar_exitos=False):
    """
    Ejecuta la suite de pruebas TESTS (380 casos) y muestra ÚNICAMENTE
    el resumen y las pruebas que fallaron.
    """
    try:
        Derivative(Ex(r'\partial{#}'))
        Derivative(Ex(r'\nabla{#}'))
    except Exception:
        pass

    exitos = 0
    fallos = 0
    total = len(TESTS)
    pruebas_fallidas = []

    for nombre_test, expr_str, esperado in TESTS:
        try:
            ex_obj = Ex(expr_str)
            resultado = eliminar_dummies(fundamental(ex_obj))

            if esperado == "INVALID":
                fallos += 1
                pruebas_fallidas.append({
                    "nombre": nombre_test,
                    "expr": expr_str,
                    "obtenido": resultado,
                    "esperado": "INVALID",
                    "error": "Expresión inválida no detectada"
                })
                continue

            res_set = normalizar_resultado(resultado)
            esp_set = normalizar_resultado(esperado)

            if res_set == esp_set:
                exitos += 1
                if mostrar_exitos:
                    print(f"✓ [{nombre_test}] -> PASÓ")
            else:
                fallos += 1
                pruebas_fallidas.append({
                    "nombre": nombre_test,
                    "expr": expr_str,
                    "obtenido": resultado,
                    "esperado": esperado,
                    "error": "No coincide resultado obtenido con esperado"
                })

        except Exception as e:
            if esperado == "INVALID":
                exitos += 1
                if mostrar_exitos:
                    print(f"✓ [{nombre_test}] -> DETECTADO INVÁLIDO ({type(e).__name__})")
            else:
                fallos += 1
                pruebas_fallidas.append({
                    "nombre": nombre_test,
                    "expr": expr_str,
                    "obtenido": f"EXCEPCIÓN: {type(e).__name__}: {e}",
                    "esperado": esperado,
                    "error": f"Lanzó excepción {type(e).__name__}"
                })

    # Imprimir resumen de estadísticas
    print("=" * 80)
    print("RESUMEN DE PRUEBAS")
    print("=" * 80)
    print(f"Total pruebas ejecutadas: {total}")
    print(f"✓ Éxitos:                 {exitos}")
    print(f"✗ Fallos:                 {fallos}")
    if total > 0:
        print(f"Porcentaje de éxito:      {(exitos / total) * 100:.2f}%")
    print("=" * 80)

    # IMPRIMIR ÚNICAMENTE LOS CASOS QUE FALLARON
    if pruebas_fallidas:
        print(f"\nLISTA DE CASOS FALLIDOS ({len(pruebas_fallidas)} CASOS):")
        print("-" * 80)
        for i, item in enumerate(pruebas_fallidas, start=1):
            print(f"{i:2d}. [{item['nombre']}]")
            print(f"    Expresión: {item['expr']}")
            print(f"    Obtenido:  {item['obtenido']}")
            print(f"    Esperado:  {item['esperado']}")
            print("-" * 80)
    else:
        print("\n¡TODAS LAS PRUEBAS PASARON CORRECTAMENTE! 🎉")

    return fallos == 0, pruebas_fallidas


if __name__ == "__main__":
    mostrar_all = "-v" in sys.argv or "--verbose" in sys.argv
    ejecutar_banco_de_pruebas(mostrar_exitos=mostrar_all)
