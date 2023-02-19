import ctypes
from abc import abstractmethod


class IList:
    @abstractmethod
    def add(self, item, index):
        raise NotImplementedError

    @abstractmethod
    def add_front(self, item):
        raise NotImplementedError

    @abstractmethod
    def add_back(self, item):
        raise NotImplementedError

    @abstractmethod
    def remove(self, index):
        raise NotImplementedError

    @abstractmethod
    def remove_front(self):
        raise NotImplementedError

    @abstractmethod
    def remove_back(self):
        raise NotImplementedError

    @abstractmethod
    def get(self, index):
        raise NotImplementedError

    @abstractmethod
    def put(self, item, index):
        raise NotImplementedError

    @abstractmethod
    def find(self, item):
        raise NotImplementedError

    @abstractmethod
    def concat(self, other):
        raise NotImplementedError

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError


class LinkedNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def is_tail(self):
        return self.next_node is None

    def __str__(self):
        return str(self.value)


class ArrayList:
    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.length = 0
        self.__values = ArrayList.build_array(self.capacity)

    @staticmethod
    def build_array(capacity):
        return (capacity * ctypes.py_object)()

    def add(self, item, index):
        if not 0 <= index < self.length:
            raise IndexError
        if self.length == self.capacity:
            self.__resize(self.capacity + 1)
        for i in range(self.length - 1, index - 1, -1):
            self.__values[i + 1] = self.get(i)
        self.__values[index] = item
        self.length += 1

    def add_front(self, item):
        if self.length == self.capacity:
            self.__resize(self.capacity + 1)
        for i in range(self.length - 1, -1, -1):
            self.__values[i + 1] = self.get(i)
        self.__values[0] = item
        self.length += 1

    def add_back(self, item):
        if self.length == self.capacity:
            self.__resize(self.capacity + 1)
        self.__values[self.length] = item
        self.length += 1

    def remove(self, index):
        if not 0 <= index < self.length:
            raise IndexError
        for i in range(index, self.length - 1):
            self.__values[i] = self.get(i + 1)
        self.length -= 1

    def remove_front(self):
        for i in range(0, self.length - 1):
            self.__values[i] = self.get(i + 1)
        self.length -= 1

    def remove_back(self):
        self.length -= 1

    def get(self, index):
        if not 0 <= index < self.length:
            raise IndexError
        return self.__values[index]

    def put(self, item, index):
        if not 0 <= index < self.length:
            raise IndexError
        self.__values[index] = item

    def find(self, item):
        for i in range(self.length):
            if self.get(i) == item:
                return i
        return -1

    def concat(self, other):
        new_values = ArrayList(self.length + other.length)
        for i in range(0, self.length):
            new_values.add_back(self.get(i))
        for i in range(0, other.length):
            new_values.add_back(other.get(i))
        return new_values

    def is_empty(self):
        return self.length == 0

    def __resize(self, capacity):
        new_values = ArrayList.build_array(capacity)
        for i in range(self.length):
            new_values[i] = self.__values[i]
        self.__values = new_values
        self.capacity = capacity

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        return self.put(value, index)

    def __delitem__(self, index):
        return self.remove(index)

    def __str__(self):
        result = f'size: {self.length},  capacity: {self.capacity} ['
        for i in range(self.length):
            result = result + str(self.__values[i])
            if i < self.length - 1:
                result = result + ','
        return result + ']'


class LinkedList(IList):
    def __init__(self):
        self.__head = None
        self.length = 0

    def add(self, item, index):
        if not 0 <= index <= self.length:
            raise IndexError
        if index == 0 and self.__head is None:
            self.__head = LinkedNode(item)
        else:
            last_node = self.get(index - 1)
            next_node = last_node.next_node
            last_node.next_node = LinkedNode(item, next_node)
        self.length += 1

    def add_front(self, item):
        self.__head = LinkedNode(item, self.__head)
        self.length += 1

    def add_back(self, item):
        self.add(item, self.length)

    def remove(self, index):
        if index == 0:
            self.remove_front()
            return
        last_node = None
        node = self.__head
        for i in range(0, index):
            last_node = node
            node = node.next_node
        last_node.next_node = node.next_node
        self.length -= 1

    def remove_front(self):
        self.__head = self.__head.next_node
        self.length -= 1

    def remove_back(self):
        self.get(self.length - 2).next_node = None
        self.length -= 1

    def get(self, index):
        if index > self.length:
            raise IndexError
        node = self.__head
        for i in range(0, index):
            node = node.next_node
        return node

    def put(self, item, index):
        self.get(index).value = item

    def find(self, item):
        node = self.__head
        for i in range(0, self.length):
            if node.value == item:
                return i
            node = node.next_node
        return -1

    def concat(self, other):
        self.get(self.length - 1).next_node = other.get(0)
        self.length += other.length

    def clear(self):
        self.__head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def __str__(self):
        result = f'size: {self.length} ['
        last_node = self.__head
        while last_node is not None:
            result = result + str(last_node) + " "
            if last_node.next_node is None:
                break
            last_node = last_node.next_node
        return result + ']'


# list1 = LinkedList()
# list1.add_back("b")
# list1.add_back("d")
# list1.add_front("a")
# list1.add("c", 2)
# print(list1)
#
# list2 = LinkedList()
# list2.add_back("e")
# list2.add_back("f")
# list2.add_back("g")
# list2.add_back("h")
# print(list2)
#
# list1.concat(list2)
# print(list1)
