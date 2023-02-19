from Tree.LinkedBinaryTreeHelper import LinkedBinaryTreeHelper


class ArrayBasedBinaryTree(object):

    def __init__(self):
        self._data = []
        self._size = 0

    def root(self):
        if self._data[1] is not None:
            return 1

    def initialize(self, data, size):
        self._data = data
        self._size = size

    def right_child(self, parent_index):
        if self._data[parent_index] is not None:
            return (2 * parent_index) + 1
        return - 1

    def left_child(self, parent_index):
        if self._data[parent_index] is not None:
            return 2 * parent_index
        return - 1

    def get_parent(self, child_index):
        if self._data[child_index] is not None and child_index / 2 is not None:
            return child_index // 2
        return -1

    def preorder(self):
        visited_items = []
        self.__preorder(index=1, visited=visited_items)
        return visited_items

    def __preorder(self, index, visited):
        if index > self._size:
            return
        if index > 0 and self._data[index] is not None:
            visited.append(self._data[index])
            self.__preorder(self.left_child(index), visited)
            self.__preorder(self.right_child(index), visited)


def app_driver():
    bt = ArrayBasedBinaryTree()
    tree = [None, 'D', 'A', 'F', 'E', 'B', 'R', 'T', 'G', 'Q', None, None, 'V', None, 'J', 'L']
    bt.initialize(tree, 15)
    print(bt.preorder())

    print(f'Nodes count is: {LinkedBinaryTreeHelper.count_nodes(bt)}')
    print(f'The dept of the tree is: {LinkedBinaryTreeHelper.depth(bt)}')
    print(f'Number of leaves is {LinkedBinaryTreeHelper.leaf_count(bt)}')

app_driver()
