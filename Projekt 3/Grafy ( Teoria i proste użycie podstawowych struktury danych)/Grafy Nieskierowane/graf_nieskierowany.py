
def who_knows_person(person:str, e:list):
    """
    Funkcja, która zwraca listę osób, ktora zna "person" - podaną osobę
    """
    friends = []
    for p1, p2 in e:
        if p1 == person:
            friends.append(p2)
        if p2 == person:
            friends.append(p1)
    return friends


if __name__ == '__main__':
    # Założenia:
    #   Krawędzie - definiują czy ktoś się z kimś zna
    #   P - Princess - Księżna
    #   Q - Queen - Królewna
    #   K - King - Król
    #   H - Hunter - Leśniczy
    #   D1 - Dwarf_1 - Krasnolud nr.1
    #   D2 - Dwarf_2 - Krasnolud nr.2

    # V opisuję nasze osoby będące na grafie.
    V = ['Princess', 'Dwarf1', 'Dwarf2', 'King', 'Queen', 'Hunter']

    # E opisuje nasze 'relacje' - krawędzie
    E = [
        ['Princess', 'Dwarf1'], ['Princess', 'Dwarf2'], ['Dwarf1', 'Dwarf2'],
        ['Princess', 'King'], ['Princess', 'Queen'], ['Princess', 'Hunter'],
        ['King', 'Queen'], ['King', 'Hunter'], ['Queen', 'Hunter']
    ]

    for person in V:
        print(f"Osoby które znają {person}: \n{who_knows_person(person, E)}")
