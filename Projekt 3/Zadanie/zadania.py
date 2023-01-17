# import enum

graf1 = {
    "A": ['B', 'C'],
    "B": ['D', 'E'],
    "C": ['B'],
    "D": ['E'],
    "E": ['F'],
    "F": ['G'],
    "G": ['H'],
    "H": [],
}

graf2 = {
    "A": ['B', 'C', 'I'],
    "B": ['D', 'E', 'I'],
    "C": ['B', 'I'],
    "D": ['E', 'I'],
    "E": ['F', 'I'],
    "F": ['G', 'I'],
    "G": ['H', 'I'],
    "H": ['I'],
    "I": [],
}

graf3 = {
    "A": ['B', 'C', 'I', "J"],
    "B": ['D', 'E', 'I', "J"],
    "C": ['B', 'I', "J"],
    "D": ['E', 'I', "J"],
    "E": ['F', 'I', "J"],
    "F": ['G', 'I', "J"],
    "G": ['H', 'I', "J"],
    "H": ['I', "J"],
    "I": ["J"],
    "J": ["I"],
}

graf4 = {
    "A": ['B', 'C', 'I'],
    "B": ['D', 'E', 'I'],
    "C": ['B', 'I'],
    "D": ['E', 'I'],
    "E": ['F', 'I'],
    "F": ['G', 'I'],
    "G": ['H', 'I'],
    "H": ['I'],
    "I": [],
    "J": [],
}


graf5 = {
    "A": ['B', 'C'],
    "B": ['D', 'E', 'A'],
    "C": ['B'],
    "D": ['E'],
    "E": ['F'],
    "F": ['G'],
    "G": ['H'],
    "H": [],
}

def zadanie1(graf):
    """
    Funkcja wypisuje sąsiadów wszystkich wierzchołków
    """
    for w in graf.keys():
        # Jeśli wartość dla klucza 'w' istnieje to wypisz ją
        if graf[w]:
            print(f"Dla wierzchołka {w} sąsiadami są:{graf[w]}")
        else:
            print(f"Wierzchołek {w} nie ma sąsiadów")


def zadanie2(graf):
    """
    Funkcja wypisuje wszystkie wierzchołki które są sąsiadami każdego wierzchołka
    """

    # Zmienna przechowująca ile wierzchołek musi mieć sąsiadów
    how_much_neighbors = len(graf.keys()) - 1
    # Zmienna przechowujaca sasiadow kazdego wierzcholka
    list_neighbors = []

    for w in graf.keys():
        # Zmienna licząca sąsiadów, w pózniejszym etapie porównuje ją ze
        # zmienną 'how_much_neighbors'
        temp = 0

        # Nazwa naszego wierzchołku będąca typem STRING aby porównać ją z wartościami
        # sąsiadów wierzchołków
        w_text = str(w)

        # Wchodze w drugą petle i sprawdzam czy wartosc w_text zawiera sie w
        # w krawedziach wierzcholkow
        for w1 in graf.keys():
            if w_text in graf[w1]:
                temp += 1

            if temp == how_much_neighbors:
                list_neighbors.append(w)
                temp = 0

    print("Wierzchołki będace sąsiadami wszystkich wierzchołków to", list_neighbors)


def zadanie3(graf):
    """
    Liczenie stopni wychodzących z danego wierzchołka
    """
    for w in graf.keys():
        print(f"Stopnie wychodzące wierzchołka {w}")
        print(f"{w} - {graf[w]} - Ilośc {len(graf[w])}")


def zadanie4(graf):
    """
    Liczenie stopni wchodzących do wierzchołka
    """
    for w in graf.keys():
        # Pomocnicza zmienna przetrzymujaca nazwe aktualnego wierzchołka
        w_text = str(w)

        # Zmienna przetrzymująca stopnie wchodzace do wierzcholka
        list_out = []

        # Dla kolejnego wierzchołka 'w1' i jego wartości
        for w1 in graf.keys():
            # Jeśli wierzcholek 'w' zawiera sie w wartosciach 'w1'
            if w_text in graf[w1]:
                # Dodaj go do 'list-out' tzn wierzcholkow wychodzacych
                list_out.append(w1)

        print(f"Wchodzace stopnie do wierzcholka {w} to {list_out}")


