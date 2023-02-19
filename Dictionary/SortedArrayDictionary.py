from src.adt.wn.SortedArrayList import SortedArrayList


class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key


class SortedArrayDictionary:
    def __init__(self):
        self.__entries = SortedArrayList()

    def size(self):
        return len(self.__entries)

    def is_empty(self):
        return self.size() <= 0

    def get(self, key):
        entry = self.__entries[MapEntry(key, None)]
        if entry is None:
            return None
        return entry.value

    def put(self, key, value):
        self.__entries.add(MapEntry(key, value))

    def remove(self, key):
        self.__entries.remove(MapEntry(key, None))

    def key_set(self):
        keys = []
        for entry in self.__entries:
            keys.append(entry.key)
        return keys

    def values(self):
        values = []
        for entry in self.__entries:
            values.append(entry.value)
        return values

    def entry_set(self):
        return self.__entries

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.size()

    def __str__(self):
        value = f"size: {self.size()}, values: ["
        for index, entry in enumerate(self.__entries):
            value += f"{entry.key}: {entry.value}"
            if index < self.size() - 1:
                value += ", "
        value += "]"
        return value


def test_array_map():
    sorted_dict = SortedArrayDictionary()
    sorted_dict.put("word", 8)
    sorted_dict.put("array", 3)
    sorted_dict.put("hash", 6)
    sorted_dict.put("dictionary", 2)
    sorted_dict.put("map", 4)
    print(sorted_dict)

    print("hash: " + str(sorted_dict["hash"]))
    print("asdf: " + str(sorted_dict["asdf"]))

    sorted_dict.remove("hash")
    print(sorted_dict)


test_array_map()
