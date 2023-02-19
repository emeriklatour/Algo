import bisect


class Sortedlist(object):

    def __init__(self, data):
        self.items = data
        self.sort()

    def sort(self):
        new_items = []
        for i in range(len(self.items)):
            # Insert item at position i in self.items in sorted order.
            bisect.insort(new_items, self.items[i])
        self.items = new_items

    def add(self, value):
        bisect.insort(self.items, value)

    def show(self):
        print(self.items)

    def find(self, value):
        # Locate the insertion point for value in self.items to maintain sorted order.
        # If value is already present in self.items, the insertion point will be before
        # (to the left of) any existing entries.
        left = bisect.bisect_left(self.items, value)
        if abs(self.items[min([left, self.length-1])] - value) >= abs(self.items[left-1] - value):
            return self.items[left-1]
        else:
            return self.items[left]

    def length(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)


def test():
    unsorted_data = [101, 3, 10, 14, 23, 86, 44, 45, 45, 50, 66, 95, 17, 77, 79, 84, 85, 91, 73]
    sorted_data = Sortedlist(unsorted_data)
    print(f'Size of sorted data is: {len(sorted_data)}')
    sorted_data.show()

    print(f'Adding new item: 99')
    sorted_data.add(99)
    print(f'Size of sorted data is: {len(sorted_data)}')
    sorted_data.show()

    print (f' Key {sorted_data.find(0)} not found')
    print (sorted_data.find(0))



test()