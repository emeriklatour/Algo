
class Node(object):
    def __init__(self, item: int, next_node=None):
        self.item = item
        self.next = next_node

    def __repr__(self):
        return repr(self.item)


# DoubleHeadedSinglyLinkedList (DHSLL) Based Queue
class Queue(object):
    def __init__(self):
        self.__head = None
        self.__tail = self.__head
        self.__current_size = 0

    def __len__(self):
        return self.__current_size

    length = __len__

    def add_front(self, item):
        new_node = Node(item, self.__head)
        self.__current_size += 1
        if self.__head is None:
            self.__tail = new_node
        self.__head = new_node

    def add_back(self, item):
        new_node = Node(item, None)
        self.__current_size += 1
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
            return
        self.__tail.next = new_node
        self.__tail = new_node

    def enqueue(self, item):
        self.add_back(item)

    def get_node_previous_to_tail_node(self) -> Node:
        current = self.__head
        while current.next != self.__tail:
            current = current.next
        return current

    def remove_back(self):
        if self.__head is None:
            print('Queue is empty')
            return None

        self.__current_size -= 1
        if self.__head == self.__tail:
            to_return = self.__head.item
            self.__head = self.__tail = None
            return to_return
        # General case
        previous_tail = self.get_node_previous_to_tail_node()
        to_return = self.__tail.item
        self.__tail = previous_tail
        self.__tail.next = None
        return to_return

    def remove_front(self):
        if self.__head is None:
            print('Queue is empty')
            return None

        self.__current_size -= 1
        if self.__head == self.__tail:
            to_return = self.__head.item
            self.__head = self.__tail = None
            return to_return
        # General case
        to_return = self.__head.item
        self.__head = self.__head.next
        return to_return

    def dequeue(self):
        return self.remove_front()

    def peek(self):
        if self.__head:
            return self.__head.item
        return None

    def __repr__(self):
        nodes = []
        current = self.__head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ', '.join(nodes) + ']'


queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
print(queue.length())

queue.dequeue()
print(queue)

queue.dequeue()
print(queue)

queue.dequeue()
print(queue)
print(queue.peek())
print(queue.length())
queue.enqueue(9)
print(queue)
queue.remove_back()
print(queue)