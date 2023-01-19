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
         ['H', 'I'],
         ['J', 'J'],
         # ['H', 'J']
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
         ['G', 'H'],
         ['A', 'A'],
         ['H', 'H'],
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


def zadanie3(graph):
    """Funkcja pokazujaca wszystkie stopnie wychodzące wszystkich wierzchołków"""

    return_list = []

    for e in graph:
        v1 = e[0]
        help_list = []
        for e1 in graph:
            # Jeśli wierzchołek 'v1' zawiera się w elemencie listy krawędzi (0 miejsec) to je dodaj
            if v1 in e1[0]:
                help_list.append([e1[0], e1[1]])

        # Pomiń duplikaty
        text = [f"Stopnie wychodzące dla {v1}:", help_list]
        if text not in return_list:
            return_list.append([f"Stopnie wychodzące dla {v1}:", help_list])

    for i in return_list:
        print(i)


def zadanie4(graph):
    """Funkcja wypisujaca wszystkie stopnie wchodzace do wierzcholków"""
    return_list = []

    for e in graph:
        # Bierzemy drugi wierzcholek z listy krawedzi
        v1 = e[1]
        help_list = []
        for e1 in graph:
            # Jesli w elemencie listy krawedzi na drugim miejscu zawiera sie ten sam wierzchołek to go dodaj.
            if v1 in e1[1]:
                help_list.append([e1[0], e1[1]])
        # Pomiń duplikaty
        text = [f"Stopnie wchodzące do wierzchołka {v1}:", help_list]
        if text not in return_list:
            return_list.append([f"Stopnie wchodzące do wierzchołka {v1}:", help_list])

    for i in return_list:
        print(i)


def zadanie5(graph):
    """Funkcja wypisująca wierzchołki izolowane.
        (Czyli w sumie takie które tworzą pętle z samym sobą,
        oraz nie są sąsiadami i nie mają sąsiadów)"""

    return_list = []

    for e in graph:
        help_list = []
        v1 = e[0]
        v2 = e[1]
        # Sprawdzamy czy dwa wierzchołki są takie same w tym elemencie listy
        if v1 == v2:
            # Wchodzimy w petle ktora sprawdzi czy nie ma innych krawedzi,
            # które zawierają wierzchołek
            for e1 in graph:
                if e1[0] == v1 or e1[1] == v1 is False:
                    help_list.append(e)
                else:
                    help_list = []
        # Jeśli lista nie jest pusta to ją dodaj do listy zwracanej.
        if help_list:
            return_list.append(help_list)

    for i in return_list:
        print(f"Wierzchołki izolowane to:", i[0][0])


def zadanie6(graph):
    """
    Funkcja wypisująca wszystkie pętle
    """

    # PRÓBA WYPISANIA CYKLU W GRAFIE.
    # edges_len = len(graph)
    #
    # for e in graph:
    #     print("Dla krawędzi", e)
    #     # DLa np ['A', 'B'] bierzemy wartość 'B' i
    #     # musimy wziąc wszystkie krawędzie które kierują sie do 'B' i będziemy szukać czy dązą do 'A'
    #     v = e[1]
    #     temp_list = []
    #     for e1 in graph:
    #         if e1[1] == v:
    #             # Tworze pomocniczą listę krawedzi wchodzacych do 'B'
    #             temp_list.append(e1)
    #
    #     for e1 in temp_list:
    #         v1 = e1[0]
    #         v2 = e1[1]
    #         if e1 == e:
    #             temp_list.remove(e1)
    #         else:
    #             boolean = True
    #             while boolean:
    #                 for e2 in graph:
    #                     if v in e2[1]:
    #                         return_list.append([e2, e1, e])
    #                     if v1 in e2[1]:
    #
    #
        #
        # for e1 in temp_list:
        #     if
        # print(temp_list)


    # # https://networkx.org/documentation/stable/_modules/networkx/algorithms/cycles.html
    # import networkx as nx
    #
    # G = nx.DiGraph(graph)
    #
    # for cycle in nx.simple_cycles(G):
    #     print(f"Pętla {cycle}")


    # PĘTLA TO CO INNEGO NIŻ CYKL - ODNOTOWANO :D
    return_list = []

    for e in graph:
        if e[0] == e[1]:
            return_list.append(e)

    for i in return_list:
        print(f"Pętle", i)



def zadanie7(graph):
    """Funkcja pokazujaca wszystkie krawedzie dwukierunkowe"""

    all_edges = []

    for e in graph:
        er = [e[1], e[0]]  # 'er' - 'edge reversed' - Krawedź odwrotna
        # Jeśli odwrócona krawedź znajduje się w liscie krawedzi to ją dodaj
        if er in graph:
            if not er[0] == er[1]:
                all_edges.append(f"Krawędź {e} i {er}")

    for i in all_edges:
        print(i)


if __name__ == '__main__':
    print("Zadanie 1")
    zadanie1(graf1)
    print("Zadanie 2")
    zadanie2(graf2)
    print("Zadanie 3")
    zadanie3(graf2)
    print("Zadanie 4")
    zadanie4(graf2)
    print("Zadanie 5")
    zadanie5(graf4)
    print("Zadanie 6")
    zadanie6(graf5)
    print("Zadanie 7")
    zadanie7(graf5)