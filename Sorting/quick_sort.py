from random import random


def swap(data, i, j):
    data[i], data[j] = data[j], data[i]


def quick_sort(values, low, high):
    if low < high:
        # pivot = rand_partition(values, low, high)
        pivot = partition(values, low, high)
        quick_sort(values, low, pivot - 1)
        quick_sort(values, pivot + 1, high)


# put the pivot element in its proper place.
# return the position of the pivot
def partition(values, start, end):
    # make the first element as pivot element
    pivot = values[start]
    # rearrange the array by putting elements which are less
    # than pivot on one side and which are greater that on other.
    i = start + 1
    for j in range(i, end + 1):
        if values[j] < pivot:
            swap(values, i, j)
            i = i + 1
    swap(values, start, i - 1)
    return i - 1


# randomized version of the partition function
def rand_partition(values, start, end):
    # chooses position of pivot randomly by using rand() function
    random_number = int(start + random() % (end - start + 1))
    swap(values, random_number, start)
    return partition(values, start, end)


def main():
    data = [-1, 19, 13, 6, 2, 18, 8, -2]
    print(data)
    low = 0
    high = len(data) - 1
    quick_sort(data, low, high)
    print(data)


main()
