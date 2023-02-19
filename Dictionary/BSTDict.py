
from src.adt.dictionary.Entry import Entry


class Node(object):

    def __init__(self, key, value):
        self.left_child = None
        self.right_child = None
        self.entry = Entry(key, value)


class BSTDict(object):

    def __init__(self):
        self.root: Node = None

    def put(self, key, value):
        new_node = Node(key, value)
        if self.root is None:
            self.root = new_node
        else:
            self.attach(self.root, new_node)

    def attach(self, root, new_node):
        if root is not None:
            if root.entry.key <= new_node.entry.key:
                if root.left_child:
                    self.attach(root.left_child, new_node)
                else:
                    root.left_child = new_node
            elif root.entry.key > new_node.entry.key:
                if root.right_child:
                    self.attach(root.right_child, new_node)
                else:
                    root.right_child = new_node

    def get(self, key):
        node_found = self.find_node(self.root, key)
        if node_found:
            return node_found.entry.value
        print('Provided key not found...')
        return None

    def find_node(self, start, key):
        if start is None:
            return None
        if key == start.entry.key:
            return start
        if key >= start.entry.key and start.left_child:
            return self.find_node(start.left_child, key)
        else:
            return self.find_node(start.right_child, key)

    def remove(self, key):
        return self.remove_node(self.root, key).entry.value

    # loop down to find the leftmost leaf
    def find_left_most(self, root):
        if not root:
            return None
        leftmost = root
        while leftmost.left_child:
            leftmost = leftmost.left_child
        return leftmost

    def remove_node(self, sub_tree, key):
        if sub_tree is None:
            return None
        if key < sub_tree.entry.key:
            sub_tree.left_child = self.remove_node(sub_tree.left_child, key)
        elif key > sub_tree.entry.key:
            sub_tree.right_child = self.remove_node(sub_tree.right_child, key)
        else:
            if sub_tree.left_child is None:
                temp = sub_tree.right_child
                sub_tree = None
                return temp

            elif sub_tree.right_child is None:
                temp = sub_tree.left_child
                sub_tree = None
                return temp

            temp = self.find_left_most(sub_tree.right_child)
            sub_tree.entry.key = temp.entry.key
            sub_tree.right_child = self.remove_node(sub_tree.right_child, temp.entry.key)
        return sub_tree

    def show(self):
        print('Current BST status is: ')
        self.in_order(self.root)

    def in_order(self, start_node: Node):
        if start_node is not None:
            self.in_order(start_node.left_child)
            print('\t', start_node.entry.key, start_node.entry.value)
            self.in_order(start_node.right_child)


def test_bst_dict():
    dic = BSTDict();
    dic.put('Canada', 'Ottawa')
    dic.put('Turkey', 'Ankara')
    dic.put('Albania', 'Tirana')
    dic.show()

    print(dic.get('Albania'))

    print(dic.remove('Canada'))
    print(dic.remove('Turkey'))
    dic.show()

test_bst_dict()