def zadanie5(graf):
    """
    Funkcja znajduje wszystkie wierzchołki izolowane w grafie
    """
    izolated = []

    for w in graf:
        # Jesli graf nie ma zadnych stopni wychodzacych to sprawdz czy nie ma rowniez krawedzi wchodzacych
        if not graf[w]:
            w_text = str(w)
            list_out = []
            for w1 in graf.keys():
                if w_text in graf[w1]:
                    list_out.append(w1)
                    # return print(f"Wierchołek {w} nie ma wychodzacych ale wchodzi do niego {w1}")
            # Jeśli lista wchodzących stopni do wierzcholka jest pusta to zwróc te wartości
            if not list_out:
                izolated.append(w)
                print("Wierzchołki izolowane to: ", izolated)
                return izolated


def zadanie6(graf):
    """
    Funkcja wypisująca wszystkie pętle
    """

    # PRÓBA BEZ INTERNETU (ZOSTAWIAM KOD DLA WIARYGODNOŚCI PRÓBOWANIA ZROBIENIA TEGO SAMEMU.)
    # - KOD NIE DZIAŁAJĄCY - PONIŻEJ UDANA IMPLEMENTACJA
    # all_loops = []
    # Dla wierzcholka i jego schodków
    # for w in graf.keys():
    #     # Dla wszystkich wierzchołków i jego wartości
    #     for w1 in graf[w]:
    #         # Wez aktualne schodki wierzcholka
    #         actual_w = graf[w1]
    #         # Sprawdz czy wierzcholek "w" zawiera się w schodkach "w1"
    #         if w in actual_w:
    #             # Dodajemy pętle potrójną tzn, są tylko dwa schodki i te wierzcholki sa swoimi sasiadami.
    #             all_loops.append([w, w1, w])
    #         else:
    #             # bool1 = True
    #             # way = []
    #             # while bool1:
    #             #     for w2 in graf[w1]:
    #             #         actual_w2 = graf[w2]
    #             #         if w in actual_w2:
    #             #             way.append(w2)
    #             #     bool1 = False
    #             # all_loops.append(way)
    #                     # else:
    #                     #     bool2 = True
    #                     #     while bool2:
    # print(all_loops)

    # OBSERWACJA - ORAZ ROZWIĄZANIE
    # Jak dotąd udało mi się wszystkie zadania z wyłączeniem zadania 6
    # zrobić bez żadnej pomocy internetu. Po kilku próbach nieudanego pisania kodu
    # doszedłem do konkluzji iż jest to nie do zrobienia
    # na moim aktualnym poziomie z algorytmów i struktur danych na pythonowych dictach.
    # Szukając odpowiedźi w internecie znalazłem gotową bibliotekę 'networkx'
    # LINK DO ŹRÓDLA INFORMACJI.
    # https://stackoverflow.com/questions/59820748/how-to-detect-a-cycle-in-a-directed-graph-with-python

    # Do uruchomienia wpisać komende "pip install networkx"
    import networkx as nx

    # TWORZE KRAWĘDZIE I ZAPISUJE JE DO LISTY W TYPIE 'TUPLE'
    edges = []
    for w in graf:
        for w1 in graf[w]:
            edges.append((w, w1))
    # print(edges)
    G = nx.DiGraph(edges)

    for cycle in nx.simple_cycles(G):
        print(cycle)


def zadanie7(graf):
    """
    Krawedzie dwukierunkowe
    """
    two_way = []

    # Dla wierzcholka i jego schodków
    for w in graf.keys():
        # Dla wszystkich wierzchołków i ich wartości
        for w1 in graf[w]:
            # Wez aktualne schodki wierzcholka
            actual_w = graf[w1]
            # Sprawdz czy wierzcholek "w" zawiera się w schodkach "w1"
            if w in actual_w:
                # Dodajemy dwukierunek
                two_way.append([w, w1])

    print(two_way)

if __name__ == '__main__':
    print("Zadanie 1")
    zadanie1(graf1)
    print("Zadanie 2")
    zadanie2(graf2)
    print("Zadanie 3")
    zadanie3(graf2)
    print("Zadadnie 4")
    zadanie4(graf2)
    print("Zadanie 5")
    zadanie5(graf4)
    print("Zadanie 6")
    zadanie6(graf5)
    print("Zadanie 7")
    zadanie7(graf5)