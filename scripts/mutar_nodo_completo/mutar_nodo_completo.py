from itertools import islice
import re


def mutar_nodo_completo(expr, final, path):
    indices = [int(x) for x in re.findall(r'\d+', path)]

    nivel = expr.top()

    for idx in indices:
        nivel = next(islice(nivel.children(), idx, None))

    nivel.replace(final)