
class Vertex(object):

    def __init__(self, label, data):
        self.key = label
        self.data = data
        # self.__neighbors = {}

    @property
    def label(self):
        return self.key

    def hash(self):
        return hash(self.__key)  # hash(id(self))

    def __str__(self):
        return f'[{str(self.key)},{str(self.data)}]'

    def __repr__(self):
        return self.__str__()

