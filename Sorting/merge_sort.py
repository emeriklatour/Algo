
from src.datasets.car import cars


def merge_sort(values, start, end):
    if start >= end:
        return
    middle = (start + end) // 2
    merge_sort(values, start, middle)
    merge_sort(values, middle + 1, end)
    merge(values, start, end, middle)


def merge(values, start, end, middle):
    left_copy = values[start:middle + 1]
    right_copy = values[middle + 1:end + 1]
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = start

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            values[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            values[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        values[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        values[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def main_v1():
    data = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
    merge_sort(data, 0, len(data) - 1)
    print(data)


def main_v2():
    merge_sort(cars, 0, len(cars) - 1)
    for car in cars:
        print(car)


main_v2()