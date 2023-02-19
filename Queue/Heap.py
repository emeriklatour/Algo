
class MinHeap(object):

    def __init__(self):
        self.__keys = [None]
        self.current_size = 0

    def insert(self, key):
        # print('Inserting' + str(key))
        self.__keys.append(key)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def heapify_up(self, index: int):
        while index // 2 > 0:
            if self.__keys[index] < self.__keys[index // 2]:
                swap = self.__keys[index // 2]
                self.__keys[index // 2] = self.__keys[index]
                self.__keys[index] = swap
            index = index // 2

    def peek(self):
        return self.__keys[1]

    def remove(self):
        to_return = self.__keys[1]
        self.__keys[1] = self.__keys[self.current_size]
        self.current_size -= 1
        self.__keys.pop()
        self.heapify_down(1)
        return to_return

    def heapify_down(self, index: int):
        while (index * 2) <= self.current_size:
            min_child = self.min_child(index)
            if self.__keys[index] > self.__keys[min_child]:
                swap = self.__keys[index]
                self.__keys[index] = self.__keys[min_child]
                self.__keys[min_child] = swap
            index = min_child

    def min_child(self, index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        else:
            if self.__keys[index * 2] < self.__keys[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def build_heap(self, keys):
        i = len(keys) // 2
        self.current_size = len(keys)
        self.__keys = [None] + keys[:]
        while i > 0:
            self.heapify_down(i)
            i = i - 1

    def size(self):
        return self.current_size

    length = size

    def keys(self):
        return self.__keys


def test():
    my_heap = MinHeap()
    # my_heap.build_heap([9, 6, 5, 2, 3, 1])
    my_heap.insert(9)
    my_heap.insert(6)
    my_heap.insert(5)
    my_heap.insert(2)
    my_heap.insert(3)
    my_heap.insert(1)
    print(my_heap.keys())
    my_heap.remove()
    print(my_heap.keys())
    my_heap.remove()
    print(my_heap.keys())
    my_heap.remove()
    print(my_heap.keys())


# test()
