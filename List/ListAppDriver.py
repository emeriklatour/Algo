from List.ArrayList import ArrayList
from List.DoublyLinkedList import DoublyLinkedList
from List.SinglyLinkedList import SinglyLinkedList


class ListAppDriver(object):

    def test_array_list(self):
        print('test array list: ')
        al = ArrayList(100)
        al.add_back(5)
        al.add_back(9)
        print(al)

        al.add_front(6)
        print(al)

        al.insert_at(8, 2)
        print(al)

    def test_singly_linked_list(self):
        print('test linked list: ')
        sll = SinglyLinkedList()
        sll.add_back(7)
        sll.add_back(5)
        sll.add_back(9)
        print(sll)
        print(f'length of list is {sll.length()}')

        sll.add_front(1)
        sll.add_front(8)
        sll.add_front(6)
        print(sll)
        print(f'length of list is {sll.length()}')

        item = 9
        print(f'Position of item {item} is {sll.find(item)}')

        index = 1
        print(f'Removing item at position {index}')
        print(sll.remove_at(index))
        print(sll)
        print(f'length of list is {sll.length()}')

        sll.reverse()
        print(f'Reversed list is : ')
        print(sll)

    def test_doubly_linked_list(self):
        print('test linked list: ')
        dll = DoublyLinkedList()
        dll.add_back(7)
        dll.add_back(5)
        dll.add_back(9)
        print(dll)
        print(f'length of list is {dll.length()}')

        dll.add_front(1)
        dll.add_front(8)
        dll.add_front(6)
        print(dll)
        print(f'length of list is {dll.length()}')

        # item = 9
        # print(f'Position of item {item} is {dll.find(item)}')

        index = 4
        print(f'Removing item at position {index}')
        dll.remove_at(index)
        print(dll)
        print(f'length of list is {dll.length()}')

        # dll.reverse()
        # print(f'Reversed list is : ')
        #  print(dll)

    @staticmethod
    def main():
        app_driver = ListAppDriver()
        # app_driver.test_array_list()
        # app_driver.test_singly_linked_list()
        app_driver.test_doubly_linked_list()


print("List App Driver ...")
ListAppDriver.main()
