import enum

RUN_LENGTH = 32


class Engine(enum.Enum):
    MockUp = 1
    Genuine = 2


def swap(data, i, j):
    data[i], data[j] = data[j], data[i]

# to find out how to calculate min-run, see:
# https://svn.python.org/projects/python/trunk/Objects/listsort.txt
def get_min_run(n):
    # default return min(32,n)
    r = 0
    while n >= RUN_LENGTH:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort_classic(items, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and items[j] < items[j - 1]:
            swap(items, j - 1, j)
            j -= 1


# sort values between start and end
def binary_insertion_sort(values, start, end):
    for i in range(start, end+1):
        value = values[i]
        position = binary_search_recursive(values, value, 0, i - 1)
        # move item at values[i] from i to position
        for j in range(i, position, -1):
            values[j] = values[j-1]
        values[position] = value


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


def merge_classic(values, start, end, middle):
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


# merge two adjacent runs according to tim-sort strategies
# strategy 1: tim-sort uses a temporary array to merge two runs
# Strategy 2 : tim-sort starts with "one pair at a time" merge mode.
# strategy 2: tim-sort switch to binary-search-based merge mode above
# threshold of winning merge element that comes from the same run
def merge_galloping(values, start, middle, end):
    print('Au galop, Hoé Hoé...')
    if middle == end:
        return
    buffer = [None]*(end-start+1)
    buffer_size = 0
    for i in range(start, middle):
        buffer[buffer_size] = values[i]
        buffer_size += 1
    for i in range(middle, end+1):
        position = binary_search_recursive(buffer, values[i], 0, buffer_size-1)
        for k in range(buffer_size, position, -1):
            buffer[k] = buffer[k-1]
        buffer[position] = values[i]
        buffer_size += 1
    for i in range(start, end+1):
        values[i] = buffer[i-start]


def timSort(items, pattern):
    n = len(items)
    min_run = get_min_run(n)
    min_run = 2
    # Sort individual sub-arrays of size RUN
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        if pattern == Engine.Genuine:
            binary_insertion_sort(items, start, end)
        else:
            insertion_sort_classic(items, start, end)
    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = min_run
    while size < n:
        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if pattern == Engine.Genuine:
                merge_galloping(items, left, mid, right)
            else:
                merge_classic(items, left, mid, right)
        size = 2 * size


def main():

    data = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, -19]
    print(f'Original data    : {data}')

    data = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, -19]
    timSort(data, pattern=Engine.MockUp)
    print(f'Mock-up Tim-sort : {data}')

    data = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, -19]
    timSort(data, pattern=Engine.Genuine)
    print(f'Genuine Tim-sort : {data}')

    # print(get_min_run(6888683))


main()
