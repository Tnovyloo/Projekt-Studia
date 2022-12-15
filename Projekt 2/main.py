from random import randint
import time
from functools import lru_cache

def max_func(array):
    temp = 0
    for num in array:
        if num > temp:
            temp = num
    return temp


def list_generator(length_of_list:int, x:int, y:int):
    """ length_of_list : int -> dlugosc listy
        x, y : int -> przedział liczbowy liczb w liscie."""
    random_list = [randint(x, y) for z in range(length_of_list)]

    return random_list


def bucket_sort(array):
    # znajdź największą wartość w tablicy przy pomocy funkcji wbudowanej bądź zrobionej ręcznie.
    max_value = max(array)
    # print(max_value)

    # max_value = max_func(array)
    # print(max_value)
    bucket_list = [0] * (max_value + 1) # stwórz listę kubełków
    # przejdź przez tablicę i zwiększ wartość w kubełku o 1
    for i in range(len(array)):
        bucket_list[array[i]] += 1
    # przejdź przez listę kubełków i dodaj wartości do tablicy
    index = 0
    for i in range(len(bucket_list)):
        for j in range(bucket_list[i]):
            array[index] = i
            index += 1

    return array


def quick_sort(array):
    if len(array) < 2: # Jesli tablica jest mniejsza od dwóch to ją zwróć
        return array
    else:
        pivot = array[0] # Bazowy element
        less = quick_sort([i for i in array if i < pivot]) # Lista elementow mniejszych od bazowego
        greater = quick_sort([i for i in array if i > pivot]) # Lista elementow wiekszych od bazowego
        return less + [pivot] + greater

def test():
    amount = 1000000
    for i in range(1, 10):
        random_array_user = list_generator(amount * i, 0, 100)
        # print(random_array_user)

        print(f"Czas sortowania dla {amount*i} elementów")

        start = time.time()
        sorted1 = bucket_sort(random_array_user)
        end = time.time()
        print(f"Kubełkowy: {round(end-start, 2)}s")
        # print(sorted1)

        start = time.time()
        sorted2 = quick_sort(tuple(random_array_user))
        end = time.time()
        print(f"Quick Sort: {round(end-start, 2)}s")
        # print(sorted2)

    return print("Koniec")

def test2():
    random_array_user = list_generator(5, 0, 51)
    print(f"{random_array_user} - Przykładowa tablica")
    print(bucket_sort(random_array_user), "- sortowanie BucketSort")
    print(quick_sort(random_array_user), "- sortowanie QuickSort")


if __name__ == '__main__':
    test()
    # test2()
    