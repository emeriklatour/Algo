from src.adt.dictionary.Entry import Entry


class UnsortedArrayDictionary(object):

    def __init__(self):
        self.__storage = []   # list of pair(k,v) <=> entry

    def find(self, key):
        for index, entry in enumerate(self.__storage):
            if key == entry.key:
                return index
        return -1

    def get(self, key):
        index = self.find(key)
        if index > -1:
            return self.__storage[index].value
        raise KeyError('Key {repr(k)} not found')

    def put(self, key, value):
        # update value if key already exists
        for entry in self.__storage:
            if key == entry.key:
                entry.value = value
                return
        # did not find match for key
        self.__storage.append(Entry(key, value))

    def delete(self, key):
        # Remove item associated with key k
        for entry in range(len(self.__storage)):
            if key == self.__storage[entry].key:
                self.__storage.pop(entry)
                return
        raise KeyError('Key not found {repr(key)}')

    def len(self):
        return len(self.__storage)

    def __iter__(self):
        for entry in self.__storage:
            yield entry.key

    def __str__(self):
        result = []
        for entry in self.__storage:
            result.append(str(entry))
        to_return = '{}'.format(',\n'.join(result))
        return '{' + to_return + '}'

    def __repr__(self):
        return self.__str__()


def test_unsorted_array_map():
    dic = UnsortedArrayDictionary()

    dic.put('Canada', 'Ottawa')
    dic.put('Turkey', 'Ankara')
    print(dic)


test_unsorted_array_map()
