
class BinaryNode:

    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data

    def __lt__(self, other):
        return self.data < other.data

    def __le__(self, other):
        return self.data <= other.data

    def __str__(self):
        return f'<data={str(self.data)}, left= {str(self.left)}, ' \
               f'right={str(self.right)}'

    __repr__ = __str__
