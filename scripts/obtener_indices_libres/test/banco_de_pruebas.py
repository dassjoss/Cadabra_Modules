"""
BANCO DE PRUEBAS — ÍNDICES TENSORIALES
"""

TESTS = [
    # =============================================================================
    # 001–020 — HOJAS: ESCALARES Y TENSORES BÁSICOS
    # =============================================================================

    ("001 — Escalar", r"A", []),

    ("002 — Escalar B", r"B", []),

    ("003 — Escalar C", r"C", []),

    ("004 — Vector covariante", r"A_{\mu}", [
        ('μ', 'sub')
    ]),

    ("005 — Vector contravariante", r"A^{\mu}", [
        ('μ', 'super')
    ]),

    ("006 — Tensor covariante rango 2", r"A_{\mu\nu}", [
        ('μ', 'sub'),
        ('ν', 'sub')
    ]),

    ("007 — Tensor contravariante rango 2", r"A^{\mu\nu}", [
        ('μ', 'super'),
        ('ν', 'super')
    ]),

    ("008 — Tensor mixto rango 2", r"A^{\mu}_{\nu}", [
        ('μ', 'super'),
        ('ν', 'sub')
    ]),

    ("009 — Tensor mixto rango 2 invertido", r"A_{\mu}^{\nu}", [
        ('μ', 'sub'),
        ('ν', 'super')
    ]),

    ("010 — Tensor covariante rango 3", r"A_{\mu\nu\rho}", [
        ('μ', 'sub'),
        ('ν', 'sub'),
        ('ρ', 'sub')
    ]),

    ("011 — Tensor contravariante rango 3", r"A^{\mu\nu\rho}", [
        ('μ', 'super'),
        ('ν', 'super'),
        ('ρ', 'super')
    ]),

    ("012 — Tensor mixto rango 3", r"A^{\mu}_{\nu\rho}", [
        ('μ', 'super'),
        ('ν', 'sub'),
        ('ρ', 'sub')
    ]),

    ("013 — Tensor mixto rango 3", r"A_{\mu}^{\nu\rho}", [
        ('μ', 'sub'),
        ('ν', 'super'),
        ('ρ', 'super')
    ]),

    ("014 — Tensor mixto rango 3", r"A^{\mu\nu}_{\rho}", [
        ('μ', 'super'),
        ('ν', 'super'),
        ('ρ', 'sub')
    ]),

    ("015 — Tensor mixto rango 3", r"A_{\mu\nu}^{\rho}", [
        ('μ', 'sub'),
        ('ν', 'sub'),
        ('ρ', 'super')
    ]),

    ("016 — Tensor covariante rango 4", r"A_{\mu\nu\rho\sigma}", [
        ('μ', 'sub'),
        ('ν', 'sub'),
        ('ρ', 'sub'),
        ('σ', 'sub')
    ]),

    ("017 — Tensor contravariante rango 4", r"A^{\mu\nu\rho\sigma}", [
        ('μ', 'super'),
        ('ν', 'super'),
        ('ρ', 'super'),
        ('σ', 'super')
    ]),

    ("018 — Tensor mixto rango 4", r"A^{\mu\nu}_{\rho\sigma}", [
        ('μ', 'super'),
        ('ν', 'super'),
        ('ρ', 'sub'),
        ('σ', 'sub')
    ]),

    ("019 — Tensor mixto rango 4", r"A_{\mu\nu}^{\rho\sigma}", [
        ('μ', 'sub'),
        ('ν', 'sub'),
        ('ρ', 'super'),
        ('σ', 'super')
    ]),

    ("020 — Tensor mixto rango 4", r"A^{\mu}_{\nu\rho\sigma}", [
        ('μ', 'super'),
        ('ν', 'sub'),
        ('ρ', 'sub'),
        ('σ', 'sub')
    ]),

    # =============================================================================
    # 021–040 — CONTRACCIONES EN UNA SOLA HOJA
    # =============================================================================

    ("021 — Contracción simple super-sub", r"A^{\mu}_{\mu}", []),

    ("022 — Contracción simple sub-super", r"A_{\mu}^{\mu}", []),

    ("023 — Traza de tensor rango 2", r"A^{\mu}_{\mu}", []),

    ("024 — Dos contracciones independientes", r"A^{\mu\nu}_{\mu\nu}", []),

    ("025 — Dos contracciones independientes invertidas", r"A_{\mu\nu}^{\mu\nu}", []),

    ("026 — Dos contracciones mixtas", r"A^{\mu\nu}_{\nu\mu}", []),

    ("027 — Contracción dejando un índice super", r"A^{\mu\nu}_{\nu}", [
        ('μ', 'super')
    ]),

    ("028 — Contracción dejando un índice sub", r"A_{\mu\nu}^{\nu}", [
        ('μ', 'sub')
    ]),

    ("029 — Contracción en tensor rango 3", r"A^{\mu}_{\mu\nu}", [
        ('ν', 'sub')
    ]),

    ("030 — Contracción en tensor rango 3 invertida", r"A_{\mu}^{\mu\nu}", [
        ('ν', 'super')
    ]),

    ("031 — Contracción con índice libre super", r"A^{\mu\nu}_{\mu}", [
        ('ν', 'super')
    ]),

    ("032 — Contracción con índice libre sub", r"A_{\mu\nu}^{\mu}", [
        ('ν', 'sub')
    ]),

    ("033 — Contracción dejando dos índices libres", r"A^{\mu\nu\rho}_{\mu}", [
        ('ν', 'super'),
        ('ρ', 'super')
    ]),

    ("034 — Contracción dejando dos índices libres mixtos", r"A^{\mu\nu}_{\mu\rho}", [
        ('ν', 'super'),
        ('ρ', 'sub')
    ]),

    ("035 — Contracción dejando dos índices libres mixtos 2", r"A^{\mu\nu}_{\rho\nu}", [
        ('μ', 'super'),
        ('ρ', 'sub')
    ]),

    ("036 — Contracción dejando dos índices libres covariantes", r"A^{\mu}_{\nu\rho\mu}", [
        ('ν', 'sub'),
        ('ρ', 'sub')
    ]),

    ("037 — Dos contracciones en rango 4", r"A^{\mu\nu}_{\mu\nu}", []),

    ("038 — Dos contracciones en orden cruzado", r"A^{\mu\nu}_{\nu\mu}", []),

    ("039 — Contracción y dos índices libres", r"A^{\mu\nu\rho}_{\nu\rho}", [
        ('μ', 'super')
    ]),

    ("040 — Contracción y dos índices libres covariantes", r"A_{\mu\nu\rho}^{\nu\rho}", [
        ('μ', 'sub')
    ]),

    # =============================================================================
    # 041–060 — PRODUCTOS Y CONTRACCIONES MÚLTIPLES
    # =============================================================================

    # 041 — Producto vector covariante × vector contravariante
    ("041 — Producto vectorial contraído",
     r"A_{\mu} B^{\mu}",
     []),

    # 042 — Producto vector contravariante × vector covariante
    ("042 — Producto vectorial contraído inverso",
     r"A^{\mu} B_{\mu}",
     []),

    # 043 — Producto tensor mixto con vector
    ("043 — Tensor mixto × vector contravariante",
     r"A^{\mu}_{\nu} B^{\nu}",
     [('μ', 'super')]),

    # 044 — Producto tensor mixto con vector covariante
    ("044 — Tensor mixto × vector covariante",
     r"A^{\mu}_{\nu} B_{\mu}",
     [('ν', 'sub')]),

    # 045 — Producto tensor covariante × vector contravariante
    ("045 — Tensor covariante × vector contravariante",
     r"A_{\mu\nu} B^{\nu}",
     [('μ', 'sub')]),

    # 046 — Producto tensor contravariante × vector covariante
    ("046 — Tensor contravariante × vector covariante",
     r"A^{\mu\nu} B_{\nu}",
     [('μ', 'super')]),

    # 047 — Dos contracciones independientes
    ("047 — Dos contracciones independientes",
     r"A^{\mu\nu} B_{\mu\nu}",
     []),

    # 048 — Dos contracciones con índices intercambiados
    ("048 — Dos contracciones intercambiadas",
     r"A^{\mu\nu} B_{\nu\mu}",
     []),

    # 049 — Producto con una contracción y dos índices libres
    ("049 — Una contracción y dos libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    # 050 — Producto encadenado con dos contracciones
    ("050 — Producto encadenado con dos contracciones",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}",
     [('μ', 'super')]),

    # 051 — Producto encadenado en orden inverso
    ("051 — Producto encadenado inverso",
     r"A_{\mu}^{\nu} B_{\nu}^{\rho} C_{\rho}",
     [('μ', 'sub')]),

    # 052 — Tres tensores con dos contracciones
    ("052 — Tres tensores dos contracciones",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma}",
     [('μ', 'super'), ('σ', 'sub')]),

    # 053 — Producto completamente contraído de tres factores
    ("053 — Producto completamente contraído",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu}",
     []),

    # 054 — Dos índices libres superiores
    ("054 — Dos libres superiores",
     r"A^{\mu}_{\rho} B^{\rho\nu}",
     [('μ', 'super'), ('ν', 'super')]),

    # 055 — Dos índices libres inferiores
    ("055 — Dos libres inferiores",
     r"A_{\mu}^{\rho} B_{\rho\nu}",
     [('μ', 'sub'), ('ν', 'sub')]),

    # 056 — Un índice libre superior y uno inferior
    ("056 — Libre superior e inferior",
     r"A^{\mu}_{\rho} B^{\rho}_{\nu}",
     [('μ', 'super'), ('ν', 'sub')]),

    # 057 — Contracción interna del primer tensor + índice libre del segundo
    ("057 — Contracción interna y libre externo",
     r"A^{\mu}_{\mu} B_{\nu}",
     [('ν', 'sub')]),

    # 058 — Contracción interna del segundo tensor + índice libre del primero
    ("058 — Libre externo y contracción interna",
     r"A^{\mu} B^{\rho}_{\rho}",
     [('μ', 'super')]),

    # 059 — Dos trazas multiplicadas
    ("059 — Producto de dos trazas",
     r"A^{\mu}_{\mu} B^{\nu}_{\nu}",
     []),

    # 060 — Traza multiplicada por tensor
    ("060 — Traza × tensor",
     r"A^{\mu}_{\mu} B_{\nu\rho}",
     [('ν', 'sub'), ('ρ', 'sub')]),

    # =============================================================================
    # 061–080 — PRODUCTOS COMPLEJOS Y CONTRACCIONES ANIDADAS
    # =============================================================================

    # 061 — Tres factores, una contracción
    ("061 — Tres factores una contracción",
     r"A_{\mu} B^{\mu} C_{\nu}",
     [('ν', 'sub')]),

    # 062 — Tres factores, una contracción y dos índices libres
    ("062 — Tres factores una contracción dos libres",
     r"A_{\mu} B^{\mu\nu} C_{\rho}",
     [('ν', 'super'), ('ρ', 'sub')]),

    # 063 — Tres factores, una contracción y tres índices libres
    ("063 — Tres factores una contracción tres libres",
     r"A_{\mu\nu} B^{\nu} C^{\rho}",
     [('μ', 'sub'), ('ρ', 'super')]),

    # 064 — Cadena de cuatro tensores
    ("064 — Cadena de cuatro tensores",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}",
     [('μ', 'super')]),

    # 065 — Cadena de cuatro tensores con índice libre inferior
    ("065 — Cadena de cuatro tensorial inversa",
     r"A_{\mu}^{\nu} B_{\nu}^{\rho} C_{\rho}^{\sigma} D_{\sigma}",
     [('μ', 'sub')]),

    # 066 — Cadena de cuatro tensores con dos libres
    ("066 — Cadena cuatro dos libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda}",
     [('μ', 'super'), ('λ', 'sub')]),

    # 067 — Producto con dos contracciones separadas
    ("067 — Dos contracciones separadas",
     r"A^{\mu}_{\nu} B^{\rho}_{\sigma} C^{\nu}_{\rho} D^{\sigma}_{\lambda}",
     [('μ', 'super'), ('λ', 'sub')]),

    # 068 — Dos contracciones cruzadas
    ("068 — Dos contracciones cruzadas",
     r"A^{\mu\nu} B_{\rho\sigma} C^{\rho}_{\mu} D^{\sigma}_{\nu}",
     []),

    # 069 — Contracciones completamente cruzadas
    ("069 — Contracciones cruzadas",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma}_{\mu} D_{\nu}",
     []),

    # 070 — Producto completamente contraído de cuatro factores
    ("070 — Cuatro factores completamente contraídos",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\mu}",
     []),

    # 071 — Traza interna más contracción
    ("071 — Traza interna más contracción",
     r"A^{\mu}_{\mu} B^{\nu}_{\rho} C^{\rho}_{\nu}",
     []),

    # 072 — Traza interna con dos libres
    ("072 — Traza interna con dos libres",
     r"A^{\mu}_{\mu} B^{\nu}_{\rho} C^{\rho}_{\sigma}",
     [('ν', 'super'), ('σ', 'sub')]),

    # 073 — Dos trazas más tensor
    ("073 — Dos trazas más tensor",
     r"A^{\mu}_{\mu} B^{\nu}_{\nu} C_{\rho\sigma}",
     [('ρ', 'sub'), ('σ', 'sub')]),

    # 074 — Traza y cadena
    ("074 — Traza y cadena",
     r"A^{\mu}_{\mu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}",
     [('ν', 'super')]),

    # 075 — Producto con contracciones en extremos
    ("075 — Contracciones en extremos",
     r"A_{\mu} B^{\mu\nu}_{\rho} C^{\rho}_{\nu}",
     []),

    # 076 — Producto con índice libre en medio
    ("076 — Libre en tensor intermedio",
     r"A_{\mu} B^{\mu\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}",
     [('ν', 'super')]),

    # 077 — Producto con dos cadenas independientes
    ("077 — Dos cadenas independientes",
     r"A^{\mu}_{\nu} B^{\nu} C_{\rho} D^{\rho}_{\sigma}",
     [('μ', 'super'), ('σ', 'sub')]),

    # 078 — Dos cadenas completamente independientes con libres
    ("078 — Cadenas independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\sigma}_{\lambda} D^{\lambda}",
     [('μ', 'super'), ('ρ', 'sub'), ('σ', 'super')]),

    # 079 — Contracción entre cadenas
    ("079 — Contracción entre cadenas",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\mu}",
     []),

    # 080 — Cadena larga con índice libre
    ("080 — Cadena larga con libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa}",
     [('μ', 'super'), ('κ', 'sub')]),

    # =============================================================================
    # 081–100 — CONTRACCIONES MÚLTIPLES Y ESTRUCTURAS COMPLEJAS
    # =============================================================================

    ("081 — Dos contracciones independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\rho}",
     []),

    ("082 — Dos contracciones con índice libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma}",
     [('μ', 'super'), ('σ', 'sub')]),

    ("083 — Cadena de tres contracciones",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\mu}",
     []),

    ("084 — Cadena con un índice libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda}",
     [('μ', 'super'), ('λ', 'sub')]),

    ("085 — Dos libres y dos mudos",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma}_{\lambda}",
     [('μ', 'super'), ('ν', 'super'), ('λ', 'sub')]),

    ("086 — Contracción cruzada de tres tensores",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma}_{\mu}",
     [('ν', 'super')]),

    ("087 — Contracción cruzada inversa",
     r"A_{\mu\nu}^{\rho} B_{\rho}^{\sigma} C_{\sigma}^{\mu}",
     [('ν', 'sub')]),

    ("088 — Dos libres separados por contracciones",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma}_{\lambda} D^{\lambda}_{\kappa}",
     [('μ', 'super'), ('ν', 'super'), ('κ', 'sub')]),

    ("089 — Cuatro tensores completamente contraídos",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\mu}",
     []),

    ("090 — Contracciones independientes and libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\lambda}",
     [('ρ', 'super'), ('λ', 'sub')]),

    ("091 — Tres índices libres",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma}_{\lambda} D^{\kappa}",
     [('μ', 'super'), ('ν', 'super'), ('λ', 'sub'), ('κ', 'super')]),

    ("092 — Tres índices libres mixtos",
     r"A_{\mu}^{\nu\rho} B_{\rho}^{\sigma} C_{\sigma\lambda}",
     [('μ', 'sub'), ('ν', 'super'), ('λ', 'sub')]),

    ("093 — Contracción con índice en posiciones opuestas",
     r"A^{\mu}_{\nu} B_{\rho}^{\nu} C^{\rho}_{\sigma}",
     [('μ', 'super'), ('σ', 'sub')]),

    ("094 — Contracción cruzada con dos libres",
     r"A^{\mu\nu}_{\rho} B_{\sigma}^{\rho} C^{\sigma}_{\lambda}",
     [('μ', 'super'), ('ν', 'super'), ('λ', 'sub')]),

    ("095 — Producto de escalares y tensor contraído",
     r"A B C^{\mu}_{\nu} D^{\nu}_{\mu}",
     []),

    ("096 — Escalar multiplicando tensor con libres",
     r"A B^{\mu}_{\nu} C^{\nu}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("097 — Cuatro factores con dos cadenas",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda} E^{\lambda}_{\sigma}",
     []),

    ("098 — Cadena cerrada con tensor libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda}",
     [('σ', 'super'), ('λ', 'sub')]),

    ("099 — Contracciones múltiples con tres libres",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma}_{\mu} D^{\lambda}_{\kappa}",
     [('ν', 'super'), ('λ', 'super'), ('κ', 'sub')]),

    ("100 — Estructura compleja completamente contraída",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\sigma}_{\kappa} E^{\kappa}_{\nu}",
     []),

    # =============================================================================
    # 101–120 — SUMAS, PRODUCTOS Y CONTRACCIONES EN EXPRESIONES COMPUESTAS
    # =============================================================================

    ("101 — Suma de escalares",
     r"A + B",
     []),

    ("102 — Suma de vectores contravariantes",
     r"A^{\mu} + B^{\mu}",
     [('μ', 'super')]),

    ("103 — Suma de vectores covariantes",
     r"A_{\mu} + B_{\mu}",
     [('μ', 'sub')]),

    ("104 — Suma de tensores mixtos",
     r"A^{\mu}_{\nu} + B^{\mu}_{\nu}",
     [('μ', 'super'), ('ν', 'sub')]),

    ("105 — Suma con productos escalares",
     r"A B + C D",
     []),

    ("106 — Suma de términos con la misma contracción",
     r"A^{\mu}_{\nu} B^{\nu} + C^{\mu}_{\rho} D^{\rho}",
     [('μ', 'super')]),

    ("107 — Suma de términos con dos libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} + C^{\mu}_{\sigma} D^{\sigma}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("108 — Suma de términos completamente contraídos",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} + C^{\rho}_{\sigma} D^{\sigma}_{\rho}",
     []),

    ("109 — Suma de cadenas de tres tensores",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho} + D^{\mu}_{\sigma} E^{\sigma}_{\lambda} F^{\lambda}",
     [('μ', 'super')]),

    ("110 — Suma con términos de estructura diferente",
     r"A^{\mu}_{\nu} B^{\nu} + C^{\mu}",
     [('μ', 'super')]),

    ("111 — Producto de una suma",
     r"(A^{\mu} + B^{\mu}) C_{\mu}",
     []),

    ("112 — Producto de suma de tensores",
     r"(A^{\mu}_{\nu} + B^{\mu}_{\nu}) C^{\nu}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("113 — Dos sumas contraídas",
     r"(A^{\mu} + B^{\mu})(C_{\mu} + D_{\mu})",
     []),

    ("114 — Dos sumas con índices libres",
     r"(A^{\mu}_{\nu} + B^{\mu}_{\nu})(C^{\nu}_{\rho} + D^{\nu}_{\rho})",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("115 — Suma de contracciones con índices distintos",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} + C^{\mu}_{\rho} D^{\rho}_{\mu}",
     []),

    ("116 — Suma con tres términos",
     r"A^{\mu}_{\nu} B^{\nu} + C^{\mu}_{\rho} D^{\rho} + E^{\mu}",
     [('μ', 'super')]),

    ("117 — Suma de términos con dos índices libres",
     r"A^{\mu\nu}_{\rho} B^{\rho} + C^{\mu\nu}_{\sigma} D^{\sigma}",
     [('μ', 'super'), ('ν', 'super')]),

    ("118 — Suma de cadenas cerradas y término libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} + C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\rho}",
     []),

    ("119 — Producto de dos sumas con contracciones cruzadas",
     r"(A^{\mu}_{\nu} + B^{\mu}_{\nu})(C^{\rho}_{\mu} + D^{\rho}_{\mu})",
     [('ρ', 'super'), ('ν', 'sub')]),

    ("120 — Expresión compuesta con múltiples sumas y contracciones",
     r"(A^{\mu}_{\nu} + B^{\mu}_{\nu}) C^{\nu}_{\rho} + D^{\mu}_{\sigma} (E^{\sigma}_{\rho} + F^{\sigma}_{\rho})",
     [('μ', 'super'), ('ρ', 'sub')]),

    # =============================================================================
    # 121–140 — PRODUCTOS ANIDADOS Y CONTRACCIONES COMPLEJAS
    # =============================================================================

    ("121 — Producto anidado simple",
     r"(A^{\mu} B_{\nu}) C^{\nu}",
     [('μ', 'super')]),

    ("122 — Producto anidado con dos libres",
     r"(A^{\mu} B_{\nu}) C^{\nu}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("123 — Producto anidado completamente contraído",
     r"(A^{\mu} B_{\nu}) C^{\nu}_{\mu}",
     []),

    ("124 — Dos productos anidados",
     r"(A^{\mu}_{\nu} B^{\nu})(C^{\rho}_{\sigma} D^{\sigma})",
     [('μ', 'super'), ('ρ', 'super')]),

    ("125 — Producto anidado con contracción cruzada",
     r"(A^{\mu\nu}_{\rho} B^{\rho})(C^{\sigma}_{\mu} D_{\sigma})",
     [('ν', 'super')]),

    ("126 — Tres niveles de anidamiento",
     r"((A^{\mu}_{\nu} B^{\nu}_{\rho}) C^{\rho}) D_{\sigma}",
     [('μ', 'super'), ('σ', 'sub')]),

    ("127 — Tres niveles completamente contraídos",
     r"((A^{\mu}_{\nu} B^{\nu}_{\rho}) C^{\rho}) D_{\mu}",
     []),

    ("128 — Cadena larga con un libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}",
     [('μ', 'super')]),

    ("129 — Cadena larga con dos libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa}",
     [('μ', 'super'), ('κ', 'sub')]),

    ("130 — Cadena larga completamente contraída",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\mu}",
     []),

    ("131 — Dos cadenas independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\sigma}",
     []),

    ("132 — Dos cadenas con libres distintos",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\lambda} D^{\sigma}_{\kappa} E^{\kappa}_{\sigma}",
     [('μ', 'super'), ('λ', 'sub')]),

    ("133 — Cadena dentro de producto anidado",
     r"(A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}) D^{\sigma}_{\mu} E_{\sigma}",
     []),

    ("134 — Producto de dos cadenas con libre común",
     r"(A^{\mu}_{\nu} B^{\nu})(C_{\rho} D^{\rho}_{\sigma})",
     [('μ', 'super'), ('σ', 'sub')]),

    ("135 — Contracción entre niveles anidados",
     r"(A^{\mu}_{\nu} B^{\nu}_{\rho})(C^{\rho}_{\sigma} D^{\sigma}_{\mu})",
     []),

    ("136 — Tres factores grouped",
     r"(A^{\mu}_{\nu} B^{\nu}_{\rho})(C^{\rho}_{\sigma} D^{\sigma}_{\lambda}) E^{\lambda}_{\mu}",
     []),

    ("137 — Estructura anidada con tres libres",
     r"(A^{\mu\nu}_{\rho} B^{\rho}_{\sigma}) C^{\sigma}_{\lambda} D^{\kappa}",
     [('μ', 'super'), ('ν', 'super'), ('λ', 'sub'), ('κ', 'super')]),

    ("138 — Contracciones cruzadas en grupos",
     r"(A^{\mu\nu}_{\rho} B^{\rho}_{\sigma})(C^{\sigma}_{\mu} D^{\lambda}_{\nu})",
     [('λ', 'super')]),

    ("139 — Producto de tres grupos contraídos",
     r"(A^{\mu}_{\nu} B^{\nu}_{\rho})(C^{\rho}_{\sigma} D^{\sigma}_{\lambda})(E^{\lambda}_{\mu})",
     []),

    ("140 — Estructura anidada máxima del bloque",
     r"((A^{\mu\nu}_{\rho} B^{\rho}_{\sigma}) C^{\sigma}_{\lambda})(D^{\lambda}_{\kappa} E^{\kappa}_{\mu}) F_{\nu}",
     []),

    # =============================================================================
    # 141–160 — CONTRACCIONES MÚLTIPLES Y CASOS LÍMITE
    # =============================================================================

    ("141 — Tres contracciones independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\rho} E^{\lambda}_{\kappa} F^{\kappa}_{\lambda}",
     []),

    ("142 — Dos cadenas y un índice libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa}",
     [('σ', 'super'), ('κ', 'sub')]),

    ("143 — Dos cadenas y dos índices libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\mu} E^{\lambda}_{\kappa}",
     [('λ', 'super'), ('κ', 'sub')]),

    ("144 — Cadena cerrada dentro de producto",
     r"A B^{\mu}_{\nu} C^{\nu}_{\rho} D^{\rho}_{\mu}",
     []),

    ("145 — Cadena abierta con escalar",
     r"A B^{\mu}_{\nu} C^{\nu}_{\rho} D^{\rho}_{\sigma}",
     [('μ', 'super'), ('σ', 'sub')]),

    ("146 — Cuatro índices libres",
     r"A^{\mu\nu}_{\rho\sigma}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("147 — Tensor rango 5",
     r"A^{\mu\nu\rho}_{\sigma\lambda}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'super'), ('σ', 'sub'), ('λ', 'sub')]),

    ("148 — Tensor rango 6",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'super'), ('σ', 'sub'), ('λ', 'sub'), ('κ', 'sub')]),

    ("149 — Tensor rango 7 mixto",
     r"A^{\mu\nu\rho\sigma}_{\lambda\kappa\tau\phi}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'super'), ('σ', 'super'),
      ('λ', 'sub'), ('κ', 'sub'), ('τ', 'sub'), ('φ', 'sub')]),

    ("150 — Producto de tensores de rango alto",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\sigma}_{\lambda\kappa}",
     [('μ', 'super'), ('ν', 'super'), ('λ', 'sub'), ('κ', 'sub')]),

    ("151 — Contracción doble entre tensores de rango 4",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\sigma}_{\mu\nu}",
     []),

    ("152 — Contracción parcial entre tensores de rango 4",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\lambda\sigma}_{\kappa}",
     [('μ', 'super'), ('ν', 'super'), ('λ', 'super'), ('κ', 'sub')]),

    ("153 — Tres contracciones cruzadas",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa} B^{\sigma\lambda\kappa}_{\mu\nu\rho}",
     []),

    ("154 — Contracción parcial rango 3 con rango 3",
     r"A^{\mu\nu}_{\rho} B^{\rho\sigma}_{\nu}",
     [('μ', 'super'), ('σ', 'super')]),

    ("155 — Contracción parcial con tres libres",
     r"A^{\mu\nu\rho}_{\sigma} B^{\sigma}_{\lambda}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'super'), ('λ', 'sub')]),

    ("156 — Dos contracciones y dos libres",
     r"A^{\mu\nu\rho}_{\sigma\lambda} B^{\sigma\lambda}_{\mu\kappa}",
     [('ν', 'super'), ('ρ', 'super'), ('κ', 'sub')]),

    ("157 — Cuatro contracciones independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\rho} E^{\lambda}_{\kappa} F^{\kappa}_{\lambda} G^{\tau}_{\phi} H^{\phi}_{\tau}",
     []),

    ("158 — Contracciones cruzadas con índice libre",
     r"A^{\mu\nu\rho}_{\sigma\lambda} B^{\sigma\lambda}_{\mu\kappa}",
     [('ν', 'super'), ('ρ', 'super'), ('κ', 'sub')]),

    ("159 — Cadena de rango alto",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\sigma}_{\kappa} E^{\kappa}_{\nu}",
     []),

    ("160 — Estructura compleja de rango alto",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa} B^{\sigma}_{\alpha} C^{\alpha}_{\mu} D^{\lambda}_{\beta} E^{\beta}_{\nu} F^{\kappa}_{\gamma} G^{\gamma}_{\rho}",
     []),

    # =============================================================================
    # 161–180 — CONTRACCIONES PROFUNDAS Y TENSORES DE RANGO ALTO
    # =============================================================================

    ("161 — Contracción simple entre tensores de rango 5",
     r"A^{\mu\nu\rho}_{\sigma\lambda} B^{\sigma\lambda}_{\alpha\beta\kappa}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'super'),
      ('α', 'sub'), ('β', 'sub'), ('κ', 'sub')]),

    ("162 — Dos contracciones entre tensores de rango 5",
     r"A^{\mu\nu\rho}_{\sigma\lambda} B^{\sigma\lambda\kappa}_{\mu\alpha\beta}",
     [('ν', 'super'), ('ρ', 'super'), ('κ', 'super'),
      ('α', 'sub'), ('β', 'sub')]),

    ("163 — Tres contracciones entre tensores de rango 5",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa} B^{\sigma\lambda\kappa}_{\mu\alpha\beta}",
     [('ν', 'super'), ('ρ', 'super'),
      ('α', 'sub'), ('β', 'sub')]),

    ("164 — Cadena de rango alto con un libre",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\sigma}_{\kappa} E^{\kappa}_{\alpha}",
     [('ν', 'super'), ('α', 'sub')]),

    ("165 — Cadena de rango alto completamente cerrada",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\sigma}_{\kappa} E^{\kappa}_{\nu}",
     []),

    ("166 — Dos cadenas conectadas",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\mu} E^{\lambda}_{\kappa} F^{\kappa}_{\lambda}",
     []),

    ("167 — Dos cadenas conectadas con libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\lambda} D^{\sigma}_{\kappa} E^{\kappa}_{\sigma} F^{\lambda}_{\alpha}",
     [('μ', 'super'), ('α', 'sub')]),

    ("168 — Tres bloques independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\rho} E^{\lambda}_{\kappa} F^{\kappa}_{\tau}",
     [('λ', 'super'), ('τ', 'sub')]),

    ("169 — Bloques con diferentes rangos",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma}_{\lambda\kappa} D^{\lambda} E^{\kappa}",
     [('μ', 'super'), ('ν', 'super')]),

    ("170 — Cuatro libres provenientes de un producto",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\lambda\kappa}",
     [('μ', 'super'), ('ν', 'super'),
      ('λ', 'super'), ('κ', 'super'), ('σ', 'sub')]),

    ("171 — Cinco índices libres",
     r"A^{\mu\nu}_{\rho} B^{\rho} C^{\lambda\kappa}_{\sigma}",
     [('μ', 'super'), ('ν', 'super'),
      ('λ', 'super'), ('κ', 'super'), ('σ', 'sub')]),

    ("172 — Contracción doble y cuatro libres",
     r"A^{\mu\nu\rho}_{\sigma\lambda} B^{\sigma\lambda}_{\alpha\mu}",
     [('ν', 'super'), ('ρ', 'super'),
      ('α', 'sub')]),

    ("173 — Contracción triple con índices libres mixtos",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa} B^{\sigma\lambda}_{\mu\alpha}",
     [('ν', 'super'), ('ρ', 'super'),
      ('κ', 'sub'), ('α', 'sub')]),

    ("174 — Cadena de seis tensores",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\mu}",
     []),

    ("175 — Cadena de seis tensores abierta",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\tau}",
     [('μ', 'super'), ('τ', 'sub')]),

    ("176 — Dos cadenas largas independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\tau} G^{\tau}_{\sigma}",
     []),

    ("177 — Cadena larga con tensor adicional libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\mu} F^{\alpha}_{\beta}",
     [('α', 'super'), ('β', 'sub')]),

    ("178 — Rango alto con dos cadenas internas",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa} B^{\sigma}_{\alpha} C^{\alpha}_{\mu} D^{\lambda}_{\beta} E^{\beta}_{\nu} F^{\kappa}_{\gamma}",
     [('ρ', 'super'), ('γ', 'sub')]),

    ("179 — Rango alto completamente contraído",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa} B^{\sigma}_{\alpha} C^{\alpha}_{\mu} D^{\lambda}_{\beta} E^{\beta}_{\nu} F^{\kappa}_{\rho}",
     []),

    ("180 — Estructura compleja con múltiples cadenas",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\sigma}_{\kappa} E^{\kappa}_{\alpha} F^{\tau}_{\nu} G^{\alpha}_{\tau}",
     []),

    # =============================================================================
    # 181–200 — SUMAS COMPLEJAS Y CONTRACCIONES ENTRE TÉRMINOS
    # =============================================================================

    ("181 — Suma de dos escalares contraídos",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} + C^{\rho}_{\sigma} D^{\sigma}_{\rho}",
     []),

    ("182 — Suma de dos vectores contravariantes",
     r"A^{\mu} + B^{\mu}",
     [('μ', 'super')]),

    ("183 — Suma de dos vectores covariantes",
     r"A_{\mu} + B_{\mu}",
     [('μ', 'sub')]),

    ("184 — Suma de productos con el mismo índice libre",
     r"A^{\mu}_{\nu} B^{\nu} + C^{\mu}_{\rho} D^{\rho}",
     [('μ', 'super')]),

    ("185 — Suma de productos con dos índices libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} + C^{\mu}_{\sigma} D^{\sigma}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("186 — Suma de términos completamente contraídos de distinto tamaño",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} + C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\rho}",
     []),

    ("187 — Suma de cadenas abiertas equivalentes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} + C^{\mu}_{\sigma} D^{\sigma}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("188 — Suma de tres términos con dos libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} + C^{\mu}_{\sigma} D^{\sigma}_{\rho} + E^{\mu}_{\lambda} F^{\lambda}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("189 — Suma de términos con tres libres",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} + C^{\mu\nu}_{\lambda} D^{\lambda}_{\sigma}",
     [('μ', 'super'), ('ν', 'super'), ('σ', 'sub')]),

    ("190 — Suma de términos con cuatro libres",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma\lambda} + C^{\mu\nu}_{\kappa} D^{\kappa}_{\sigma\lambda}",
     [('μ', 'super'), ('ν', 'super'), ('σ', 'sub'), ('λ', 'sub')]),

    ("191 — Suma de contracciones dobles",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\sigma}_{\mu\nu} + C^{\lambda\kappa}_{\alpha\beta} D^{\alpha\beta}_{\lambda\kappa}",
     []),

    ("192 — Suma de contracciones parciales",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\sigma}_{\mu\lambda} + C^{\alpha\nu}_{\beta\sigma} D^{\beta\sigma}_{\alpha\lambda}",
     [('ν', 'super'), ('λ', 'sub')]),

    ("193 — Suma con tres índices libres",
     r"A^{\mu\nu\rho}_{\sigma} B^{\sigma}_{\lambda} + C^{\mu\nu\rho}_{\kappa} D^{\kappa}_{\lambda}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'super'), ('λ', 'sub')]),

    ("194 — Suma de cadenas largas",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\lambda} + D^{\mu}_{\sigma} E^{\sigma}_{\tau} F^{\tau}_{\lambda}",
     [('μ', 'super'), ('λ', 'sub')]),

    ("195 — Suma de dos cadenas cerradas",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} + D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\sigma}",
     []),

    ("196 — Suma de estructuras de rango diferente",
     r"A^{\mu}_{\nu} B^{\nu} + C^{\mu\rho}_{\sigma} D^{\sigma}_{\rho}",
     [('μ', 'super')]),

    ("197 — Suma con tensor adicional de índice libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho} + D^{\mu}_{\sigma} E^{\sigma}_{\lambda} F^{\lambda}",
     [('μ', 'super')]),

    ("198 — Suma de dos términos completamente abiertos",
     r"A^{\mu\nu}_{\rho\sigma} + B^{\mu\nu}_{\rho\sigma}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("199 — Suma de productos con cinco índices libres",
     r"A^{\mu\nu}_{\rho} B^{\lambda\kappa}_{\sigma} + C^{\mu\nu}_{\rho} D^{\lambda\kappa}_{\sigma}",
     [('μ', 'super'), ('ν', 'super'), ('λ', 'super'), ('κ', 'super'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("200 — Suma compleja de cadenas y contracciones",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} + D^{\mu}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\sigma} + G^{\mu}_{\tau} H^{\tau}_{\phi} I^{\phi}_{\sigma}",
     [('μ', 'super'), ('σ', 'sub')]),

    # =============================================================================
    # 201–220 — SUMAS, PRODUCTOS Y CONTRACCIONES MIXTAS
    # =============================================================================

    ("201 — Producto de dos vectores con contracción",
     r"A^{\mu} B_{\mu}",
     []),

    ("202 — Producto de vectores con un índice libre",
     r"A^{\mu} B_{\nu} C^{\nu}",
     [('μ', 'super')]),

    ("203 — Producto con libre covariante",
     r"A_{\mu} B^{\nu} C_{\nu}",
     [('μ', 'sub')]),

    ("204 — Dos productos independientes con libres diferentes",
     r"A^{\mu} B_{\mu} C^{\nu}",
     [('ν', 'super')]),

    ("205 — Dos contracciones y un libre",
     r"A^{\mu\nu} B_{\mu} C_{\nu} D_{\rho}",
     [('ρ', 'sub')]),

    ("206 — Dos contracciones y dos libres",
     r"A^{\mu\nu} B_{\mu} C_{\nu} D^{\rho}_{\sigma}",
     [('ρ', 'super'), ('σ', 'sub')]),

    ("207 — Contracción dentro de producto de rango 2",
     r"A^{\mu\nu} B_{\nu\rho} C^{\rho}",
     [('μ', 'super')]),

    ("208 — Contracción cruzada de tres tensores",
     r"A^{\mu}_{\nu} B^{\nu\rho} C_{\rho\sigma}",
     [('μ', 'super'), ('σ', 'sub')]),

    ("209 — Cadena mixta con un libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}",
     [('μ', 'super')]),

    ("210 — Cadena mixta con libre covariante",
     r"A_{\mu}^{\nu} B_{\nu}^{\rho} C_{\rho}",
     [('μ', 'sub')]),

    ("211 — Cadena de cuatro tensores abierta",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}",
     [('μ', 'super')]),

    ("212 — Cadena de cuatro tensores invertida",
     r"A_{\mu}^{\nu} B_{\nu}^{\rho} C_{\rho}^{\sigma} D_{\sigma}",
     [('μ', 'sub')]),

    ("213 — Producto de tensor rango 2 con dos vectores",
     r"A^{\mu\nu} B_{\mu} C_{\nu}",
     []),

    ("214 — Producto de tensor covariante con dos vectores",
     r"A_{\mu\nu} B^{\mu} C^{\nu}",
     []),

    ("215 — Tensor mixto con dos contracciones",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\mu} C^{\sigma}_{\nu}",
     []),

    ("216 — Tensor mixto con una contracción y dos libres",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\mu} C^{\sigma}_{\lambda}",
     [('ν', 'super'), ('λ', 'sub')]),

    ("217 — Producto con tres contracciones independientes",
     r"A^{\mu\nu\rho}_{\alpha\beta\gamma} B^{\alpha}_{\mu} C^{\beta}_{\nu} D^{\gamma}_{\rho}",
     []),

    ("218 — Producto con tres contracciones and un libre",
     r"A^{\mu\nu\rho}_{\alpha\beta\gamma} B^{\alpha}_{\mu} C^{\beta}_{\nu} D^{\gamma}_{\sigma}",
     [('ρ', 'super'), ('σ', 'sub')]),

    ("219 — Suma de productos con libre contravariante",
     r"A^{\mu}_{\nu} B^{\nu} + C^{\mu}_{\rho} D^{\rho}",
     [('μ', 'super')]),

    ("220 — Suma de productos con libre covariante",
     r"A_{\mu}^{\nu} B_{\nu} + C_{\mu}^{\rho} D_{\rho}",
     [('μ', 'sub')]),

    # =============================================================================
    # 221–240 — CONTRACCIONES MÚLTIPLES, CADENAS Y ESTRUCTURAS PROFUNDAS
    # =============================================================================

    ("221 — Suma de tres términos con una contracción",
     r"A^{\mu}_{\nu} B^{\nu} + C^{\mu}_{\rho} D^{\rho} + E^{\mu}_{\sigma} F^{\sigma}",
     [('μ', 'super')]),

    ("222 — Suma de tres términos con libre covariante",
     r"A_{\mu}^{\nu} B_{\nu} + C_{\mu}^{\rho} D_{\rho} + E_{\mu}^{\sigma} F_{\sigma}",
     [('μ', 'sub')]),

    ("223 — Suma de términos con dos libres mixtos",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} + C^{\mu}_{\sigma} D^{\sigma}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("224 — Suma de términos con tres libres",
     r"A^{\mu\nu}_{\rho} B^{\rho} + C^{\mu\nu}_{\sigma} D^{\sigma}",
     [('μ', 'super'), ('ν', 'super')]),

    ("225 — Suma de productos con cuatro libres",
     r"A^{\mu\nu}_{\rho} B^{\lambda}_{\sigma} + C^{\mu\nu}_{\rho} D^{\lambda}_{\sigma}",
     [('μ', 'super'), ('ν', 'super'), ('λ', 'super'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("226 — Doble contracción cruzada",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\sigma}_{\mu\lambda}",
     [('ν', 'super'), ('λ', 'sub')]),

    ("227 — Triple contracción cruzada",
     r"A^{\mu\nu\rho}_{\alpha\beta\gamma} B^{\alpha\beta}_{\mu\nu} C^{\gamma}_{\rho}",
     []),

    ("228 — Triple contracción con dos libres",
     r"A^{\mu\nu\rho}_{\alpha\beta\gamma} B^{\alpha\beta}_{\mu\lambda} C^{\gamma}_{\rho}",
     [('ν', 'super'), ('λ', 'sub')]),

    ("229 — Cadena de cinco tensores abierta",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\tau}",
     [('μ', 'super'), ('τ', 'sub')]),

    ("230 — Cadena de cinco tensores cerrada",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\mu}",
     []),

    ("231 — Dos cadenas abiertas independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\lambda}_{\kappa} E^{\kappa}_{\tau}",
     [('μ', 'super'), ('σ', 'sub'), ('λ', 'super'), ('τ', 'sub')]),

    ("232 — Dos cadenas cerradas independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\rho} E^{\lambda}_{\kappa} F^{\kappa}_{\lambda}",
     []),

    ("233 — Cadena conectada a tensor de rango 2",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho\sigma}_{\lambda} D^{\lambda}_{\mu}",
     [('σ', 'super')]),

    ("234 — Cadena conectada a tensor covariante",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho\sigma} D_{\sigma\lambda}",
     [('μ', 'super'), ('λ', 'sub')]),

    ("235 — Cadena conectada a tensor contravariante",
     r"A_{\mu}^{\nu} B_{\nu}^{\rho} C_{\rho\sigma} D^{\sigma\lambda}",
     [('μ', 'sub'), ('λ', 'super')]),

    ("236 — Tensor de rango 4 con tres contracciones",
     r"A^{\mu\nu\rho\sigma}_{\alpha\beta\gamma\delta} B^{\alpha}_{\mu} C^{\beta}_{\nu} D^{\gamma}_{\rho} E^{\delta}_{\lambda}",
     [('σ', 'super'), ('λ', 'sub')]),

    ("237 — Tensor de rango 4 completamente contraído",
     r"A^{\mu\nu\rho\sigma}_{\alpha\beta\gamma\delta} B^{\alpha}_{\mu} C^{\beta}_{\nu} D^{\gamma}_{\rho} E^{\delta}_{\sigma}",
     []),

    ("238 — Dos bloques de rango alto con contracciones",
     r"A^{\mu\nu\rho}_{\alpha\beta\gamma} B^{\alpha\beta}_{\mu\lambda} C^{\gamma}_{\rho} D^{\lambda}_{\sigma}",
     [('ν', 'super'), ('σ', 'sub')]),

    ("239 — Estructura de rango alto completamente cerrada",
     r"A^{\mu\nu\rho}_{\alpha\beta\gamma} B^{\alpha}_{\mu} C^{\beta}_{\nu} D^{\gamma}_{\lambda} E^{\lambda}_{\rho}",
     []),

    ("240 — Estructura profunda con dos cadenas y contracciones cruzadas",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\sigma}_{\kappa} E^{\kappa}_{\alpha} F^{\alpha}_{\nu}",
     []),

    # =============================================================================
    # 241–260 — CONTRACCIONES MÚLTIPLES Y ESTRUCTURAS MIXTAS
    # =============================================================================

    ("241 — Contracción simple con cuatro índices libres",
     r"A^{\mu\nu\rho}_{\sigma} B^{\sigma}_{\lambda\kappa}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'super'),
      ('λ', 'sub'), ('κ', 'sub')]),

    ("242 — Dos contracciones con cuatro libres",
     r"A^{\mu\nu\rho}_{\sigma\lambda} B^{\sigma\lambda}_{\kappa\tau}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'super'),
      ('κ', 'sub'), ('τ', 'sub')]),

    ("243 — Tres contracciones con tres libres",
     r"A^{\mu\nu\rho\sigma}_{\alpha\beta\gamma} B^{\alpha\beta\gamma}_{\mu\nu\lambda}",
     [('ρ', 'super'), ('σ', 'super'), ('λ', 'sub')]),

    ("244 — Contracción cruzada de tres tensores",
     r"A^{\mu\nu}_{\rho} B^{\rho\lambda}_{\sigma} C^{\sigma}_{\mu\kappa}",
     [('ν', 'super'), ('λ', 'super'), ('κ', 'sub')]),

    ("245 — Contracción cruzada con dos índices compartidos",
     r"A^{\mu\nu\rho}_{\sigma\lambda} B^{\sigma\lambda}_{\mu\kappa} C^{\kappa}_{\nu}",
     [('ρ', 'super')]),

    ("246 — Cadena con tensor de rango tres",
     r"A^{\mu}_{\nu} B^{\nu\rho}_{\sigma} C^{\sigma}_{\mu\lambda}",
     [('ρ', 'super'), ('λ', 'sub')]),

    ("247 — Cadena cerrada con tensor de rango tres",
     r"A^{\mu}_{\nu} B^{\nu\rho}_{\sigma} C^{\sigma}_{\mu\rho}",
     []),

    ("248 — Dos cadenas con índices libres diferentes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\lambda} D^{\sigma}_{\kappa} E^{\kappa}_{\tau}",
     [('μ', 'super'), ('λ', 'sub'),
      ('σ', 'super'), ('τ', 'sub')]),

    ("249 — Dos cadenas conectadas por un índice",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\lambda} D^{\lambda}_{\sigma} E^{\sigma}_{\kappa}",
     [('μ', 'super'), ('κ', 'sub')]),

    ("250 — Cadena larga con tensor de rango dos",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho\lambda}_{\sigma} D^{\sigma}_{\mu\kappa}",
     [('λ', 'super'), ('κ', 'sub')]),

    ("251 — Dos contracciones internas y un bloque abierto",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\lambda}",
     [('ρ', 'super'), ('λ', 'sub')]),

    ("252 — Tres bloques: dos cerrados y uno abierto",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\rho} E^{\lambda}_{\kappa} F^{\kappa}_{\tau}",
     [('λ', 'super'), ('τ', 'sub')]),

    ("253 — Cuatro contracciones independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\rho} E^{\lambda}_{\kappa} F^{\kappa}_{\lambda} G^{\tau}_{\phi} H^{\phi}_{\tau}",
     []),

    ("254 — Producto de tensor abierto y escalar contraído",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\alpha}_{\beta} E^{\beta}_{\alpha}",
     [('ν', 'super'), ('σ', 'sub')]),

    ("255 — Tensor de rango cuatro con dos cadenas",
     r"A^{\mu\nu\rho\sigma}_{\alpha\beta\gamma\delta} B^{\alpha}_{\mu} C^{\beta}_{\nu} D^{\gamma}_{\rho} E^{\delta}_{\lambda}",
     [('σ', 'super'), ('λ', 'sub')]),

    ("256 — Tensor de rango cuatro completamente contraído",
     r"A^{\mu\nu\rho\sigma}_{\alpha\beta\gamma\delta} B^{\alpha}_{\mu} C^{\beta}_{\nu} D^{\gamma}_{\rho} E^{\delta}_{\sigma}",
     []),

    ("257 — Dos tensores de rango cuatro parcialmente contraídos",
     r"A^{\mu\nu\rho\sigma}_{\alpha\beta} B^{\alpha\beta}_{\mu\nu\lambda\kappa}",
     [('ρ', 'super'), ('σ', 'super'),
      ('λ', 'sub'), ('κ', 'sub')]),

    ("258 — Contracción múltiple con tres tensores",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\sigma\lambda}_{\mu\kappa} C^{\kappa}_{\nu}",
     [('λ', 'super')]),

    ("259 — Estructura cerrada con cinco tensores",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\mu}",
     []),

    ("260 — Estructura abierta con cinco tensores",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa}",
     [('μ', 'super'), ('κ', 'sub')]),

    # =============================================================================
    # 261–280 — SUMAS, BLOQUES INDEPENDIENTES Y CONTRACCIONES COMPLEJAS
    # =============================================================================

    ("261 — Suma de dos productos con tres índices libres",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} + C^{\mu\nu}_{\lambda} D^{\lambda}_{\sigma}",
     [('μ', 'super'), ('ν', 'super'), ('σ', 'sub')]),

    ("262 — Suma de tres cadenas abiertas",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} + C^{\mu}_{\sigma} D^{\sigma}_{\rho} + E^{\mu}_{\lambda} F^{\lambda}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("263 — Suma de dos términos con los mismos índices libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} + C^{\mu}_{\sigma} D^{\sigma}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("264 — Suma de dos estructuras de rango tres",
     r"A^{\mu\nu\rho}_{\sigma} B^{\sigma}_{\lambda} + C^{\mu\nu\rho}_{\kappa} D^{\kappa}_{\lambda}",
     [('μ', 'super'), ('ν', 'super'), ('ρ', 'super'),
      ('λ', 'sub')]),

    ("265 — Suma con dos contracciones independientes",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\mu} C^{\sigma}_{\nu} + D^{\lambda\kappa}_{\alpha\beta} E^{\alpha}_{\lambda} F^{\beta}_{\kappa}",
     []),

    ("266 — Suma con un índice libre común",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\nu} + C^{\mu\lambda}_{\sigma} D^{\sigma}_{\lambda}",
     [('μ', 'super')]),

    ("267 — Suma de contracciones parciales con índices libres coincidentes",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\mu} + C^{\mu\nu}_{\alpha\sigma} D^{\alpha}_{\mu}",
     [('ν', 'super'), ('σ', 'sub')]),

    ("268 — Tres términos completamente contraídos",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} + C^{\rho}_{\sigma} D^{\sigma}_{\rho} + E^{\lambda}_{\kappa} F^{\kappa}_{\lambda}",
     []),

    ("269 — Suma de cadenas de diferente longitud",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} + C^{\mu}_{\sigma} D^{\sigma}_{\tau} E^{\tau}_{\rho}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("270 — Suma de estructuras con cuatro libres",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma\lambda} + C^{\mu\nu}_{\kappa} D^{\kappa}_{\sigma\lambda}",
     [('μ', 'super'), ('ν', 'super'),
      ('σ', 'sub'), ('λ', 'sub')]),

    ("271 — Producto de dos bloques parcialmente contraídos",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\sigma}_{\kappa} D^{\lambda\kappa}_{\alpha}",
     [('μ', 'super'), ('ν', 'super'), ('α', 'sub')]),

    ("272 — Producto con dos cadenas internas",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa} B^{\sigma}_{\alpha} C^{\alpha}_{\mu} D^{\lambda}_{\beta} E^{\beta}_{\nu} F^{\kappa}_{\gamma}",
     [('ρ', 'super'), ('γ', 'sub')]),

    ("273 — Producto completamente cerrado de rango alto",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa} B^{\sigma}_{\alpha} C^{\alpha}_{\mu} D^{\lambda}_{\beta} E^{\beta}_{\nu} F^{\kappa}_{\rho}",
     []),

    ("274 — Dos bloques abiertos independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\alpha}_{\beta} D^{\beta}_{\gamma}",
     [('μ', 'super'), ('ρ', 'sub'),
      ('α', 'super'), ('γ', 'sub')]),

    ("275 — Tres bloques abiertos independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\alpha}_{\beta} D^{\beta}_{\gamma} E^{\lambda}_{\kappa} F^{\kappa}_{\tau}",
     [('μ', 'super'), ('ρ', 'sub'),
      ('α', 'super'), ('γ', 'sub'),
      ('λ', 'super'), ('τ', 'sub')]),

    ("276 — Bloque cerrado más dos bloques abiertos",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\alpha}_{\beta} F^{\beta}_{\gamma}",
     [('ρ', 'super'), ('λ', 'sub'),
      ('α', 'super'), ('γ', 'sub')]),

    ("277 — Cadena cruzada de cuatro índices",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\nu} D^{\sigma}_{\kappa}",
     [('μ', 'super'), ('κ', 'sub')]),

    ("278 — Cadena cruzada completamente cerrada",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\nu} D^{\sigma}_{\mu}",
     []),

    ("279 — Suma de dos estructuras complejas",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\sigma}_{\kappa} + E^{\mu\nu}_{\alpha\beta} F^{\alpha}_{\gamma} G^{\gamma}_{\mu} H^{\beta}_{\kappa}",
     [('ν', 'super'), ('κ', 'sub')]),

    ("280 — Estructura compleja máxima del bloque",
     r"A^{\mu\nu\rho}_{\sigma\lambda\kappa} B^{\sigma}_{\alpha} C^{\alpha}_{\mu} D^{\lambda}_{\beta} E^{\beta}_{\nu} F^{\kappa}_{\gamma} G^{\gamma}_{\rho} + H^{\mu\nu\rho}_{\delta\epsilon\zeta} I^{\delta}_{a} J^{a}_{\mu} K^{\epsilon}_{b} L^{b}_{\nu} M^{\zeta}_{c} N^{c}_{\rho}",
     []),

    # =============================================================================
    # 281–300 — DERIVADAS COVARIANTES Y PARCIALES
    # =============================================================================

    ("281 — Derivada covariante de escalar",
     r"\nabla_{\mu}(A)",
     [('μ', 'sub')]),

    ("282 — Derivada parcial de escalar",
     r"\partial_{\mu}(A)",
     [('μ', 'sub')]),

    ("283 — Derivada covariante de vector contravariante",
     r"\nabla_{\mu}(A^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("284 — Derivada covariante de vector covariante",
     r"\nabla_{\mu}(A_{\nu})",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("285 — Derivada parcial de vector contravariante",
     r"\partial_{\mu}(A^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("286 — Derivada parcial de tensor covariante",
     r"\partial_{\mu}(A_{\nu\rho})",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("287 — Derivada covariante de tensor mixto",
     r"\nabla_{\mu}(A^{\nu}_{\rho})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("288 — Derivada covariante de tensor rango 3",
     r"\nabla_{\mu}(A^{\nu\rho}_{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'super'), ('σ', 'sub')]),

    ("289 — Derivada parcial de tensor mixto rango 3",
     r"\partial_{\mu}(A^{\nu}_{\rho\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("290 — Derivada covariante con contracción interna",
     r"\nabla_{\mu}(A^{\mu}_{\nu})",
     [('ν', 'sub')]),

    ("291 — Derivada covariante con índice derivativo contraído",
     r"\nabla_{\mu}(A^{\nu\mu})",
     [('ν', 'super')]),

    ("292 — Derivada parcial con contracción interna",
     r"\partial_{\mu}(A^{\mu\nu})",
     [('ν', 'super')]),

    ("293 — Derivada de producto escalar",
     r"\nabla_{\mu}(A B)",
     [('μ', 'sub')]),

    ("294 — Derivada de producto de vectores",
     r"\nabla_{\mu}(A^{\nu} B_{\rho})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("295 — Derivada de producto con contracción",
     r"\nabla_{\mu}(A^{\nu} B_{\nu})",
     [('μ', 'sub')]),

    ("296 — Derivada parcial de producto contraído",
     r"\partial_{\mu}(A^{\nu} B_{\nu})",
     [('μ', 'sub')]),

    ("297 — Derivada de producto con dos libres",
     r"\nabla_{\mu}(A^{\nu} B_{\rho} C^{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'super')]),

    ("298 — Derivada de producto completamente contraído",
     r"\nabla_{\mu}(A^{\nu}_{\rho} B^{\rho}_{\nu})",
     [('μ', 'sub')]),

    ("299 — Derivada parcial de producto mixto",
     r"\partial_{\mu}(A^{\nu}_{\rho} B^{\rho}_{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('σ', 'sub')]),

    ("300 — Derivada covariante de cadena contraída",
     r"\nabla_{\mu}(A^{\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma})",
     [('μ', 'sub'), ('ν', 'super')]),

    # =============================================================================
    # 301–320 — DERIVADAS COMPUESTAS, CONTRACCIONES Y SUMAS
    # =============================================================================

    ("301 — Segunda derivada covariante de escalar",
     r"\nabla_{\mu}(\nabla_{\nu}(A))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("302 — Segunda derivada parcial de escalar",
     r"\partial_{\mu}(\partial_{\nu}(A))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("303 — Derivada covariante aplicada a derivada de vector",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super')]),

    ("304 — Derivada covariante compuesta con índice contraído",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\nu}))",
     [('μ', 'sub')]),

    ("305 — Derivada compuesta con contracción externa",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho}) B_{\rho})",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("306 — Derivada de producto dentro de derivada",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho} B_{\rho}))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("307 — Segunda derivada con dos índices libres del tensor",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho\sigma}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('σ', 'super')]),

    ("308 — Segunda derivada con tensor covariante",
     r"\nabla_{\mu}(\nabla_{\nu}(A_{\rho\sigma}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("309 — Segunda derivada de tensor mixto",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho}_{\sigma}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('σ', 'sub')]),

    ("310 — Derivada externa de producto contraído",
     r"\nabla_{\mu}(A^{\nu}_{\rho} B^{\rho}_{\nu})",
     [('μ', 'sub')]),

    ("311 — Derivada externa de cadena abierta",
     r"\nabla_{\mu}(A^{\nu}_{\rho} B^{\rho}_{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('σ', 'sub')]),

    ("312 — Derivada externa de cadena cerrada",
     r"\nabla_{\mu}(A^{\nu}_{\rho} B^{\rho}_{\nu})",
     [('μ', 'sub')]),

    ("313 — Suma de derivadas de escalares",
     r"\nabla_{\mu}(A) + \partial_{\mu}(B)",
     [('μ', 'sub')]),

    ("314 — Suma de derivadas de vectores",
     r"\nabla_{\mu}(A^{\nu}) + \partial_{\mu}(B^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("315 — Suma de derivadas de vectores covariantes",
     r"\nabla_{\mu}(A_{\nu}) + \partial_{\mu}(B_{\nu})",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("316 — Suma de derivadas de productos",
     r"\nabla_{\mu}(A^{\nu} B_{\nu}) + \partial_{\mu}(C^{\rho} D_{\rho})",
     [('μ', 'sub')]),

    ("317 — Suma de derivadas con dos índices libres",
     r"\nabla_{\mu}(A^{\nu} B_{\rho}) + \partial_{\mu}(C^{\nu} D_{\rho})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("318 — Derivada de suma de vectores",
     r"\nabla_{\mu}(A^{\nu} + B^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("319 — Derivada de suma de tensores mixtos",
     r"\nabla_{\mu}(A^{\nu}_{\rho} + B^{\nu}_{\rho})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("320 — Estructura compuesta de derivadas y contracciones",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho}_{\sigma} B^{\sigma}_{\rho}) + \partial_{\nu}(C^{\lambda} D_{\lambda}))",
     [('μ', 'sub'), ('ν', 'sub')]),

    # =============================================================================
    # 321–340 — DERIVADAS Y DERIVADAS COVARIANTES BÁSICAS
    # =============================================================================

    ("321 — Derivada parcial de escalar",
     r"\partial_{\mu}{A}",
     [('μ', 'sub')]),

    ("322 — Derivada covariante de escalar",
     r"\nabla_{\mu}{A}",
     [('μ', 'sub')]),

    ("323 — Derivada parcial de vector contravariante",
     r"\partial_{\mu}{A^{\nu}}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("324 — Derivada covariante de vector contravariante",
     r"\nabla_{\mu}{A^{\nu}}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("325 — Derivada parcial de vector covariante",
     r"\partial_{\mu}{A_{\nu}}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("326 — Derivada covariante de vector covariante",
     r"\nabla_{\mu}{A_{\nu}}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("327 — Derivada parcial de tensor mixto",
     r"\partial_{\mu}{A^{\nu}_{\rho}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("328 — Derivada covariante de tensor mixto",
     r"\nabla_{\mu}{A^{\nu}_{\rho}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("329 — Derivada parcial de tensor rango 2 contravariante",
     r"\partial_{\mu}{A^{\nu\rho}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'super')]),

    ("330 — Derivada covariante de tensor rango 2 contravariante",
     r"\nabla_{\mu}{A^{\nu\rho}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'super')]),

    ("331 — Derivada parcial de tensor rango 2 covariante",
     r"\partial_{\mu}{A_{\nu\rho}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("332 — Derivada covariante de tensor rango 2 covariante",
     r"\nabla_{\mu}{A_{\nu\rho}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("333 — Derivada parcial de tensor mixto rango 3",
     r"\partial_{\mu}{A^{\nu\rho}_{\sigma}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'super'), ('σ', 'sub')]),

    ("334 — Derivada covariante de tensor mixto rango 3",
     r"\nabla_{\mu}{A^{\nu\rho}_{\sigma}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'super'), ('σ', 'sub')]),

    ("335 — Derivada parcial de tensor rango 3 covariante",
     r"\partial_{\mu}{A_{\nu\rho\sigma}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("336 — Derivada covariante de tensor rango 3 covariante",
     r"\nabla_{\mu}{A_{\nu\rho\sigma}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("337 — Derivada parcial de producto escalar",
     r"\partial_{\mu}{A B}",
     [('μ', 'sub')]),

    ("338 — Derivada covariante de producto escalar",
     r"\nabla_{\mu}{A B}",
     [('μ', 'sub')]),

    ("339 — Derivada parcial de producto tensorial",
     r"\partial_{\mu}{A^{\nu} B_{\rho}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("340 — Derivada covariante de producto tensorial",
     r"\nabla_{\mu}{A^{\nu} B_{\rho}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    # =============================================================================
    # 341–360 — COMBINACIÓN DE DERIVADAS, PRODUCTOS, SUMAS Y CONTRACCIONES
    # =============================================================================

    ("341 — Derivada parcial de producto de dos vectores",
     r"\partial_{\mu}{A^{\nu} B_{\rho}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("342 — Derivada covariante de producto de dos vectores",
     r"\nabla_{\mu}{A^{\nu} B_{\rho}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("343 — Derivada parcial de producto con contracción interna",
     r"\partial_{\mu}{A^{\nu} B_{\nu}}",
     [('μ', 'sub')]),

    ("344 — Derivada covariante de producto con contracción interna",
     r"\nabla_{\mu}{A^{\nu} B_{\nu}}",
     [('μ', 'sub')]),

    ("345 — Derivada parcial de producto de tensores",
     r"\partial_{\mu}{A^{\nu\rho} B_{\sigma\lambda}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'super'), ('σ', 'sub'), ('λ', 'sub')]),

    ("346 — Derivada covariante de producto de tensores",
     r"\nabla_{\mu}{A^{\nu\rho} B_{\sigma\lambda}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'super'), ('σ', 'sub'), ('λ', 'sub')]),

    ("347 — Derivada parcial de producto con una contracción",
     r"\partial_{\mu}{A^{\nu\rho} B_{\rho\sigma}}",
     [('μ', 'sub'), ('ν', 'super'), ('σ', 'sub')]),

    ("348 — Derivada covariante de producto con una contracción",
     r"\nabla_{\mu}{A^{\nu\rho} B_{\rho\sigma}}",
     [('μ', 'sub'), ('ν', 'super'), ('σ', 'sub')]),

    ("349 — Derivada parcial de producto completamente contraído",
     r"\partial_{\mu}{A^{\nu}_{\rho} B^{\rho}_{\nu}}",
     [('μ', 'sub')]),

    ("350 — Derivada covariante de producto completamente contraído",
     r"\nabla_{\mu}{A^{\nu}_{\rho} B^{\rho}_{\nu}}",
     [('μ', 'sub')]),

    ("351 — Segunda derivada parcial de escalar",
     r"\partial_{\mu}{\partial_{\nu}{A}}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("352 — Segunda derivada covariante de escalar",
     r"\nabla_{\mu}{\nabla_{\nu}{A}}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("353 — Derivada parcial seguida de covariante",
     r"\partial_{\mu}{\nabla_{\nu}{A}}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("354 — Derivada covariante seguida de parcial",
     r"\nabla_{\mu}{\partial_{\nu}{A}}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("355 — Segunda derivada de vector contravariante",
     r"\nabla_{\mu}{\nabla_{\nu}{A^{\rho}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super')]),

    ("356 — Segunda derivada de vector covariante",
     r"\nabla_{\mu}{\nabla_{\nu}{A_{\rho}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("357 — Segunda derivada con contracción interna",
     r"\nabla_{\mu}{\nabla_{\nu}{A^{\nu}}}",
     [('μ', 'sub')]),

    ("358 — Segunda derivada con índice externo contraído",
     r"\nabla_{\mu}{\nabla_{\nu}{A^{\mu}}}",
     [('ν', 'sub')]),

    ("359 — Suma de dos derivadas parciales con mismo índice libre",
     r"\partial_{\mu}{A^{\nu}} + \partial_{\mu}{B^{\nu}}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("360 — Suma de dos derivadas covariantes con mismo índice libre",
     r"\nabla_{\mu}{A^{\nu}} + \nabla_{\mu}{B^{\nu}}",
     [('μ', 'sub'), ('ν', 'super')]),

    # =============================================================================
    # 361–380 — DERIVADAS ANIDADAS Y ESTRUCTURAS RECURSIVAS
    # =============================================================================

    ("361 — Tercera derivada covariante de escalar",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("362 — Tercera derivada parcial de escalar",
     r"\partial_{\mu}{\partial_{\nu}{\partial_{\rho}{A}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("363 — Mezcla de tres derivadas",
     r"\nabla_{\mu}{\partial_{\nu}{\nabla_{\rho}{A}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("364 — Otra mezcla de tres derivadas",
     r"\partial_{\mu}{\nabla_{\nu}{\partial_{\rho}{A}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("365 — Tercera derivada de vector contravariante",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A^{\sigma}}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'super')]),

    ("366 — Tercera derivada de vector covariante",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A_{\sigma}}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("367 — Tercera derivada con contracción interna",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A^{\rho}}}}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("368 — Tercera derivada con contracción con índice externo",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A^{\mu}}}}",
     [('ν', 'sub'), ('ρ', 'sub')]),

    ("369 — Tercera derivada con contracción con índice intermedio",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A^{\nu}}}}",
     [('μ', 'sub'), ('ρ', 'sub')]),

    ("370 — Cuarta derivada covariante de escalar",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{\nabla_{\sigma}{A}}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("371 — Cuarta derivada con una contracción",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{\nabla_{\sigma}{A^{\sigma}}}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("372 — Cuarta derivada con contracción externa",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{\nabla_{\sigma}{A^{\mu}}}}}",
     [('ν', 'sub'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("373 — Cuarta derivada con dos contracciones",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A^{\mu\nu}}}}",
     [('ρ', 'sub')]),

    ("374 — Cuarta estructura con dos índices libres",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A^{\rho\sigma}}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('σ', 'super')]),

    ("375 — Derivadas anidadas sobre tensor mixto",
     r"\nabla_{\mu}{\nabla_{\nu}{A^{\rho}_{\sigma}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('σ', 'sub')]),

    ("376 — Tres derivadas sobre tensor mixto",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A^{\sigma}_{\lambda}}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'super'), ('λ', 'sub')]),

    ("377 — Derivadas anidadas con producto interno",
     r"\nabla_{\mu}{\nabla_{\nu}{A^{\rho} B_{\rho}}}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("378 — Tres derivadas sobre producto contraído",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A^{\sigma} B_{\sigma}}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("379 — Derivadas anidadas sobre producto con índices libres",
     r"\nabla_{\mu}{\nabla_{\nu}{A^{\rho} B_{\sigma}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('σ', 'sub')]),

    ("380 — Derivadas anidadas profundas sobre producto mixto",
     r"\nabla_{\mu}{\nabla_{\nu}{\nabla_{\rho}{A^{\sigma}_{\lambda} B^{\lambda}}}}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'super')]),

    # =============================================================================
    # 381–400 — CONTRACCIONES ENTRE DIFERENTES NIVELES DE LA ESTRUCTURA
    # =============================================================================

    ("381 — Índice del operador externo contraído con tensor interno",
     r"\nabla_{\mu}{A^{\mu}}",
     []),

    ("382 — Índice del operador interno contraído con tensor",
     r"\nabla_{\mu}{\nabla_{\nu}{A^{\nu}}}",
     [('μ', 'sub')]),

    ("383 — Índice del operador externo contraído dentro del argumento",
     r"\nabla_{\mu}{A^{\mu} B_{\nu}}",
     [('ν', 'sub')]),

    ("384 — Índice del operador externo contraído con segundo tensor",
     r"\nabla_{\mu}{A^{\nu} B^{\mu}_{\rho}}",
     [('ν', 'super'), ('ρ', 'sub')]),

    ("385 — Índice del operador interno contraído con tensor externo al operador interno",
     r"\nabla_{\mu}{A^{\nu} \nabla_{\nu}{B^{\rho}}}",
     [('μ', 'sub'), ('ρ', 'super')]),

    ("386 — Índice del operador interno contraído con tensor covariante",
     r"\nabla_{\mu}{A^{\nu} \nabla_{\nu}{B_{\rho}}}",
     [('μ', 'sub'), ('ρ', 'sub')]),

    ("387 — Contracción entre operador externo y tensor dentro de producto",
     r"\nabla_{\mu}{A^{\nu} B_{\nu} C^{\mu}}",
     []),

    ("388 — Contracción externa más índice libre",
     r"\nabla_{\mu}{A^{\nu} B_{\nu} C^{\mu}_{\rho}}",
     [('ρ', 'sub')]),

    ("389 — Operador externo contraído con índice de tensor de rango 2",
     r"\nabla_{\mu}{A^{\mu\nu}_{\rho}}",
     [('ν', 'super'), ('ρ', 'sub')]),

    ("390 — Operador externo contraído con índice inferior de tensor",
     r"\nabla^{\mu}{A^{\nu}_{\mu\rho}}",
     [('ν', 'super'), ('ρ', 'sub')]),

    ("391 — Operador interno contraído con índice del tensor final",
     r"\nabla_{\mu}{\nabla_{\nu}{A^{\rho\nu}}}",
     [('μ', 'sub'), ('ρ', 'super')]),

    ("392 — Operador interno contraído con índice covariante",
     r"\nabla_{\mu}{\nabla_{\nu}{A_{\rho}^{\nu}}}",
     [('μ', 'sub'), ('ρ', 'sub')]),

    ("393 — Operador externo e interno contraídos independientemente",
     r"\nabla_{\mu}{\nabla_{\nu}{A^{\mu\nu}}}",
     []),

    ("394 — Contracción entre los dos operadores y tensores",
     r"\nabla_{\mu}{A^{\nu} \nabla_{\nu}{B^{\mu}}}",
     []),

    ("395 — Contracción entre derivada interna y tensor exterior",
     r"\nabla_{\mu}{A^{\nu} \nabla_{\rho}{B^{\rho}}}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("396 — Contracción entre derivada interna y tensor exterior de rango 2",
     r"\nabla_{\mu}{A^{\nu}_{\rho} \nabla_{\nu}{B^{\rho}}}",
     [('μ', 'sub')]),

    ("397 — Cadena de derivadas con contracción cruzada",
     r"\nabla_{\mu}{A^{\nu} \nabla_{\rho}{B^{\rho}_{\nu}}}",
     [('μ', 'sub')]),

    ("398 — Cadena de derivadas con dos contracciones",
     r"\nabla_{\mu}{A^{\nu} \nabla_{\rho}{B^{\rho}_{\nu}} C^{\mu}}",
     []),

    ("399 — Derivada externa con producto de derivada y tensor",
     r"\nabla_{\mu}{A^{\nu} \nabla_{\nu}{B_{\rho}} C^{\rho}}",
     [('μ', 'sub')]),

    ("400 — Estructura profundamente anidada con múltiples contracciones",
     r"\nabla_{\mu}{A^{\nu} \nabla_{\rho}{B^{\rho}_{\nu} \nabla_{\sigma}{C^{\sigma\mu}}}}",
     []),

    # =============================================================================
    # 401–420 — DERIVADAS ANIDADAS PROFUNDAS
    # =============================================================================

    ("401 — Derivada covariante de vector",
     r"\nabla_{\mu}(A^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("402 — Segunda derivada covariante",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super')]),

    ("403 — Tercera derivada covariante",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(A^{\sigma})))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'super')]),

    ("404 — Cuarta derivada covariante",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(\nabla_{\sigma}(A^{\lambda}))))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'sub'), ('λ', 'super')]),

    ("405 — Derivadas anidadas sobre tensor mixto",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho}_{\sigma}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('σ', 'sub')]),

    ("406 — Derivadas anidadas sobre tensor rango 2",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho\lambda}_{\sigma}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('λ', 'super'), ('σ', 'sub')]),

    ("407 — Derivada parcial dentro de covariante",
     r"\nabla_{\mu}(\partial_{\nu}(A^{\rho}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super')]),

    ("408 — Covariante dentro de parcial",
     r"\partial_{\mu}(\nabla_{\nu}(A^{\rho}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super')]),

    ("409 — Dos parciales anidadas",
     r"\partial_{\mu}(\partial_{\nu}(A^{\rho}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super')]),

    ("410 — Parcial y dos covariantes",
     r"\partial_{\mu}(\nabla_{\nu}(\nabla_{\rho}(A^{\sigma})))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'super')]),

    ("411 — Cuatro niveles mixtos",
     r"\nabla_{\mu}(\partial_{\nu}(\nabla_{\rho}(\partial_{\sigma}(A^{\lambda}))))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'sub'), ('λ', 'super')]),

    ("412 — Derivada de escalar",
     r"\nabla_{\mu}(A)",
     [('μ', 'sub')]),

    ("413 — Segunda derivada de escalar",
     r"\nabla_{\mu}(\nabla_{\nu}(A))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("414 — Tercera derivada de escalar",
     r"\partial_{\mu}(\nabla_{\nu}(\partial_{\rho}(A)))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("415 — Derivadas anidadas de producto",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho} B_{\sigma}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('σ', 'sub')]),

    ("416 — Derivadas profundas de producto",
     r"\nabla_{\mu}(\partial_{\nu}(\nabla_{\rho}(A^{\sigma} B_{\lambda})))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'super'), ('λ', 'sub')]),

    ("417 — Derivadas anidadas sobre tensor rango 3",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho\sigma}_{\lambda}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('σ', 'super'), ('λ', 'sub')]),

    ("418 — Cinco niveles de derivación",
     r"\nabla_{\mu}(\nabla_{\nu}(\partial_{\rho}(\nabla_{\sigma}(\partial_{\lambda}(A^{\tau})))))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'sub'), ('λ', 'sub'), ('τ', 'super')]),

    ("419 — Derivadas anidadas con contracción interna",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho}_{\rho}))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("420 — Derivadas profundas con contracción externa",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho} B_{\rho}))",
     [('μ', 'sub'), ('ν', 'sub')]),

    # =============================================================================
    # 421–440 — CONTRACCIONES ENTRE NIVELES
    # =============================================================================

    ("421 — Contracción entre derivada y tensor",
     r"\nabla_{\mu}(A^{\mu})",
     []),

    ("422 — Contracción de dos niveles",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\nu}))",
     [('μ', 'sub')]),

    ("423 — Contracción con derivada exterior",
     r"\nabla^{\mu}(\nabla_{\mu}(A^{\nu}))",
     [('ν', 'super')]),

    ("424 — Contracción cruzada entre niveles",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\mu\nu}))",
     []),

    ("425 — Contracción cruzada inversa",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\nu\mu}))",
     []),

    ("426 — Derivada de producto contraído",
     r"\nabla_{\mu}(A^{\nu} B_{\nu})",
     [('μ', 'sub')]),

    ("427 — Contracción entre dos tensores dentro de derivada",
     r"\nabla_{\mu}(A^{\mu\nu} B_{\nu})",
     []),

    ("428 — Un libre después de contracción interna",
     r"\nabla_{\mu}(A^{\mu\nu} B_{\rho})",
     [('ν', 'super'), ('ρ', 'sub')]),

    ("429 — Contracción interna y derivada libre",
     r"\nabla_{\mu}(A^{\rho}_{\rho} B^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("430 — Dos contracciones dentro de derivada",
     r"\nabla_{\mu}(A^{\rho\sigma}_{\rho\sigma})",
     [('μ', 'sub')]),

    ("431 — Derivada exterior contraída con tensor interno",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\mu} B^{\nu}))",
     []),

    ("432 — Una contracción entre niveles y un libre",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\mu} B^{\rho}))",
     [('ν', 'sub'), ('ρ', 'super')]),

    ("433 — Contracción de índice de derivada con tensor profundo",
     r"\nabla_{\mu}(\partial_{\nu}(A^{\mu\nu}))",
     []),

    ("434 — Contracción parcial entre niveles",
     r"\nabla_{\mu}(\partial_{\nu}(A^{\mu\rho} B_{\rho}))",
     [('ν', 'sub')]),

    ("435 — Cadena derivativa cerrada",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(A^{\mu\nu\rho})))",
     []),

    ("436 — Cadena derivativa con un índice libre",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(A^{\mu\nu\sigma})))",
     [('ρ', 'sub'), ('σ', 'super')]),

    ("437 — Producto dentro de derivada con dos contracciones",
     r"\nabla_{\mu}(A^{\mu\nu}_{\rho} B^{\rho}_{\nu})",
     []),

    ("438 — Producto dentro de derivada con libre",
     r"\nabla_{\mu}(A^{\mu\nu}_{\rho} B^{\rho}_{\sigma})",
     [('ν', 'super'), ('σ', 'sub')]),

    ("439 — Derivadas mixtas con contracciones profundas",
     r"\nabla_{\mu}(\partial_{\nu}(A^{\mu\rho}_{\sigma} B^{\sigma}_{\rho}))",
     [('ν', 'sub')]),

    ("440 — Estructura profunda completamente contraída",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\mu\rho}_{\sigma} B^{\sigma}_{\rho} C^{\nu}))",
     []),

    # =============================================================================
    # 441–460 — OPERADORES + PRODUCTOS + CONTRACCIONES
    # =============================================================================

    ("441 — Producto de dos derivadas",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\rho}(B^{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'super')]),

    ("442 — Producto de derivada covariante y parcial",
     r"\nabla_{\mu}(A^{\nu}) \partial_{\rho}(B^{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'super')]),

    ("443 — Producto de parcial y covariante",
     r"\partial_{\mu}(A^{\nu}) \nabla_{\rho}(B^{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'super')]),

    ("444 — Producto de dos parciales",
     r"\partial_{\mu}(A^{\nu}) \partial_{\rho}(B^{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'super')]),

    ("445 — Producto con índice compartido contraído",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\nu}(B^{\rho})",
     [('μ', 'sub'), ('ρ', 'super')]),

    ("446 — Producto con índice del primer operador contraído",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\rho}(B^{\mu})",
     [('ν', 'super'), ('ρ', 'sub')]),

    ("447 — Producto con índice del segundo operador contraído",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\nu}(B)",
     [('μ', 'sub')]),

    ("448 — Producto completamente contraído",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\nu}(B^{\mu})",
     []),

    ("449 — Producto de operador con contracción interna",
     r"\nabla_{\mu}(A^{\nu} B_{\nu}) \partial_{\rho}(C^{\sigma})",
     [('μ', 'sub'), ('ρ', 'sub'), ('σ', 'super')]),

    ("450 — Producto con derivadas de escalares",
     r"\nabla_{\mu}(A) \nabla_{\nu}(B)",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("451 — Producto de operadores anidados",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho})) \nabla_{\sigma}(B^{\lambda})",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('σ', 'sub'), ('λ', 'super')]),

    ("452 — Producto de operadores profundamente anidados",
     r"\nabla_{\mu}(\partial_{\nu}(A^{\rho})) \nabla_{\sigma}(\partial_{\lambda}(B^{\tau}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super'), ('σ', 'sub'), ('λ', 'sub'), ('τ', 'super')]),

    ("453 — Producto con contracción entre subárboles",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\nu}(B_{\rho})",
     [('μ', 'sub'), ('ρ', 'sub')]),

    ("454 — Producto con dos contracciones entre operadores",
     r"\nabla_{\mu}(A^{\nu\rho}) \nabla_{\nu}(B_{\rho})",
     [('μ', 'sub')]),

    ("455 — Producto de operadores con tensor mixto",
     r"\nabla_{\mu}(A^{\nu}_{\rho}) \partial_{\sigma}(B^{\rho}_{\lambda})",
     [('μ', 'sub'), ('ν', 'super'), ('σ', 'sub'), ('λ', 'sub')]),

    ("456 — Producto con contracción cruzada",
     r"\nabla_{\mu}(A^{\nu}_{\rho}) \partial_{\nu}(B^{\rho}_{\sigma})",
     [('μ', 'sub'), ('σ', 'sub')]),

    ("457 — Tres operadores independientes",
     r"\nabla_{\mu}(A^{\nu}) \partial_{\rho}(B^{\sigma}) \nabla_{\lambda}(C^{\kappa})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'super'), ('λ', 'sub'), ('κ', 'super')]),

    ("458 — Tres operadores con cadena de contracciones",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\nu}(B^{\rho}) \nabla_{\rho}(C^{\sigma})",
     [('μ', 'sub'), ('σ', 'super')]),

    ("459 — Cadena de cuatro operadores",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\nu}(B^{\rho}) \partial_{\rho}(C^{\sigma}) \nabla_{\sigma}(D^{\lambda})",
     [('μ', 'sub'), ('λ', 'super')]),

    ("460 — Producto complejo de operadores",
     r"\nabla_{\mu}(\partial_{\nu}(A^{\rho})) \nabla_{\rho}(\partial_{\sigma}(B^{\mu}))",
     [('ν', 'sub'), ('σ', 'sub')]),

    # =============================================================================
    # 461–480 — SUMAS DENTRO/FUERA DE DERIVADAS
    # =============================================================================

    ("461 — Derivada de suma de escalares",
     r"\nabla_{\mu}{(A + B)}",
     [('μ', 'sub')]),

    ("462 — Derivada parcial de suma de escalares",
     r"\partial_{\mu}{(A + B)}",
     [('μ', 'sub')]),

    ("463 — Suma de derivadas",
     r"\nabla_{\mu}{A} + \nabla_{\mu}{B}",
     [('μ', 'sub')]),

    ("464 — Suma de derivadas parciales",
     r"\partial_{\mu}{A} + \partial_{\mu}{B}",
     [('μ', 'sub')]),

    ("465 — Derivada de suma de vectores contravariantes",
     r"\nabla_{\mu}{(A^{\nu} + B^{\nu})}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("466 — Derivada de suma de vectores covariantes",
     r"\nabla_{\mu}{(A_{\nu} + B_{\nu})}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("467 — Suma de derivadas de vectores",
     r"\nabla_{\mu}{A^{\nu}} + \nabla_{\mu}{B^{\nu}}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("468 — Suma de derivadas de covectores",
     r"\nabla_{\mu}{A_{\nu}} + \nabla_{\mu}{B_{\nu}}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("469 — Derivada de suma con contracción interna",
     r"\nabla_{\mu}{(A^{\nu} B_{\nu} + C^{\rho} D_{\rho})}",
     [('μ', 'sub')]),

    ("470 — Suma de productos contraídos dentro de derivada",
     r"\nabla_{\mu}{(A^{\nu} B_{\nu})} + \nabla_{\mu}{(C^{\rho} D_{\rho})}",
     [('μ', 'sub')]),

    ("471 — Derivada de suma de tensores mixtos",
     r"\nabla_{\mu}{(A^{\nu}_{\rho} + B^{\nu}_{\rho})}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("472 — Suma de derivadas de tensores mixtos",
     r"\nabla_{\mu}{A^{\nu}_{\rho}} + \nabla_{\mu}{B^{\nu}_{\rho}}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("473 — Derivada de suma con dos índices libres",
     r"\nabla_{\mu}{(A^{\nu\rho} + B^{\nu\rho})}",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'super')]),

    ("474 — Derivada de suma covariante con dos índices libres",
     r"\nabla_{\mu}{(A_{\nu\rho} + B_{\nu\rho})}",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("475 — Suma de tres términos dentro de derivada",
     r"\nabla_{\mu}{(A^{\nu} + B^{\nu} + C^{\nu})}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("476 — Tres derivadas sumadas",
     r"\nabla_{\mu}{A^{\nu}} + \nabla_{\mu}{B^{\nu}} + \nabla_{\mu}{C^{\nu}}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("477 — Derivada externa de suma de productos",
     r"\nabla_{\mu}{(A^{\nu}_{\rho} B^{\rho} + C^{\nu}_{\sigma} D^{\sigma})}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("478 — Suma externa de productos derivados",
     r"\nabla_{\mu}{(A^{\nu}_{\rho} B^{\rho})} + \nabla_{\mu}{(C^{\nu}_{\sigma} D^{\sigma})}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("479 — Derivada de suma con cadenas contraídas",
     r"\nabla_{\mu}{(A^{\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma} + D^{\nu}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa})}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("480 — Estructura completa: suma de productos contraídos derivada",
     r"\nabla_{\mu}{(A^{\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma} + D^{\nu}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa})} + \nabla_{\mu}{G^{\nu}}",
     [('μ', 'sub'), ('ν', 'super')]),

    # =============================================================================
    # 481–500 — PRODUCTOS DE OPERADORES
    # =============================================================================

    ("481 — Producto de dos derivadas parciales",
     r"\partial_{\mu}(A) \partial_{\nu}(B)",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("482 — Producto de dos derivadas covariantes",
     r"\nabla_{\mu}(A) \nabla_{\nu}(B)",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("483 — Producto de derivada y tensor",
     r"\nabla_{\mu}(A) B^{\nu}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("484 — Producto de tensor y derivada",
     r"A^{\nu} \nabla_{\mu}(B)",
     [('ν', 'super'), ('μ', 'sub')]),

    ("485 — Producto de derivadas con contracción",
     r"\nabla_{\mu}(A^{\mu}) \nabla_{\nu}(B)",
     [('ν', 'sub')]),

    ("486 — Producto de derivadas con índice compartido",
     r"\nabla_{\mu}(A) \nabla^{\mu}(B)",
     []),

    ("487 — Producto de derivadas parciales con contracción",
     r"\partial_{\mu}(A^{\mu}) \partial_{\nu}(B^{\nu})",
     []),

    ("488 — Producto de derivadas actuando sobre vectores",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\nu}(B^{\mu})",
     []),

    ("489 — Producto de derivadas actuando sobre tensores",
     r"\nabla_{\mu}(A^{\nu}_{\rho}) \nabla_{\nu}(B^{\rho\mu})",
     []),

    ("490 — Producto de operador y expresión compuesta",
     r"\nabla_{\mu}(A^{\nu} B_{\rho}) C^{\mu\rho}",
     [('ν', 'super')]),

    ("491 — Expresión compuesta multiplicando derivada",
     r"A^{\mu}_{\nu} \nabla_{\mu}(B^{\nu})",
     []),

    ("492 — Dos operadores con dos contracciones",
     r"\nabla_{\mu}(A^{\nu}_{\rho}) \nabla_{\nu}(B^{\rho\mu})",
     []),

    ("493 — Producto de derivadas sobre escalares con tensor externo",
     r"C^{\mu\nu} \nabla_{\mu}(A) \nabla_{\nu}(B)",
     []),

    ("494 — Producto de operadores y vectores abiertos",
     r"\nabla_{\mu}(A^{\nu}) B_{\nu} C^{\mu}",
     []),

    ("495 — Dos derivadas y un índice libre",
     r"\nabla_{\mu}(A^{\nu}) B_{\nu} C^{\rho}",
     [('μ', 'sub'), ('ρ', 'super')]),

    ("496 — Producto de operadores con cadena de contracciones",
     r"\nabla_{\mu}(A^{\nu}) B_{\rho} C^{\rho}_{\nu} D^{\mu}",
     []),

    ("497 — Producto de dos operadores actuando sobre productos",
     r"\nabla_{\mu}(A^{\nu} B_{\rho}) \nabla_{\nu}(C^{\rho} D^{\mu})",
     []),

    ("498 — Producto de operadores con tensor de rango alto",
     r"\nabla_{\mu}(A^{\nu\rho}_{\sigma}) B^{\mu\sigma} \nabla_{\nu}(C_{\rho})",
     []),

    ("499 — Producto triple de operadores",
     r"\nabla_{\mu}(A) \nabla_{\nu}(B) \nabla_{\rho}(C)",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("500 — Producto complejo de operadores y tensores",
     r"\nabla_{\mu}(A^{\nu}_{\rho}) B^{\rho}_{\sigma} \nabla_{\nu}(C^{\sigma}_{\lambda}) D^{\lambda\mu}",
     []),

    # =============================================================================
    # 501–520 — CASOS INVÁLIDOS / MANEJO DE ERRORES
    # =============================================================================

    ("501 — Índice repetido en la misma posición",
     r"A_{\mu} B_{\mu}",
     "INVALID"),

    ("502 — Índice contravariante repetido",
     r"A^{\mu} B^{\mu}",
     "INVALID"),

    ("503 — Tres apariciones del mismo índice",
     r"A^{\mu} B_{\mu} C_{\mu}",
     "INVALID"),

    ("504 — Tres apariciones con posiciones mixtas",
     r"A^{\mu} B_{\mu} C^{\mu}",
     "INVALID"),

    ("505 — Cuatro apariciones del mismo índice",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\mu}",
     "INVALID"),

    ("506 — Contracción interna inválida",
     r"A^{\mu}_{\mu} B_{\nu}",
     [('ν', 'sub')]),

    ("507 — Traza interna repetida en posición inferior",
     r"A_{\mu\mu}",
     "INVALID"),

    ("508 — Traza interna repetida en posición superior",
     r"A^{\mu\mu}",
     "INVALID"),

    ("509 — Índice repetido dentro de producto",
     r"A^{\mu}_{\nu} B^{\nu}_{\nu}",
     "INVALID"),

    ("510 — Índices repetidos en posiciones incompatibles",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\mu}_{\rho}",
     "INVALID"),

    ("511 — Suma con índices libres incompatibles",
     r"A^{\mu} + B_{\mu}",
     "INVALID"),

    ("512 — Suma de escalar y vector",
     r"A^{\mu}_{\mu} + B^{\nu}",
     "INVALID"),

    ("513 — Suma con diferentes índices libres",
     r"A^{\mu} + B^{\nu}",
     "INVALID"),

    ("514 — Suma con diferente estructura de índices",
     r"A^{\mu}_{\nu} + B^{\mu\nu}",
     "INVALID"),

    ("515 — Suma con diferente número de índices libres",
     r"A^{\mu}_{\nu} + B^{\mu}",
     "INVALID"),

    ("516 — Derivadas con suma tensorial incompatible",
     r"\nabla_{\mu}(A^{\nu}) + \nabla_{\rho}(B_{\rho})",
     "INVALID"),

    ("517 — Derivadas con índices libres incompatibles",
     r"\nabla_{\mu}(A^{\nu}) + \nabla_{\rho}(B^{\nu})",
     "INVALID"),

    ("518 — Contracción inválida dentro de operador",
     r"\nabla_{\mu}(A^{\mu}_{\mu})",
     "INVALID"),

    ("519 — Producto con índice repetido inválidamente dentro de subárbol",
     r"\nabla_{\mu}(A^{\nu}_{\nu}) B^{\nu}",
     "INVALID"),

    ("520 — Estructura compleja inválida",
     r"\nabla_{\mu}(A^{\nu}_{\rho} B^{\rho}_{\nu}) + C^{\mu}_{\mu}",
     "INVALID"),

    # =============================================================================
    # 521–540 — EXPRESIONES DE GEOMETRÍA DIFERENCIAL
    # =============================================================================

    ("521 — Derivada covariante de un escalar",
     r"\nabla_{\mu}(A)",
     [('μ', 'sub')]),

    ("522 — Derivada covariante de un vector contravariante",
     r"\nabla_{\mu}(A^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("523 — Derivada covariante de un vector covariante",
     r"\nabla_{\mu}(A_{\nu})",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("524 — Derivada covariante de tensor mixto",
     r"\nabla_{\mu}(A^{\nu}_{\rho})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("525 — Segunda derivada covariante de un escalar",
     r"\nabla_{\mu}(\nabla_{\nu}(A))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("526 — Segunda derivada covariante de un vector",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super')]),

    ("527 — Derivada parcial de un campo vectorial",
     r"\partial_{\mu}(A^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("528 — Derivada parcial de un tensor covariante",
     r"\partial_{\mu}(A_{\nu\rho})",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("529 — Símbolo de Christoffel",
     r"\Gamma^{\mu}_{\nu\rho}",
     [('μ', 'super'), ('ν', 'sub'), ('ρ', 'sub')]),

    ("530 — Christoffel contraído con un vector",
     r"\Gamma^{\mu}_{\nu\rho} A^{\nu}",
     [('μ', 'super'), ('ρ', 'sub')]),

    ("531 — Christoffel contraído con dos vectores",
     r"\Gamma^{\mu}_{\nu\rho} A^{\nu} B^{\rho}",
     [('μ', 'super')]),

    ("532 — Christoffel multiplicando tensor covariante",
     r"\Gamma^{\rho}_{\mu\nu} A_{\rho}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("533 — Derivada covariante y Christoffel",
     r"\nabla_{\mu}(A^{\nu}) + \Gamma^{\nu}_{\mu\rho} A^{\rho}",
     [('μ', 'sub'), ('ν', 'super')]),

    ("534 — Derivada covariante de tensor de rango 2",
     r"\nabla_{\mu}(A^{\nu\rho}_{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'super'), ('σ', 'sub')]),

    ("535 — Tensor métrico y su inversa",
     r"g_{\mu\nu} g^{\nu\rho}",
     [('μ', 'sub'), ('ρ', 'super')]),

    ("536 — Métrica con derivada covariante",
     r"\nabla_{\rho}(g_{\mu\nu})",
     [('ρ', 'sub'), ('μ', 'sub'), ('ν', 'sub')]),

    ("537 — Tensor de Riemann",
     r"R^{\rho}_{\sigma\mu\nu}",
     [('ρ', 'super'), ('σ', 'sub'), ('μ', 'sub'), ('ν', 'sub')]),

    ("538 — Riemann contraído con un vector",
     r"R^{\rho}_{\sigma\mu\nu} A^{\sigma}",
     [('ρ', 'super'), ('μ', 'sub'), ('ν', 'sub')]),

    ("539 — Tensor de Ricci mediante contracción",
     r"R^{\rho}_{\mu\rho\nu}",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("540 — Expresión geométrica compuesta",
     r"\nabla_{\mu}(R^{\mu}_{\nu\rho\sigma} A^{\nu})",
     [('ρ', 'sub'), ('σ', 'sub')]),

    # =============================================================================
    # 541–560 — STRESS TESTS
    # =============================================================================

    ("541 — Cadena profunda de derivadas sobre vector",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(A^{\sigma})))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'super')]),

    ("542 — Cadena profunda sobre tensor mixto",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(A^{\sigma}_{\lambda})))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'super'), ('λ', 'sub')]),

    ("543 — Derivadas anidadas con contracción externa",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\mu} B^{\nu}))",
     []),

    ("544 — Derivadas anidadas completamente contraídas",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\mu} B^{\nu})) C^{\rho}_{\rho}",
     []),

    ("545 — Producto de derivadas anidadas",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho})) \nabla_{\rho}(\nabla_{\sigma}(B^{\mu}))",
     [('ν', 'sub'), ('σ', 'sub')]),

    ("546 — Tres bloques derivados con contracciones cruzadas",
     r"\nabla_{\mu}(A^{\nu}) \nabla_{\nu}(B^{\rho}) \nabla_{\rho}(C^{\mu})",
     []),

    ("547 — Producto profundo con tensor de rango 2",
     r"\nabla_{\mu}(A^{\nu\rho}) B_{\nu} C_{\rho} \nabla_{\sigma}(D^{\sigma})",
     [('μ', 'sub')]),

    ("548 — Métrica y derivadas anidadas",
     r"g_{\mu\nu} \nabla_{\rho}(\nabla_{\sigma}(A^{\nu}))",
     [('μ', 'sub'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("549 — Riemann con derivada y contracción",
     r"\nabla_{\mu}(R^{\mu}_{\nu\rho\sigma} A^{\nu})",
     [('ρ', 'sub'), ('σ', 'sub')]),

    ("550 — Riemann multiplicado por dos vectores",
     r"R^{\mu}_{\nu\rho\sigma} A^{\nu} B^{\rho} C^{\sigma}",
     [('μ', 'super')]),

    ("551 — Riemann con tensor externo",
     r"R^{\mu}_{\nu\rho\sigma} A^{\nu\lambda} B_{\lambda} C^{\rho} D^{\sigma}",
     [('μ', 'super')]),

    ("552 — Christoffel dentro de derivada covariante",
     r"\nabla_{\mu}(\Gamma^{\nu}_{\rho\sigma} A^{\rho} B^{\sigma})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("553 — Derivada parcial de producto geométrico",
     r"\partial_{\mu}(g_{\nu\rho} A^{\nu} B^{\rho})",
     [('μ', 'sub')]),

    ("554 — Suma de estructuras derivadas",
     r"\nabla_{\mu}(A^{\nu}) + \nabla_{\mu}(B^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("555 — Suma de productos derivados",
     r"\nabla_{\mu}(A^{\rho}) B_{\rho} + C^{\rho} \nabla_{\mu}(D_{\rho})",
     [('μ', 'sub')]),

    ("556 — Suma de términos con dos niveles de derivación",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho})) B_{\rho} + C^{\rho} \nabla_{\mu}(\nabla_{\nu}(D_{\rho}))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("557 — Expresión grande con métrica y Riemann",
     r"g_{\mu\lambda} R^{\lambda}_{\nu\rho\sigma} A^{\nu} B^{\rho} C^{\sigma}",
     [('μ', 'sub')]),

    ("558 — Riemann derivado y contracciones",
     r"\nabla_{\lambda}(R^{\lambda}_{\mu\nu\rho} A^{\mu} B^{\nu} C^{\rho})",
     []),

    ("559 — Stress test con múltiples subárboles",
     r"\nabla_{\mu}(A^{\nu}_{\rho} B^{\rho}) C_{\nu} + D^{\nu} \nabla_{\mu}(E_{\nu}^{\rho} F_{\rho})",
     [('μ', 'sub')]),

    ("560 — Stress test máximo del bloque",
     r"\nabla_{\mu}(\nabla_{\nu}(R^{\nu}_{\rho\sigma\lambda} A^{\rho} B^{\sigma} C^{\lambda})) D^{\mu}_{\kappa} E^{\kappa} + g_{\alpha\beta} \nabla_{\rho}(F^{\alpha}) \nabla^{\beta}(G^{\rho})",
     []),

    # =============================================================================
    # 561–580 — INDEPENDENCIA DEL ORDEN DE LOS FACTORES
    # =============================================================================

    ("561 — Contracción simple con factores invertidos",
     r"A^{\mu} B_{\mu} C^{\nu}",
     [('ν', 'super')]),

    ("562 — Contracción simple orden alternativo",
     r"C^{\nu} A^{\mu} B_{\mu}",
     [('ν', 'super')]),

    ("563 — Contracción simple con índice libre al inicio",
     r"C^{\nu} A^{\mu} B_{\mu}",
     [('ν', 'super')]),

    ("564 — Contracción simple con índice libre al final",
     r"A^{\mu} B_{\mu} C^{\nu}",
     [('ν', 'super')]),

    ("565 — Dos contracciones independientes",
     r"A^{\mu} B_{\mu} C^{\nu} D_{\nu} E^{\rho}",
     [('ρ', 'super')]),

    ("566 — Dos contracciones independientes reordenadas",
     r"E^{\rho} C^{\nu} D_{\nu} A^{\mu} B_{\mu}",
     [('ρ', 'super')]),

    ("567 — Dos índices libres y una contracción",
     r"A^{\mu} B_{\nu} C^{\nu} D^{\rho}",
     [('μ', 'super'), ('ρ', 'super')]),

    ("568 — Dos índices libres y una contracción reordenada",
     r"D^{\rho} C^{\nu} A^{\mu} B_{\nu}",
     [('μ', 'super'), ('ρ', 'super')]),

    ("569 — Cadena de tres tensores",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}",
     [('μ', 'super')]),

    ("570 — Cadena de tres tensores reordenada",
     r"C^{\rho} A^{\mu}_{\nu} B^{\nu}_{\rho}",
     [('μ', 'super')]),

    ("571 — Cadena cerrada",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu}",
     []),

    ("572 — Cadena cerrada reordenada",
     r"C^{\rho}_{\mu} A^{\mu}_{\nu} B^{\nu}_{\rho}",
     []),

    ("573 — Dos cadenas independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}",
     [('ρ', 'super')]),

    ("574 — Dos cadenas independientes reordenadas",
     r"D^{\sigma} C^{\rho}_{\sigma} A^{\mu}_{\nu} B^{\nu}_{\mu}",
     [('ρ', 'super')]),

    ("575 — Tensor de rango 2 con contracción externa",
     r"A^{\mu\nu}_{\rho} B^{\rho} C_{\nu}",
     [('μ', 'super')]),

    ("576 — Tensor de rango 2 reordenado",
     r"C_{\nu} B^{\rho} A^{\mu\nu}_{\rho}",
     [('μ', 'super')]),

    ("577 — Producto con dos cadenas y un libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}",
     [('μ', 'super')]),

    ("578 — Producto con dos cadenas reordenado",
     r"D^{\sigma} C^{\rho}_{\sigma} A^{\mu}_{\nu} B^{\nu}_{\rho}",
     [('μ', 'super')]),

    ("579 — Contracciones múltiples con tres índices libres",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma} D^{\lambda}",
     [('μ', 'super'), ('ν', 'super'), ('lambda', 'super')]),

    ("580 — Contracciones múltiples reordenadas",
     r"D^{\lambda} C^{\sigma} B^{\rho}_{\sigma} A^{\mu\nu}_{\rho}",
     [('μ', 'super'), ('ν', 'super'), ('lambda', 'super')]),

    # =============================================================================
    # 581–600 — CADENAS, CICLOS Y ESTRUCTURAS DE CONTRACCIÓN
    # =============================================================================

    ("581 — Cadena lineal de cuatro tensores",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda}",
     [('μ', 'super'), ('λ', 'sub')]),

    ("582 — Cadena lineal completamente cerrada",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\mu}",
     []),

    ("583 — Cadena lineal de cinco tensores",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa}",
     [('μ', 'super'), ('κ', 'sub')]),

    ("584 — Cadena de cinco tensores cerrada",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\mu}",
     []),

    ("585 — Cadena con tensor de rango 2 intermedio",
     r"A^{\mu}_{\nu} B^{\nu\rho}_{\sigma} C^{\sigma}_{\rho} D^{\lambda}_{\mu}",
     [('λ', 'super')]),

    ("586 — Cadena con dos índices libres internos",
     r"A^{\mu}_{\nu} B^{\nu\rho}_{\sigma} C^{\sigma}_{\lambda} D^{\lambda}_{\rho}",
     [('μ', 'super')]),

    ("587 — Ciclo triangular",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu}",
     []),

    ("588 — Ciclo triangular con índice libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\mu} E^{\lambda}_{\kappa}",
     [('λ', 'super'), ('κ', 'sub')]),

    ("589 — Dos ciclos independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\sigma}",
     []),

    ("590 — Ciclo y cadena abierta",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa}",
     [('σ', 'super'), ('κ', 'sub')]),

    ("591 — Cadena con producto tensorial adicional",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\lambda} D^{\sigma}_{\kappa} E^{\kappa}_{\tau}",
     [('μ', 'super'), ('λ', 'sub'), ('σ', 'super'), ('τ', 'sub')]),

    ("592 — Cadena conectada por dos índices",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\sigma}_{\lambda\kappa} C^{\lambda\kappa}_{\mu\alpha}",
     [('ν', 'super'), ('α', 'sub')]),

    ("593 — Ciclo de tensores de rango 2",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\sigma}_{\lambda\kappa} C^{\lambda\kappa}_{\mu\nu}",
     []),

    ("594 — Cadena profunda con dos libres",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\tau}",
     [('μ', 'super'), ('τ', 'sub')]),

    ("595 — Ciclo profundo de seis tensores",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\mu}",
     []),

    ("596 — Ciclo profundo con rama abierta",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\mu} E^{\lambda}_{\kappa} F^{\kappa}_{\tau}",
     [('λ', 'super'), ('τ', 'sub')]),

    ("597 — Dos cadenas que se conectan",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\lambda} D^{\lambda}_{\sigma} E^{\sigma}_{\mu}",
     []),

    ("598 — Ciclo con tensor externo de dos índices",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma\lambda}_{\kappa\tau}",
     [('σ', 'super'), ('λ', 'super'), ('κ', 'sub'), ('τ', 'sub')]),

    ("599 — Cadena de alto rango con cierre parcial",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\sigma}_{\kappa} E^{\kappa}_{\alpha}",
     [('ν', 'super'), ('α', 'sub')]),

    ("600 — Estructura mixta de ciclo y cadenas",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\tau} G^{\tau}_{\sigma}",
     []),

    # =============================================================================
    # 601–620 — RAMIFICACIONES, CICLOS PARCIALES Y ESTRUCTURAS MIXTAS
    # =============================================================================

    ("601 — Cadena con dos ramas independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\alpha}_{\beta} F^{\beta}_{\gamma}",
     [('μ', 'super'), ('λ', 'sub'), ('α', 'super'), ('γ', 'sub')]),

    ("602 — Dos cadenas cerradas independientes",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\sigma}",
     []),

    ("603 — Cadena abierta conectada a ciclo",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\kappa} F^{\kappa}_{\tau}",
     [('μ', 'super'), ('τ', 'sub')]),

    ("604 — Ciclo interno con cadena externa",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\sigma}_{\lambda} E^{\lambda}_{\tau}",
     [('σ', 'super'), ('τ', 'sub')]),

    ("605 — Tensor de rango 3 conectado a cadena",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma\kappa}_{\lambda} D^{\lambda}_{\alpha} E^{\alpha}_{\beta} F^{\beta}_{\kappa}",
     [('μ', 'super'), ('ν', 'super')]),

    ("606 — Dos conexiones entre bloques",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho\sigma}_{\lambda\kappa} C^{\lambda}_{\alpha} D^{\alpha}_{\mu} E^{\kappa}_{\beta} F^{\beta}_{\nu}",
     []),

    ("607 — Dos ramas que convergen",
     r"A^{\mu}_{\rho} B^{\rho}_{\nu} C^{\nu}_{\lambda} + D^{\mu}_{\sigma} E^{\sigma}_{\lambda}",
     [('μ', 'super'), ('λ', 'sub')]),

    ("608 — Ramas convergentes con dos índices compartidos",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\lambda} C^{\lambda}_{\sigma} D^{\sigma}_{\mu\nu}",
     []),

    ("609 — Ciclo de rango mixto",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma}_{\lambda} D^{\lambda}_{\mu\nu}",
     []),

    ("610 — Ciclo con rama libre",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\lambda}_{\kappa} E^{\kappa}_{\tau}",
     [('λ', 'super'), ('τ', 'sub')]),

    ("611 — Cadena con contracción transversal",
     r"A^{\mu\nu}_{\rho} B^{\rho}_{\sigma} C^{\sigma}_{\mu} D^{\lambda}_{\nu} E^{\alpha}_{\lambda}",
     [('α', 'super')]),

    ("612 — Dos ciclos unidos por un índice",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\lambda} D^{\lambda}_{\mu} E^{\sigma}_{\kappa} F^{\kappa}_{\tau} G^{\tau}_{\alpha} H^{\alpha}_{\sigma}",
     []),

    ("613 — Producto de tres estructuras cerradas",
     r"A^{\mu}_{\nu} B^{\nu}_{\mu} C^{\rho}_{\sigma} D^{\sigma}_{\rho} E^{\lambda}_{\kappa} F^{\kappa}_{\lambda}",
     []),

    ("614 — Producto de tres cadenas abiertas",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\alpha}_{\beta} E^{\beta}_{\gamma} F^{\gamma}_{\delta} G^{\lambda}_{\kappa} H^{\kappa}_{\tau}",
     [('μ', 'super'), ('σ', 'sub'), ('α', 'super'), ('δ', 'sub'), ('λ', 'super'), ('τ', 'sub')]),

    ("615 — Rango 3 con ciclo interno",
     r"A^{\mu\nu\rho}_{\sigma} B^{\sigma}_{\lambda} C^{\lambda}_{\mu} D^{\alpha}_{\nu} E^{\beta}_{\rho}",
     [('α', 'super'), ('β', 'super')]),

    ("616 — Rango 3 completamente conectado",
     r"A^{\mu\nu\rho}_{\sigma\lambda} B^{\sigma}_{\alpha} C^{\alpha}_{\mu} D^{\lambda}_{\beta} E^{\beta}_{\nu\rho}",
     []),

    ("617 — Dos niveles de ramificación",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\sigma} D^{\sigma}_{\lambda} E^{\lambda}_{\mu} F^{\alpha}_{\beta} G^{\beta}_{\gamma}",
     [('α', 'super'), ('γ', 'sub')]),

    ("618 — Ciclo central con dos cadenas externas",
     r"A^{\mu}_{\nu} B^{\nu}_{\rho} C^{\rho}_{\mu} D^{\alpha}_{\beta} E^{\beta}_{\gamma} F^{\lambda}_{\kappa} G^{\kappa}_{\tau}",
     [('α', 'super'), ('γ', 'sub'), ('λ', 'super'), ('τ', 'sub')]),

    ("619 — Estructura altamente conectada",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\mu} D^{\sigma}_{\kappa} E^{\kappa}_{\nu} F^{\alpha}_{\beta}",
     [('α', 'super'), ('β', 'sub')]),

    ("620 — Red de contracciones cerrada",
     r"A^{\mu\nu}_{\rho\sigma} B^{\rho}_{\lambda} C^{\lambda}_{\alpha} D^{\alpha}_{\mu} E^{\sigma}_{\kappa} F^{\kappa}_{\beta} G^{\beta}_{\nu}",
     []),

    # =============================================================================
    # 621–640 — OPERADORES, ALCANCE DE ÍNDICES Y CONTRACCIONES ENTRE NIVELES
    # =============================================================================

    ("621 — Operador sobre vector contravariante",
     r"\nabla_{\mu}(A^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("622 — Operador sobre vector covariante",
     r"\nabla_{\mu}(A_{\nu})",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("623 — Derivada parcial sobre tensor mixto",
     r"\partial_{\mu}(A^{\nu}_{\rho})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("624 — Operador contraído con argumento",
     r"\nabla_{\mu}(A^{\mu})",
     []),

    ("625 — Operador contraído dentro de producto",
     r"\nabla_{\mu}(A^{\nu} B^{\mu})",
     [('ν', 'super')]),

    ("626 — Índice del operador libre y contracción interna",
     r"\nabla_{\mu}(A^{\nu} B_{\nu})",
     [('μ', 'sub')]),

    ("627 — Contracción entre operador y tensor externo",
     r"\nabla_{\mu}(A_{\nu}) B^{\mu}",
     [('ν', 'sub')]),

    ("628 — Tensor externo conectado al argumento",
     r"A^{\mu}\nabla_{\mu}(B_{\nu})",
     [('ν', 'sub')]),

    ("629 — Dos operadores independientes",
     r"\nabla_{\mu}(A^{\nu}) \partial_{\rho}(B_{\sigma})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub'), ('σ', 'sub')]),

    ("630 — Dos operadores conectados por contracción",
     r"\nabla_{\mu}(A^{\nu}) \partial_{\nu}(B_{\rho})",
     [('μ', 'sub'), ('ρ', 'sub')]),

    ("631 — Operadores con contracción cruzada",
     r"\nabla_{\mu}(A^{\nu}) \partial_{\nu}(B^{\mu})",
     []),

    ("632 — Operadores sobre productos contraídos",
     r"\nabla_{\mu}(A^{\nu} B_{\nu}) \partial_{\rho}(C^{\rho})",
     [('μ', 'sub')]),

    ("633 — Operador anidado con índice libre",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super')]),

    ("634 — Operador anidado con contracción interna",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\nu}))",
     [('μ', 'sub')]),

    ("635 — Contracción entre operador externo y argumento interno",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\mu}))",
     [('ν', 'sub')]),

    ("636 — Dos niveles completamente contraídos",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\nu} B^{\mu}))",
     []),

    ("637 — Tres niveles de derivación",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(A^{\sigma})))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'sub'), ('σ', 'super')]),

    ("638 — Tres niveles con contracción progresiva",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(A^{\rho})))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("639 — Tres niveles con contracción exterior",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(A^{\mu} B^{\rho})))",
     [('ν', 'sub')]),

    ("640 — Cuatro niveles con múltiples contracciones",
     r"\nabla_{\mu}(\nabla_{\nu}(\nabla_{\rho}(\nabla_{\sigma}(A^{\sigma} B^{\rho} C^{\nu} D^{\mu}))))",
     []),

    # =============================================================================
    # 641–660 — SUMAS VÁLIDAS, PRODUCTOS Y OPERADORES PROFUNDAMENTE COMBINADOS
    # =============================================================================

    ("641 — Derivada de suma de vectores",
     r"\nabla_{\mu}(A^{\nu} + B^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("642 — Derivada de suma de covectores",
     r"\nabla_{\mu}(A_{\nu} + B_{\nu})",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("643 — Derivada de suma de escalares",
     r"\nabla_{\mu}(A + B)",
     [('μ', 'sub')]),

    ("644 — Derivada de suma de productos",
     r"\nabla_{\mu}(A^{\nu} B_{\rho} + C^{\nu} D_{\rho})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("645 — Suma de derivadas con mismo índice libre",
     r"\nabla_{\mu}(A^{\nu}) + \partial_{\mu}(B^{\nu})",
     [('μ', 'sub'), ('ν', 'super')]),

    ("646 — Suma de derivadas sobre productos",
     r"\nabla_{\mu}(A^{\nu} B_{\nu}) + \partial_{\mu}(C^{\rho} D_{\rho})",
     [('μ', 'sub')]),

    ("647 — Suma de derivadas completamente contraídas",
     r"\nabla_{\mu}(A^{\mu}) + \partial_{\nu}(B^{\nu})",
     []),

    ("648 — Suma de términos con dos índices libres",
     r"\nabla_{\mu}(A^{\nu} B_{\rho}) + \partial_{\mu}(C^{\nu} D_{\rho})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("649 — Operador externo sobre suma con contracción",
     r"\nabla_{\mu}(A^{\nu} B_{\nu} + C^{\rho} D_{\rho})",
     [('μ', 'sub')]),

    ("650 — Operador externo sobre suma con índice libre",
     r"\nabla_{\mu}(A^{\nu} B_{\rho} + C^{\nu} D_{\rho})",
     [('μ', 'sub'), ('ν', 'super'), ('ρ', 'sub')]),

    ("651 — Operador anidado sobre suma",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho} + B^{\rho}))",
     [('μ', 'sub'), ('ν', 'sub'), ('ρ', 'super')]),

    ("652 — Operador anidado sobre suma contraída",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\nu} + B^{\nu}))",
     [('μ', 'sub')]),

    ("653 — Producto de derivada y suma",
     r"A^{\mu}\nabla_{\mu}(B^{\nu} + C^{\nu})",
     [('ν', 'super')]),

    ("654 — Producto de dos operadores y suma",
     r"\nabla_{\mu}(A^{\nu} + B^{\nu}) \partial_{\nu}(C_{\rho})",
     [('μ', 'sub'), ('ρ', 'sub')]),

    ("655 — Contracción completa entre dos operadores",
     r"\nabla_{\mu}(A^{\nu}) \partial_{\nu}(B^{\mu})",
     []),

    ("656 — Cadena de operadores con producto interno",
     r"\nabla_{\mu}(\partial_{\nu}(A^{\rho} B_{\rho}))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("657 — Cadena de operadores con contracción entre niveles",
     r"\nabla_{\mu}(\partial_{\nu}(A^{\mu} B^{\nu}))",
     []),

    ("658 — Operadores anidados con tensor externo",
     r"A^{\mu}\nabla_{\mu}(\partial_{\nu}(B^{\nu} C_{\rho}))",
     [('ρ', 'sub')]),

    ("659 — Estructura profunda con suma y contracciones",
     r"\nabla_{\mu}(\nabla_{\nu}(A^{\rho} B_{\rho} + C^{\sigma} D_{\sigma}))",
     [('μ', 'sub'), ('ν', 'sub')]),

    ("660 — Caso final: operadores, suma, producto y contracciones",
     r"\nabla_{\mu}(\partial_{\nu}(A^{\mu} B^{\nu} + C^{\nu} D^{\mu}))",
     []),
]

BANCO_DE_PRUEBAS = TESTS
