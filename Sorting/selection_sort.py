

def selection_sort(values):
    for i in range(len(values) - 1):
        min_index = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]


def main():
    data = [3, 1, 41, 59, 26, 53, 59, -1]
    print(data)
    selection_sort(data)
    print(data)


main()
