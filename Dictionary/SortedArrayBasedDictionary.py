from src.adt.dictionary.Entry import Entry
from sortedcontainers import SortedList

from src.adt.list.SortedArrayList import SortedArrayList


class SortedArrayBasedDictionary(object):

    def __init__(self):
        self.__storage = SortedArrayList()

    # return the index of the provided key
    def find(self, key):
        for (i, e) in enumerate(self.__storage):
            if e.key == key:
                return i
        return -1

    # get returns value associated with provided key
    def get(self, key):
        index = self.find(key)
        if index != -1:
            return self.__storage[index].value
        return None

    def put(self, key, value):
        # update value if key already exists
        for entry in self.__storage:
            if key == entry.key:
                entry.value = value
                return
        # did not find match for key
        self.__storage.add(Entry(key, value))

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


def test_sorted_array_dic():
    dic = SortedArrayBasedDictionary()
    dic.put('Canada', 'Ottawa')
    dic.put('Turkey', 'Ankara')
    print(dic)
    print(f'Getting value associated with Turkey: {dic.get("Turkey")}')


test_sorted_array_dic()
