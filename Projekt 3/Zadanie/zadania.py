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


def zadanie1(graf):
    """
    Funkcja wypisuje sąsiadów wszystkich wierzchołków
    """
    for w in graf.keys():
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
        # Pomocnicza zmienna przettrzymujaca nazwe aktualnego wierzchołka
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
    Wszystkie wierzchołki izolowane
    """
    for w in graf:
        if not graf[w]:
            print(f"Wierzcholek {w} nie ma zadnych stopni wychodzacych")
        # TODO SPRAWDZ TERAZ CZY WIERZCHOLEK TEZ NIE MA STOPNI WCHODZACYCH.


def zadanie6(graf):
    """
    Wszystkie pętle
    """
    pass


def zadanie7(graf):
    """
    Krawedzie dwukierunkowe (?)
    """


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
    zadanie5(graf2)