class LinkedBinaryTreeHelper(object):

    @classmethod
    def count_nodes(cls, bt):
        return cls.__count_number_of_nodes(bt.root())

    @classmethod
    def __count_number_of_nodes(cls, root):
        if root is None:
            return 0
        return 1 + cls.__count_number_of_nodes(root.left) + cls.__count_number_of_nodes(root.right)

    @classmethod
    def depth(cls, bt):
        return cls.__depth(bt.root())

    @classmethod
    def __depth(cls, root) -> int:
        if root is None:
            return 0
        left_depth = cls.__depth(root.left)
        right_depth = cls.__depth(root.right)
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    # In a full Binary tree every parent/internal
    # node has either two or no children.
    @classmethod
    def is_full(cls, bt):
        return cls.__is_full(bt.root())

    @classmethod
    def __is_full(cls, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is not None:
            return cls.__is_full(root.left) and \
                   cls.__is_full(root.right)
        return False

    # In a complete binary tree all the levels are completely filled
    # except possibly the lowest one, which is filled from the left.
    @classmethod
    def is_complete(cls, bt):
        return cls.__is_complete(root=bt.root(), nodes_count=cls.count_nodes(bt), index=0)

    @classmethod
    def __is_complete(cls, root, nodes_count, index) -> bool:
        if root is None:
            return True
        if index >= nodes_count:
            return False
        return cls.__is_complete(root.left, nodes_count, 2 * index + 1) \
               and cls.__is_complete(root.right, nodes_count, 2 * index + 2)

    # In a perfect binary tree every parent/internal node has exactly
    # two child nodes and all the leaf nodes are at the same level.
    # A perfect binary tree with n nodes has height log(n + 1) – 1 = Θ(ln(n))
    @classmethod
    def is_perfect(cls, bt):
        return cls.__is_perfect(root=bt.root(), depth=cls.depth(bt), level=0)

    @classmethod
    def __is_perfect(cls, root, depth, level) -> bool:
        if root is None:
            return True
        # Check the presence of trees
        if root.left is None and root.right is None:
            return level + 1 == cls.depth
        if root.left is None or root.right is None:
            return False
        return cls.__is_perfect(root.left, depth, level + 1) and cls.__is_perfect(root.right, depth, level + 1)

    @classmethod
    def leaf_count(cls, bt):
        return cls.__leaf_count(bt.root())

    @classmethod
    def __leaf_count(cls, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return cls.__leaf_count(root.left) \
                   + cls.__leaf_count(root.right)

# Examples of use are available within BinaryTree class
