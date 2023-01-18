# GRAFY ZE SPRAWOZDANIA ZAPISANE W POSTACI LISTY KRAWEDZI
graf1 = [['A', 'B'],
         ['A', 'C'],
         ['B', 'D'],
         ['B', 'E'],
         ['C', 'B'],
         ['D', 'E'],
         ['E', 'F'],
         ['F', 'G'],
         ['G', 'H']
         ]

graf2 = [['A', 'B'],
         ['A', 'C'],
         ['A', 'I'],
         ['B', 'D'],
         ['B', 'E'],
         ['B', 'I'],
         ['C', 'B'],
         ['C', 'I'],
         ['D', 'E'],
         ['D', 'I'],
         ['E', 'F'],
         ['E', 'I'],
         ['F', 'G'],
         ['F', 'I'],
         ['G', 'H'],
         ['G', 'I'],
         ['H', 'I']
         ]

graf3 = [['A', 'B'],
         ['A', 'C'],
         ['A', 'I'],
         ['A', 'J'],
         ['B', 'D'],
         ['B', 'E'],
         ['B', 'I'],
         ['B', 'J'],
         ['C', 'B'],
         ['C', 'I'],
         ['C', 'J'],
         ['D', 'E'],
         ['D', 'I'],
         ['D', 'J'],
         ['E', 'F'],
         ['E', 'I'],
         ['E', 'J'],
         ['F', 'G'],
         ['F', 'I'],
         ['F', 'J'],
         ['G', 'H'],
         ['G', 'I'],
         ['G', 'J'],
         ['H', 'I'],
         ['H', 'J'],
         ['I', 'J'],
         ['J', 'I']
         ]

graf4 = [['A', 'B'],
         ['A', 'C'],
         ['A', 'I'],
         ['B', 'D'],
         ['B', 'E'],
         ['B', 'I'],
         ['C', 'B'],
         ['C', 'I'],
         ['D', 'E'],
         ['D', 'I'],
         ['E', 'F'],
         ['E', 'I'],
         ['F', 'G'],
         ['F', 'I'],
         ['G', 'H'],
         ['G', 'I'],
         ['H', 'I']
         ]


graf5 = [['A', 'B'],
         ['A', 'C'],
         ['B', 'D'],
         ['B', 'E'],
         ['B', 'A'],
         ['C', 'B'],
         ['D', 'E'],
         ['E', 'F'],
         ['F', 'G'],
         ['G', 'H']
         ]

# FUNKCJE DO KONKRETNYCH ZADAŃ

def zadanie1(graph: list):
    """Funkcja wypisująca wszystkich sąsiadów dla każdego wierzchołka"""

    neighbors = []
    # Dla krawędzi w liście krawędzi
    for e in graph:
        help_list = []  # Pomocnicza lista w której będe zapisywać sąsiadów wierzchołka
        v1 = e[0]       # Biorę wierzchołek z 'lewej' strony krawędzi
        for e1 in graph:
            # Jeśli wierzchołek zawiera się w krawędziach po lewej stronie dodaj go.
            if v1 == e1[0]:
                help_list.append(e1[1])

        # Dodaj tekst do listy wszystkich sąsiadów jeśli się nie powtarza
        text = [f"Wierzchołek {v1} ma sąsiadów:", help_list]
        if text not in neighbors:
            neighbors.append([f"Wierzchołek {v1} ma sąsiadów:", help_list])

    # Wypisanie sąsiadów
    for neighbor in neighbors:
        print(neighbor)

    return neighbors

def count_vertices(graph: list):
    """Funkcja liczy ilość wierzchołków w liście krawędzi"""
    all_v = []
    for e in graph:
        v1 = e[0]
        v2 = e[1]
        if v1 not in all_v:
            all_v.append(v1)
        if v2 not in all_v:
            all_v.append(v2)

    return len(all_v)


def zadanie2(graph: list):
    """Funkcja wypisująca wszyskie wierzchołki, które są sąsiadami każdego wierzchołka"""

    e_count = len(graph)             # Ilość krawędzi listy
    v_count = count_vertices(graph) - 1  # Ilość wierzchołków aby spełnic warunek, że jest sąsiadem każdego wierzchołka
    list = []

    # Dla krawędzi w grafie
    for e in graph:
        temp_list = []    # Tworze pomocniczą listę
        v1 = e[1]         # Biore wierzchołek z prawej strony listy krawędzi
        # Dla kolejnej krawędzi
        for e1 in graph:
            # Jeśli krawędź e1 i jej prawa strona (wierzchołek) jest równy aktualnemu v1
            if e1[1] == v1:
                # Jeśli wierzchołek z lewej strony listy krawedzi nie zawiera sie w pomocniczej liscie
                if e1[0] not in temp_list:
                    # Dodaje go
                    temp_list.append(e1[0])

        # Jeśli liczba wierzchołków jest równa wymaganej liczbie wierzchołków
        if len(temp_list) == v_count:
            text = [f"Wierzchołek {v1} ma sąsiadów", temp_list]
            # I jeśli nie występuje już w ogólnej liście to ją dodaj
            if text not in list:
                list.append(text)

    for i in list:
        print(i)


def zadanie3(graf):
    """Funkcja pokazujaca wszystkie stopnie wychodzące wszystkich wierzchołków"""

    return_list = []

    for e in graf:
        v1 = e[0]
        help_list = []
        for e1 in graf:
            if v1 in e1[0]:
                help_list.append([e1[0], e1[1]])

        # Pomiń duplikaty
        text = [f"Stopnie wychodzące dla {v1}:", help_list]
        if text not in return_list:
            return_list.append([f"Stopnie wychodzące dla {v1}:", help_list])

    for i in return_list:
        print(i)


def zadanie4(graf):
    pass

def zadanie5(graf):
    pass

def zadanie6(graf):
    pass

def zadanie7(graf):
    """Funkcja pokazujaca wszystkie krawedzie dwukierunkowe"""

    all_edges = []

    for e in graf:
        er = [e[1], e[0]]  # 'er' edge reversed - Krawedź odwrotna
        if er in graf:
            all_edges.append(f"Krawędź {e} i {er}")

    print(all_edges)


if __name__ == '__main__':
    print(graf1)
    print("Zadanie 1")
    zadanie1(graf1)
    print("Zadanie 2")
    zadanie2(graf2)
    print("Zadanie 3")
    zadanie3(graf2)


    print("Zadanie 7")
    zadanie7(graf5)