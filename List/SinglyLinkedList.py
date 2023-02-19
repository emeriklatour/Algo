class Node(object):
    def __init__(self, item: int, next_node=None):
        self.item = item
        self.next = next_node

    def __repr__(self):
        return repr(self.item)


class SinglyLinkedList(object):

    def __init__(self):
        self.__head = None
        # self.__tail = None

    def __len__(self):
        current = self.__head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter

    length = __len__

    def add_front(self, item):
        # new_node = Node(item)
        # if self.__head is None:
        #    self.__head = new_node
        #    return
        # new_node.next = self.__head
        # self.__head = new_node
        self.__head = Node(item, self.__head)

    def add_back(self, item):
        if self.__head is None:
            self.__head = Node(item)
            return
        current = self.__head
        while current.next is not None:
            current = current.next
        current.next = Node(item)

    # find rank of given key= item
    def find(self, key) -> int:
        current = self.__head
        counter = 0
        while not (current is None or current.item == key):
            current = current.next
            counter += 1
        if current is None:
            return -1
        return counter

    def remove_at(self, index):
        if not 0 <= index < self.length():
            return IndexError('Provided index is out of bounds')

        current = self.__head
        previous = None
        rank = 0
        while current and rank != index:
            rank += 1
            previous = current
            current = current.next

        # Unlink it from the list
        if previous is None:
            self.__head = current.next
        elif current:
            previous.next = current.next
            current.next = None
        return 'Item removed...'

    def reverse(self):
        current = self.__head
        previous_node = None
        next_node = None
        while current:
            next_node = current.next
            current.next = previous_node
            previous_node = current
            current = next_node
        self.__head = previous_node

    def __repr__(self):
        nodes = []
        current = self.__head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ', '.join(nodes) + ']'
