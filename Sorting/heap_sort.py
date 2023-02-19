from heapq import heappop, heappush
from src.datasets.movie import movies


def heap_sort(values):
    heap = []
    # build heap
    for element in values:
        heappush(heap, element)

    sorted_values = []
    while heap:
        sorted_values.append(heappop(heap))
    return sorted_values


def main_v1():
    data = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
    print(data)
    print(heap_sort(data))


def main_v2():
    for movie in heap_sort(movies):
        print(movie)


main_v2()
