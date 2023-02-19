from src.adt.list.DoublyLinkedCircularList import DoublyLinkedCircularList


class DLCLBasedStack(object):

    def __init__(self):
        self.__stack = DoublyLinkedCircularList()

    def push(self, item):
        # print(f'PUSH a new item {item}')
        # self.__stack.add_front(item)
        self.__stack.add_back(item)

    def pop(self):
        # print('POP last item')
        # self.__stack.remove_front(item)
        return self.__stack.remove_back()

    def top(self):
        # In case of front: self.__stack.get_head()
        self.__stack.get_tail()

    def is_empty(self):
        return self.__stack.is_empty()

    def size(self):
        return self.__stack.length()

    def __repr__(self):
        return self.__stack.__repr__()


def test_linked_stack():
    print('Testing stack behavior...')
    dlcl_stack = DLCLBasedStack()
    dlcl_stack.push(1)
    dlcl_stack.push(2)
    print(f'Stack= {dlcl_stack}')
    print(f'Popped item is: {dlcl_stack.pop()}')
    print(f'Stack= {dlcl_stack}')
    dlcl_stack.push(3)
    print(f'Stack= {dlcl_stack}')
    print(f'Popped item is: {dlcl_stack.pop()}')
    print(f'Popped item is: {dlcl_stack.pop()}')
    print(f'Stack= {dlcl_stack}')


# test_linked_stack()
