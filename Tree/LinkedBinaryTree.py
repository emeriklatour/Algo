from Tree.BinaryNode import BinaryNode
from Tree.LinkedBinaryTreeHelper import LinkedBinaryTreeHelper
from Tree.BinaryTreeWalker import BinaryTreeWalker


class LinkedBinaryTree(object):


    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._root

    def add(self, data):
        new_node = BinaryNode(data)
        self._size += 1
        if self._root is None:
            self._root = new_node
            return
        self.__attach(self._root, new_node)

    def __attach(self, root, new_node):
        if root is not None:
            if root.data > new_node.data:
                if root.left:
                    self.__attach(root.left, new_node)
                else:
                    root.left = new_node
            elif root.data <= new_node.data:
                if root.right:
                    self.__attach(root.right, new_node)
                else:
                    root.right = new_node

    def remove(self, key):
        pass

    def root(self):
        return self._root


def app_driver():
    bst = LinkedBinaryTree()
    bst.add(1)
    bst.add(2)
    bst.add(3)
    bst.add(4)
    bst.add(5)
    # bst.put(4)
    # bst.put(6)

    print(BinaryTreeWalker.pre_order(bst))
    print(BinaryTreeWalker.in_order(bst))
    print(BinaryTreeWalker.post_order(bst))

    print(f'Nodes count is: {LinkedBinaryTreeHelper.count_nodes(bst)}')
    print(f'The dept of the tree is: {LinkedBinaryTreeHelper.depth(bst)}')
    print(f'Number of leaves is {LinkedBinaryTreeHelper.leaf_count(bst)}')

    print(f'Is the tree full?: {LinkedBinaryTreeHelper.is_full(bst)}')
    print(f'Is the tree perfect?: {LinkedBinaryTreeHelper.is_perfect(bst)}')
    print(f'Is the tree complete?: {LinkedBinaryTreeHelper.is_complete(bst)}')


app_driver()
