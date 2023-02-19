
class NaryNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

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
        return f'<data={str(self.data)}>'

    __repr__ = __str__

