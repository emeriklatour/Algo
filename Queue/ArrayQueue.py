
import ctypes


class Queue(object):

    def __init__(self, capacity: int = 100):
        self.__capacity = capacity
        self.__front = 0
        self.__rear = 0
        self.__items = Queue.build_array(self.__capacity)

    def enqueue(self, item):
        if self.__capacity == self.__rear:
            print('Queue is full.')
            return
        self.__items[self.__rear] = item
        self.__rear += 1

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        to_return = self.__items[self.__front]
        self.shift_left(self.__front)
        self.__rear -= 1
        return to_return

    def shift_left(self, index):
        for i in range(index, self.__rear - 1):
            self.__items[i] = self.__items[i+1]

    def is_empty(self):
        if self.__front == self.__rear == 0:
            return True
        return False

    def __len__(self):
        return self.__rear

    length = __len__

    def peek(self):
        return self.__items[self.__front]

    def is_empty(self):
        return self.size() == 0

    size = __len__

    @staticmethod
    def build_array(new_capacity):
        return (new_capacity * ctypes.py_object)()

    def is_empty(self) -> bool:
        if self.length == 0:
            return True
        return False

    def __str__(self):
        to_return = "["
        for i in range(self.__rear):
            to_return = to_return + str(self.__items[i])
            if i < self.__rear - 1:
                to_return = to_return + ','
        return to_return + ']'


queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
print(queue.size())

print(queue.peek())

queue.dequeue()
queue.dequeue()
print(queue)
print(queue.size())




