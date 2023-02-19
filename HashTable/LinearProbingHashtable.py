

class LinearProbingHashTable(object):

    def __init__(self):
        self.max_length = 10
        self.max_load_factor = 0.75
        self.length = 0
        self.storage = [None for _ in range(self.max_length)]
        # self.storage =  [None] * self.max_length

    def __len__(self):
        return self.length

    def _hash(self, key):
        return hash(key) % self.max_length

    def _increment_key(self, key): # Linear probing
        return (key + 1) % self.max_length

    def put(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        self.length += 1
        hashed_key = self._hash(key)
        while self.storage[hashed_key] is not None:
            if self.storage[hashed_key][0] == key:
                self.length -= 1
                break
            hashed_key = self._increment_key(hashed_key)
        new_tuple = (key, value)
        self.storage[hashed_key] = new_tuple
        if self.length / float(self.max_length) >= self.max_load_factor:
            self._resize()

    def get(self, key):
        return self.__getitem__(key)

    def remove(self, key):
        self.__delitem__(key)

    def __getitem__(self, key):
        index = self._find_item(key)
        return self.storage[index][1]

    def __delitem__(self, key):
        index = self._find_item(key)
        self.storage[index] = None

    def _find_item(self, key):
        hashed_key = self._hash(key)
        if self.storage[hashed_key] is None:
            raise KeyError
        if self.storage[hashed_key][0] != key:
            original_key = hashed_key
            while self.storage[hashed_key][0] != key:
                hashed_key = self._increment_key(hashed_key)
                if self.storage[hashed_key] is None:
                    raise KeyError
                if hashed_key == original_key:
                    raise KeyError
        return hashed_key

    def _resize(self):
        self.max_length *= 2
        self.length = 0
        old_table = self.storage
        self.storage = [None] * self.max_length
        for tuple in old_table:
            if tuple is not None:
                self[tuple[0]] = tuple[1]

    def get(self, key):
        try:
            return self.__getitem__(key)
        except KeyError:
            return None

    def __iterate_kv(self):
        for entry in self.storage:
            if not entry:
                continue
            yield entry

    def __iter__(self):
        for key_value in self.__iterate_kv():
            yield key_value[0]

    def keys(self):
        return self.__iter__()


def test_linear_probing_hashtable():
    ht = LinearProbingHashTable()
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


test_linear_probing_hashtable()

