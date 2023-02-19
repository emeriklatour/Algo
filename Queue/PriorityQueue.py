from Queue.Heap import MinHeap
from src.datasets.movie import movies


class PriorityQueue(object):

    def __init__(self):
        self.__heap = MinHeap()

    def enqueue(self, item):
        self.__heap.insert(item)

    def first(self):
        return self.__heap.peek()

    def dequeue(self):
        if self.__heap.size() is None:
            raise ValueError("Error your queue is empty.")
        to_return = self.first()
        self.__heap.remove()
        return to_return

    def size(self):
        return self.__heap.size()

    def __str__(self):
        to_return = "["
        for i in range(len(self.__heap.keys())):
            to_return = to_return + str(self.__heap.keys()[i])
            if i < len(self.__heap.keys()) - 1:
                to_return = to_return + ',\n'
        return to_return + ']'


movie_queue = PriorityQueue()

movie_queue.enqueue(movies[0])
movie_queue.enqueue(movies[1])
movie_queue.enqueue(movies[2])
movie_queue.enqueue(movies[3])
movie_queue.enqueue(movies[4])
print(movie_queue)
print(movie_queue.size())
movie_queue.dequeue()
movie_queue.dequeue()
movie_queue.dequeue()
print(movie_queue)


