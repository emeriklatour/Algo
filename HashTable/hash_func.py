def hash_code_for_string(key, number_of_buckets):
    hash_code = 0
    for letter in key:
        hash_code = hash_code + ord(letter)
    return hash_code % number_of_buckets


def hash_code_for_string_2(key, number_of_buckets):
    hash_code = 0
    power = len(key) - 1
    for letter in key:
        hash_code = hash_code + ord(letter) * 128 ** power
        power -= 1
    return hash_code % number_of_buckets


# Hashing Function to return
# key for every value. -> Colavl
def hash_code(key, number_of_buckets):
    return key % number_of_buckets


# Insert Function to add
# values to the hash table -> Colavl
def put(hashtable, key, value):
    hash_key = hash_code(key)
    hashtable[hash_key].append(value)


# Colval - DSA - Hashing
print(hash_code_for_string_2('Python', 10))
