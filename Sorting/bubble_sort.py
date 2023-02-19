

# brute force strategy
def bubble_sort_brute_force(values):
    for i in range(len(values)):
        for j in range(len(values) - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]


def bubble_sort_exit_condition(values):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(len(values) - 1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                has_swapped = True


def bubble_sort_recursive(values):
    has_swapped = False
    for i in range(len(values)-1):
        if values[i+1] < values[i]:
            values[i], values[i + 1] = values[i + 1], values[i]
            has_swapped = True
    if has_swapped:
        bubble_sort_recursive(values)
    else:
        return values


def main():
    data = [19, 13, 6, 2, 18, 8, 1]
    print(f'Original data         : {data}')

    data = [19, 13, 6, 2, 18, 8, 1]
    bubble_sort_brute_force(data)
    print(f'Brute force sort      : {data}')

    data = [19, 13, 6, 2, 18, 8, 1]
    bubble_sort_exit_condition(data)
    print(f'Exit condition sort   : {data}')

    data = [19, 13, 6, 2, 18, 8, 1]
    bubble_sort_recursive(data)
    print(f'Recursive Bubble sort : {data}')


main()
