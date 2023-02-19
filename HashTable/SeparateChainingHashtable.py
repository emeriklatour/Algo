# separate chaining / closed addressing hash table

class SeparateChainingHashtable(object):

    def __init__(self, capacity=1000):
        # List of lists
        self.storage = [[] for _ in range(capacity)]
        self.capacity = capacity
        self.length = 0

    def put(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        hashed_key = hash(key)
        storage_index = hashed_key % self.capacity
        for element in self.storage[storage_index]:
            if key == element[0]:  # already exist, update it
                element[1] = value
                break
        else:
            # separate chaining strategy :
            # create a chain of values in the same bucket
            # by using another data structure (in this case a list).
            self.storage[storage_index].append([key, value])
            self.length += 1

    def __getitem__(self, key):
        hashed_key = hash(key)
        storage_index = hashed_key % self.capacity
        for element in self.storage[storage_index]:
            if element[0] == key:
                return element[1]
        raise KeyError(f'Key {key} not found')

    def __delitem__(self, key):
        hashed_key = hash(key)
        storage_index = hashed_key % self.capacity
        for sub_list in self.storage[storage_index]:
            if key == sub_list[0]:
                self.storage[storage_index].remove(sub_list)
                self.length -= 1
                return
        raise KeyError('Key {key} not found')

    def __contains__(self, key):
        hashed_key = hash(key)
        storage_index = hashed_key % self.capacity
        for element in self.storage[storage_index]:
            if element[0] == key:
                return True
        return False

    def __len__(self):
        return self.length

    def __iterate_kv(self):
        for sub_list in self.storage:
            if not sub_list:
                continue
            for element in sub_list:
                yield element

    def __iter__(self):
        for key_value in self.__iterate_kv():
            yield key_value[0]

    def keys(self):
        return self.__iter__()

    def values(self):
        for key_value in self.__iterate_kv():
            yield key_value[1]

    def items(self):
        return self.__iterate_kv()

    def get(self, key):
        try:
            return self.__getitem__(key)
        except KeyError:
            return None

    find = get

    def __str__(self):
        result = []
        for element in self.storage:
            for key_value in element:
                if isinstance(key_value[0], str):
                    key_str = '\'{}\''.format(key_value[0])
                else:
                    key_str = '{}'.format(key_value[0])
                if isinstance(key_value[1], str):
                    value_str = '\'{}\''.format(key_value[1])
                else:
                    value_str = '{}'.format(key_value[1])
                result.append('{}: {}'.format(key_str, value_str))
        key_value_pairs_str = '{}'.format(', '.join(result))
        return '{' + key_value_pairs_str + '}'

    def __repr__(self):
        return self.__str__()


def test_separate_chaining_hashtable():
    ht = SeparateChainingHashtable()
    ht['Canada'] = 'Ottawa'
    ht['Turkey'] = 'Ankara'
    print(ht['Turkey'])
    for key in ht.keys():
        print(f'({key}, {ht.get(key)})')
    print(ht)

    if 'Canada' in ht:
        print('Canada is found')
    else:
        print('Canada not found')


# test_separate_chaining_hashtable()

