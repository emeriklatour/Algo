from src.adt.stack.ArrayStack import ArrayStack
from src.adt.stack.LinkedStack import DLCLBasedStack


class QueueUsing2Stacks(object):

    def __init__(self):
        self.array_stack = ArrayStack()
        self.linked_stack = DLCLBasedStack()

    def enqueue(self, item):
        self.array_stack.push(item)

    def dequeue(self):
        if self.linked_stack.is_empty():
            if self.array_stack.is_empty():
                raise IndexError("Can't dequeue from empty queue!")
            while not self.array_stack.is_empty():
                item = self.array_stack.pop()
                self.linked_stack.push(item)
        self.linked_stack.pop()

    def __repr__(self):
        to_return = 'Array-stack  ' + str(self.array_stack)
        to_return = to_return + '\nLinked-stack ' + str(self.linked_stack)
        return to_return


def test_queue_using_2stacks():
    queue = QueueUsing2Stacks()
    queue.enqueue(1)
    queue.enqueue(2)
    print(f'-----Queue content after pushing 1 & 2 : -----\n{queue}')
    queue.dequeue()
    print(f'-----Queue content after poping 2 : -----\n{queue}')
    queue.enqueue(3)
    print(f'-----Queue content after pushing 3 : -----\n{queue}')
    queue.dequeue()
    print(f'-----Queue content after poping last element : -----\n{queue}')
    queue.dequeue()
    print(f'-----Queue content after poping last element : -----\n{queue}')


test_queue_using_2stacks()
