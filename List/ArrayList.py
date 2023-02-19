import ctypes
from List.IList import IList


class ArrayList(object):

    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.length = 0
        self.__items = ArrayList.build_array(self.capacity)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if not 0 <= index < self.length:
            return IndexError('Provided index is out of bounds')
        return self.__items[index]

    def add_back(self, item):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.__items[self.length] = item
        self.length += 1

    def insert_at(self, item, index):
        if not 0 <= index < self.length:
            print("Please provide an appropriate index [0<=index<length]...")
            return
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.length - 1, index - 1, -1):
            self.__items[i + 1] = self.__items[i]
        self.__items[index] = item
        self.length += 1

    def add_front(self, item):
        for i in range(self.length - 1, -1, -1):
            self.__items[i + 1] = self.__getitem__(i)
        self.__items[0] = item
        self.length += 1

    def __str__(self):
        to_return = "["
        for i in range(self.length):
            to_return = to_return + str(self.__items[i])
            if i < self.length - 1:
                to_return = to_return + ','
        return to_return + ']'

    def _resize(self, new_capacity):
        new_items = ArrayList.build_array(new_capacity)
        for i in range(self.length):
            new_items[i] = self.__items[i]
        self.__items = new_items
        self.capacity = new_capacity

    @staticmethod
    def build_array(new_capacity):
        return (new_capacity * ctypes.py_object)()

    def get(self, index):
        return self.__getitem__(index)

    def is_empty(self) -> bool:
        if self.length == 0:
            return True
        return False


