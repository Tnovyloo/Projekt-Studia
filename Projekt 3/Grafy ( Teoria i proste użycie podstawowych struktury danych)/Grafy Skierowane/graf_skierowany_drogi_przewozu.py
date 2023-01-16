
def is_subgraph(V, V_sub):
    """
    V: graf
    V_sub: podgraf
    Sprawdzamy czy Graf "V sub" jest podgrafem grafu V,
    - Żeby jeden graf stał się podgrafem drugiego grafu, musi miec te same wierzchołki
    """

    for v in V_sub.keys():
        # Sprawdzamy czy klucz v występuje w zbiorze kluczy V
        if not v in V.keys():
            # Jesli klucz 'v' nie występuje w kluczach 'V' wiadomym jest, że nie jest podgrafem.
            print('Nie jest podgrafem', v)
            return False
        # Jeśli jest podgrafem to:
        else:
            # Sprawdzamy czy krawędzie w kluczu V są połączone w kluczu V
            for e in V_sub[v]:
                if not e in V[v]:
                    print('Brakuje krawędzi', v, e)
                    return False
    return True


if __name__ == '__main__':
    # MOŻLIWE DROGI
    lines = {
        "BE": ['IT', 'DE'],
        "IT": ['ES', 'PT'],
        "DE": ['PL'],
        "LT": ['SE'],
        "ES": ['DE', 'BE'],
        "PT": ['ES'],
        "PL": ['LT'],
        "SE": [],
    }

    # ZAPYTANIE NR.1  KLUCZ TO 'ODKĄD' A WARTOŚCI TO 'DOKĄD'
    req1 = {
        'IT': ['PT'],
        'PT': ['ES'],
        'ES': ['BE', 'DE']
    }

    # ZAPYTANIE NR.2  KLUCZ TO 'ODKĄD' A WARTOŚCI TO 'DOKĄD'
    req2 = {
        'BE': ['DE'],
        'DE': ['SE'],
    }

    # ZAPYTANIE NR.3 (Sprawdzamy dla nie istniejacego panstwa (niepowiazanego)
    req3 = {
        'GB': ['BE'],  # GB nie istnieje.
        'BE': ['DE'],
    }


    print('REQ-1', is_subgraph(lines, req1), '\n')
    print('REQ-2', is_subgraph(lines, req2), '\n')
    print('REQ-3', is_subgraph(lines, req3), '\n')