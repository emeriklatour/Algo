

def insertion_sort(values):
    for index in range(0, len(values)-1):
        current_position = index
        value_to_sort = values[index]
        while current_position > 0 and \
                values[current_position - 1] > value_to_sort:
            values[current_position] = values[current_position - 1]
            current_position -= 1
        values[current_position] = value_to_sort


def main():
    data = [3, 1, 41, 59, 26, 53, 59]
    print(data)
    insertion_sort(data)
    print(data)


main()
