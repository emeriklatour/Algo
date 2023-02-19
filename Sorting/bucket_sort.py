import math


def bucket_sort(input_values):
    max_value = max(input_values)
    # size = max_value/len(input_values)
    size = math.sqrt(len(input_values))

    # Create empty buckets
    buckets = []
    for x in range(len(input_values)):
        buckets.append([])

    # Put items into their respective bucket based on the size
    for value in input_values:
        index_bucket = int(value / size)
        if index_bucket != len(input_values):
            buckets[index_bucket].append(value)
        else:
            buckets[len(input_values) - 1].append(value)

    # Sort elements within the buckets using Insertion Sort
    for index in range(len(input_values)):
        insertion_sort(buckets[index])

    # Concatenate buckets with sorted elements into a single list
    sorted_values = []
    for index in range(len(input_values)):
        sorted_values = sorted_values + buckets[index]
    return sorted_values


def insertion_sort(bucket):
    for i in range(1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while j >= 0 and var < bucket[j]:
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var


def main():
    # input_data = [1.20, 0.22, 0.43, 0.36, 0.39, 0.27]
    input_data = [8, 7, 6, 5]
    print('ORIGINAL DATA:')
    print(input_data)
    sorted_list = bucket_sort(input_data)
    print('SORTED DATA:')
    print(sorted_list)


main()



