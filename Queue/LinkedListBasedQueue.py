from List.SinglyLinkedList import SinglyLinkedList


class QueueUsingInheritance(object, SinglyLinkedList):

    def enqueue(self, item):
        self.add_back(item)

    def dequeue(self):
        self.remove_front()


class QueueUsingDelegation(object):

    def __init__(self):
        self.__queue = SinglyLinkedList()

    def enqueue(self, item):
        self.__queue.add_back(item)

    def dequeue(self):
        self.__queue.remove_front()
