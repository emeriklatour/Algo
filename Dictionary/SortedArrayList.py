from src.adt.wn.list import ArrayList


class SortedArrayList:
    def __init__(self, items=None):
        self.__items = ArrayList()
        if items is not None:
            for item in items:
                self.add(item)

    def find(self, item):
        return self.__binary_search(item, 0, self.size() - 1)

    def get(self, item):
        index = self.find(item)
        if index < 0:
            return None
        return self.__items[index]

    def add(self, item):
        self.__insert_at(item, self.__find_insert_index(item))

    def remove(self, item):
        index = self.find(item)
        if index >= 0:
            self.__remove_at(index)

    def size(self):
        return self.__items.length

    def __find_insert_index(self, item):
        for index, entry in enumerate(self.__items):
            if item < entry:
                return index
        return self.size()

    def __binary_search(self, item, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if item == self.__items[middle]:
            return middle
        if item < self.__items[middle]:
            return self.__binary_search(item, start, middle - 1)
        return self.__binary_search(item, middle + 1, end)

    def __len__(self):
        return self.size()

    length = __len__

    def __insert_at(self, item, index):
        self.__items.add_back(None)
        for i in range(self.length() - 1, index, -1):
            self.__items[i] = self.__items[i - 1]
        self.__items[index] = item

    def __remove_at(self, index):
        for i in range(index, self.size() - 1):
            self.__items[i] = self.__items[i + 1]
        del self.__items[self.size() - 1]

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, item):
        return self.remove(item)

    def __iter__(self):
        for item in self.__items:
            yield item

    def __str__(self):
        return str(self.__items)


def sorted_test():
    sorted_arr = SortedArrayList([5, 2, 8, 32, 9])
    print(sorted_arr)
    sorted_arr.add(1)
    sorted_arr.add(10)
    sorted_arr.add(1000)
    print(sorted_arr)
    sorted_arr.remove(8)
    print(sorted_arr)


sorted_test()
