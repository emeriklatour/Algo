class Node(object):
    def __init__(self, item: int, previous_node=None, next_node=None):
        self.item = item
        self.next = next_node
        self.previous = previous_node

    def __repr__(self):
        return repr(self.item)


class DoublyLinkedList(object):

    def __init__(self):
        self.__head = None
        self.__tail = self.__head

    def __len__(self):
        current = self.__head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter

    length = __len__

    def add_front(self, item):
        new_node = Node(item, None, self.__head)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
            return
        self.__head.previous = new_node
        self.__head = new_node

    def add_back(self, item):
        new_node = Node(item, self.__tail, None)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
            return
        self.__tail.next = new_node
        self.__tail = new_node

    def remove_at(self, index):
        if not 0 <= index < self.length():
            return IndexError('Provided index is out of bounds')
        if index == 0:
            self.__head = self.__head.next
            if self.__head is not None:
                self.__head.previous = None
            else:
                self.__tail = None
            return
        if index == self.length()-1:
            self.__tail = self.__tail.previous
            self.__tail.next = None
        current = self.__head
        rank = 0
        while rank != index:
            current = current.next
            rank += 1
        # remove current node
        current.previous.next = current.next
        current.next.previous = current.previous

    def __repr__(self):
        nodes = []
        current = self.__head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ', '.join(nodes) + ']'

