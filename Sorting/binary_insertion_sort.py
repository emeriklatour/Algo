
def insertion_sort_classic(values):
    for index in range(0, len(values)):
        current_position = index
        value_to_sort = values[index]
        while current_position > 0 and \
                values[current_position - 1] > value_to_sort:
            values[current_position] = values[current_position - 1]
            current_position -= 1
        values[current_position] = value_to_sort


# sort values between start and end
def binary_insertion_sort(values, start, end):
    for i in range(start, end):
        value = values[i]
        position = binary_search_recursive(values, value, 0, i - 1)
        # move item at values[i] from i to position
        values = values[:position] + [value] + values[position:i] + values[i + 1:]
        # for j in range(i, position, -1):
        #    values[j] = values[j-1]
        # values[position] = value
    return values


def binary_insertion_sort_all(values):
    return binary_insertion_sort(values, 1, len(values))


# return position of item to insert
def binary_search_recursive(items, item_to_insert, start, end):
    if start == end:
        if items[start] > item_to_insert:
            return start
        else:
            return start + 1
    if start > end:
        return start
    middle = (start + end) // 2
    if item_to_insert == items[middle]:
        return middle
    if item_to_insert < items[middle]:
        return binary_search_recursive(items, item_to_insert, start, middle - 1)
    else:
        return binary_search_recursive(items, item_to_insert, middle + 1, end)


def main():
    data = [-22, 99, 78, 56, 42, 36, 23, 11, 6, 2, 1, -4]
    print(f'Original data             : {data}')

    data = [-22, 99, 78, 56, 42, 36, 23, 11, 6, 2, 1, -4]
    insertion_sort_classic(data)
    print(f'Classic insertion sort    : {data}')

    data = [-22, 99, 78, 56, 42, 36, 23, 11, 6, 2, 1, -4]
    data = binary_insertion_sort_all(data)
    print(f'Binary insertion sort     : {data}')

    data = [-22, 99, 78, 56, 42, 36, 23, 11, 6, 2, 1, -4]
    data = binary_insertion_sort(data, start=0, end=len(data)//2)
    print(f'Binary insertion portion  : {data}')

main()
