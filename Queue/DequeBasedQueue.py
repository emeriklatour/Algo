# https://docs.python.org/2.5/lib/deque-objects.html
# Deques are a generalization of stacks and queues
# (the name is pronounced ``deck'' and is short for ``double-ended queue'')
# append(x) : Add x to the right side of the deque.
# appendleft(x) : Add x to the left side of the deque.
# clear() : Remove all elements from the deque leaving it with length 0.
# extend(iterable) : Extend the right side of the deque by appending elements from the iterable argument.
# extendleft(iterable): Extend the left side of the deque by appending elements from iterable.
# pop() : Remove and return an element from the right side of the deque.
# If no elements are present, raises an IndexError.
# popleft() : Remove and return an element from the left side of the deque.
# If no elements are present, raises an IndexError.
# remove(value) : Removed the first occurrence of value.
# If not found, raises a ValueError. New in version 2.5.
# insert(i, a) : inserts the value mentioned in arguments(a) at index(i) specified in arguments.
# remove() : removes the first occurrence of value mentioned in arguments.
# count(x) : counts the number of occurrences of value x mentioned in arguments.

from collections import deque


class Queue(object):

    def __init__(self):
        self.__items = deque()

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        self.__items.popleft()

    def peek(self):
        return self.__items[0]

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def __str__(self):
        if self.size():
            values = [str(i) for i in self.__items]
            heap_items_str = ' -> '.join(values)
            return "Queue items are: {}".format(heap_items_str)
        else:
            return "Queue is empty."


queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.peek())
print(queue)
queue.dequeue()
print(queue.peek())
queue.dequeue()
queue.dequeue()
print(queue)
print(queue.size())
