import cadabra2
import textwrap
import re

if '_keepalive' not in cadabra2.__dict__:
    cadabra2.__dict__['_keepalive'] = []

def ejecutar_cadabra(codigo_nativo):
    """
    Ejecuta código escrito en sintaxis nativa pura de Cadabra (ej. {\mu}::Indices(space).)
    dentro del kernel actual de Python. Es equivalente a correr una celda de Cadabra.
    """
    codigo = textwrap.dedent(codigo_nativo).strip()
    codigo_python = cadabra2.cdb2python_string(codigo, True, "cadabra2")
    
    # Truco de magia: Evita que el recolector de basura de Python (GC) destruya
    # las propiedades C++ nativas al terminar la ejecución.
    codigo_python = re.sub(r'__cdbtmp__\s*=\s*(.*)', r'_keepalive.append(\1)', codigo_python)
    
    exec(codigo_python, cadabra2.__dict__)
