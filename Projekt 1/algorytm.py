from random import randint
import time

def list_generator(length_of_list:int, x:int, y:int):
    """ length_of_list : int -> dlugosc listy
        x, y : int -> przedział liczbowy liczb w liscie."""

    random_list = [randint(x, y) for z in range(length_of_list)] # Tworzę za pomocą 'List comprehension'
                                                                 # listę z losowymi liczbami w podanym przedziale użytkownika.
    return random_list #Zwracam zawartość listy.
    

def find_decreasing_sequence(global_list:list):
    """global_list -> lista"""
    # print(f"Lista to: {global_list}")

    all_sequences = []                      # Tworzę listę wszystkich podciągów
    temp_sequence = []                      # Tworzę pomocniczą chwilową listę do której bedę zapisywał wyrazy które spełniają założenia podciągu
    for p in range(0, len(global_list) - 1):    # Tworzę pivota który bedzie przemierzał listę
        if global_list[p] > global_list[p + 1]:             # Jeśli lista[p] > lista[p + 1] wtedy:
            all_sequences.append([global_list[p], global_list[p + 1]])  # Dodaję ciąg dwuwyrazowy do wszystkich ciągów występujacych w podanej liście
            temp_sequence = [global_list[p], global_list[p + 1]]        # Dodaję również go do chwilowego 'pomocniczego' ciągu 
            for q in range(p + 1, len(global_list) - 1):                    # Następnie tworzę pomocniczego pivota tzw. 'q',
                                                                            # będzie on sprawdzał czy od miejsca 'list[p]' następne wyrazy są malejące.
                if global_list[q] > global_list[q + 1]:                         # Jeśli lista[q] > lista[q+1]:
                    temp_sequence.append(global_list[q + 1])                        # Dodajemy do pomocniczego ciągu ten wyraz (lista[q + 1])
                else:                                                           # Jeśli NIE:
                    if temp_sequence != all_sequences[-1]:                          # Sprawdzamy czy nasz pomocniczy ciąg
                                                                                    # NIE jest taki sam jak ten dwuwyrazowy ciąg który dodaliśmy wcześniej
                        all_sequences.append(temp_sequence)                             # Dodajemy go. 
                    temp_sequence = []                                          # Końcowo czyścimy chwilową pamięć
                    break

    return all_sequences

def test():
    """Testowanie algorytmu pod przykładowe listy z zadania."""
    test = [[5, 4, 2, 2, 1],
            [2, 5, 3],
            [1, 2, 4, 6, 7]
    ]

    result = [print(f"Tablica {test[x]} - wyniki: {find_decreasing_sequence(test[x])}") for x in range(len(test))]
    # return result

def generator_test():
    user_input = int(input('Ilosc wszystkich list:'))
    list_length = int(input('Wielkosc tych tablic:'))
    x = int(input('zakres x'))
    y = int(input('zakres y'))
    for i in range(user_input):
        tested_list = list_generator(length_of_list=list_length, x=x, y=y)
        print(find_decreasing_sequence(tested_list))

# print(test())
# test()
def check_time():

    for i in range(11):
        elements = 1000000 * i
        tested_list = list_generator(elements, 0, 10)
        start = time.time() # start 
        find_decreasing_sequence(global_list=tested_list)
        end = time.time()
        print(f"Czas dla {elements} elementów w liście: {end - start}")


if __name__ == "__main__":
    # generator_test()
    check_time()