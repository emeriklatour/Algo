
class BinaryTreeWalker(object):

    @classmethod
    def pre_order(cls, bt):
        visited = []
        cls.__pre_order(bt.root(), visited)
        return visited

    @classmethod
    def __pre_order(self, root, visited):
        visited.append(root.data)
        if root.left:
            self.__pre_order(root.left, visited)
        if root.right:
            self.__pre_order(root.right, visited)

    @classmethod
    def in_order(cls, bt):
        visited = []
        cls.__in_order(bt.root(), visited)
        return visited

    @classmethod
    def __in_order(self, root, visited):
        if root.left:
            self.__in_order(root.left, visited)
        visited.append(root.data)
        if root.right:
            self.__in_order(root.right, visited)

    @classmethod
    def post_order(cls, bt):
        visited = []
        cls.__post_order(bt.root(), visited)
        return visited

    @classmethod
    def __post_order(self, root, visited):
        if root.left:
            self.__post_order(root.left, visited)
        if root.right:
            self.__post_order(root.right, visited)
        visited.append(root.data)

