
# Bucket / Slot

class Entry(object):

    def __init__(self, key, value, provided_hash=None):
        self.key = key
        self.value = value
        self.hash = provided_hash  # hash = f(key) = index  modulo of  capacity

    def __eq__(self, other):
        # compare items based on their keys
        return self.key == other.key

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        # compare items based on their keys
        return self.key < other.key

    def __str__(self):
        return "<Entry: key={0} value={1}>"\
            .format(self.key, self.value)

    def __repr__(self):
        return self.__str__()
