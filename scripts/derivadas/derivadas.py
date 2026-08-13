import cadabra2
from cadabra2 import Ex, parent_rel_t
from cdb.utils.indices import get_free_indices

from scripts.get_full_index_name import get_full_index_name
from scripts.mutar_nodo_indice import mutar_nodo_indice
from scripts.mutar_indice import mutar_indice


def d_c_g(ex, idx_curvos_totales, idx_planos_totales):

    indices_en_uso = set()
    iterador_global = iter(ex)
    print("TIPO ITERADOR:", type(iterador_global))

    for n in iterador_global:
        nombre = get_full_index_name(n)
        if nombre not in indices_en_uso:
            indices_en_uso.add(nombre)

    idx_curvos = [idx for idx in idx_curvos_totales if idx not in indices_en_uso]
    idx_planos = [idx for idx in idx_planos_totales if idx not in indices_en_uso]

    while True:
        curvos_trabajo = idx_curvos.copy()
        planos_trabajo = idx_planos.copy()

        iterador = ex[r'\nabla']
        try:
            nabla = next(iterador)
        except StopIteration:
            break

        print("TIPO EX:", type(ex))
        print("EX:", ex)
        print("CALLABLE EX:", callable(ex))
        print("ITER EX:", getattr(ex, "__iter__", None))
        indices_en_uso = set()
        iterador_global = iter(ex)
        for n in iterador_global:
            nombre = get_full_index_name(n)
            if nombre not in indices_en_uso:
                indices_en_uso.add(nombre)

        curvos_trabajo = [idx for idx in curvos_trabajo if idx not in indices_en_uso]
        planos_trabajo = [idx for idx in planos_trabajo if idx not in indices_en_uso]

        argumentos = list(nabla.args())
        if len(argumentos) == 0:
            nabla.name = r'\partial'
            continue

        dindex = nabla.indices().__next__()
        terminos_conexion = Ex(0)

        for arg in argumentos:
            nodo_ex = Ex(r'@(arg)')

            try:
                indices_libres_cpp = get_free_indices(nodo_ex)
                indices_logicos = [get_full_index_name(next(iter(idx))) for idx in indices_libres_cpp]
            except Exception as e:
                continue

            for nombre_idx in indices_logicos:

                # Si obtener_nodo_indice no está presente en el entorno se maneja limpiamente
                try:
                    from scripts.utils import obtener_nodo_indice
                    idx_original = obtener_nodo_indice(nodo_ex, nombre_idx)
                except Exception:
                    continue

                if nombre_idx in idx_curvos_totales:

                    mudo = curvos_trabajo.pop(0)
                    t2 = Ex(r'@(arg)')
                    mutar_indice(t2, nombre_idx, mudo)

                    nodo_idx = idx_original

                    if nodo_idx.parent_rel == parent_rel_t.sub:
                        t1 = Ex(r"-\Gamma^{" + mudo + "}_{" + dindex.name + " " + nombre_idx + "}")
                    else:
                        t1 = Ex(r"\Gamma^{" + nombre_idx + "}_{" + dindex.name + " " + mudo + "}")
                    terminos_conexion = terminos_conexion + t1 * t2
                    mutar_indice(arg, mudo, nombre_idx)

        nabla.name = r'\partial'
        reemplazo = Ex(r'@(nabla)') + terminos_conexion
        nabla.replace(reemplazo)

    return None
