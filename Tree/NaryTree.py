from Tree.NaryNode import NaryNode


class NaryTree(object):

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._root

    def add(self, data, parent=None):
        new_node = NaryNode(data)
        if self._root is None:
            self._root = new_node
            return
        found_parent: NaryNode = self.find_node(key=parent)
        if not found_parent:
            raise KeyError
        found_parent.children.append(new_node)
        new_node.parent = found_parent

    def find_node(self, key):
        all_nodes = self.walk_bf()  # self.walk_df()
        for e in all_nodes:
            if e.data == key:
                return e
        return None

    # level wise traversal = breadth-first
    # non-recursive walk
    # must use queue
    def walk_bf(self):
        levelwise_walk = []
        if self._root is None:
            return levelwise_walk
        to_visit_queue = [self._root]  # one can use genuine queue
        while len(to_visit_queue) > 0:
            # removes the first element from the list (considered as queue)
            e: NaryNode = to_visit_queue.pop(0)
            to_visit_queue.extend(e.children)
            levelwise_walk.append(e)
        return levelwise_walk

    # depth first Order Traversal
    # non-recursive walk
    # must use stack
    def walk_df(self):
        df_walk = []
        if self._root is None:
            return df_walk
        to_visit_stack = [self._root] # push the root
        while len(to_visit_stack) > 0:
            # removes the last element from the list
            e: NaryNode = to_visit_stack.pop()
            to_visit_stack.extend(e.children)
            df_walk.append(e)
        return df_walk


def app_driver():
    gt = NaryTree()
    gt.add(data='Abraham')
    gt.add(data='Ishmael', parent='Abraham')
    gt.add(data='Isaak', parent='Abraham')
    gt.add(data='Jacob', parent='Isaak')
    gt.add(data='Joseph', parent='Jacob')
    gt.add(data='Zimran', parent='Abraham')

    print(gt.walk_bf())
    print(gt.walk_df())


app_driver()