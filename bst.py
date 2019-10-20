class Node:
    """
    Binary search tree implementation. Duplicates not allowed. Keys are values.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Node = left
        self.right: Node = right

    def __del__(self):
        pass

    def remove(self, x):
        pass

    def add(self, x):
        cur_node = self
        while True:
            if x < cur_node.val:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = Node(x)
                    break
            elif x > cur_node.val:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(x)
                    break
            else:
                break

    def contains(self, x):
        pass

    def is_valid_bst(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __repr__(self):
        pass
