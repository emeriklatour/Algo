from src.adt.queue.DHSLLBasedQueue import Queue as LinkedQueue
from src.adt.queue.ArrayQueue import Queue as ArrayQueue


class StackUsing2Queues(object):

    def __init__(self):
        self.main_queue = LinkedQueue()
        self.swap_queue = ArrayQueue()

    def push(self, item):
        # print(str(self.inbox_queue.is_empty()))
        # move all elements in inbox to outbox
        # Swap-out of all items
        while not self.main_queue.is_empty():
            self.swap_queue.enqueue(self.main_queue.dequeue())

        # add the last pushed item in the first position in the queue
        self.main_queue.enqueue(item)

        # Swap-in elements
        # move all elements back to inbox from outbox
        while not self.swap_queue.is_empty():
            self.main_queue.enqueue(self.swap_queue.dequeue())

        print(f'\nStatus of the stack after pushing item {item} ')
        print(f'Main-Queue: {str(self.main_queue)}')
        print(f'Swap-Queue: {str(self.swap_queue)}')

    def pop(self):
        # if inbox queue is empty
        if not self.main_queue:
            print("Stack Underflow...")
        # return the front item from the inbox
        return self.main_queue.dequeue()

    def top(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass


def test_stack_using_2_queues():
    stack = StackUsing2Queues()
    print('Testing stack_using_2_queues behavior...')
    stack = StackUsing2Queues()
    stack.push(1)
    stack.push(2)

    print(f'Popped item is: {stack.pop()}')
    stack.push(3)

    print(f'Popped item is: {stack.pop()}')
    print(f'Popped item is: {stack.pop()}')


test_stack_using_2_queues()
