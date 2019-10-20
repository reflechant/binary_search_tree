from typing import Union, Tuple, Any


class Node:
    """
    Binary search tree implementation. Duplicates not allowed. Keys are values.
    """

    def __eq__(self, node: 'Node')->bool:
        return self.val == node.val and self.left is node.left and self.right is node.right

    def __init__(self, val, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left: Node = left
        self.right: Node = right

    def __del__(self) -> 'Node':
        pass

    def __find(self, x, return_nearest=False) -> Union['Node', None]:
        cur_node = self
        while True:
            if x < cur_node.val:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    if return_nearest:
                        return cur_node
                    else:
                        return None
            elif x > cur_node.val:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    if return_nearest:
                        return cur_node
                    else:
                        return None
            else:
                return cur_node

    def find(self, x) -> Union['Node', None]:
        return self.__find(x)

    def find_nearest(self, x) -> 'Node':
        return self.__find(x, return_nearest=True)

    def remove(self, x):
        pass

    def add(self, x) -> 'Node':
        node = self.find_nearest(x)
        if x < node.val:
            node.left = Node(x)
        elif x > node.val:
            node.right = Node(x)
        return node

    def contains(self, x) -> bool:
        return True if self.__find(x) else False

    def is_valid_bst(self) -> bool:
        pass

    def tuple(self) -> Tuple[Any, tuple, tuple]:
        return (self.val, self.left.tuple() if self.left else None, self.right.tuple() if self.right else None)

    def __iter__(self):
        def f():
            if self.left:
                yield from self.left
            yield self.val
            if self.right:
                yield from self.right
        return f()

    def __repr__(self):
        return "-".join(str(x) for x in iter(self))


if __name__ == "__main__":
    node = Node(1)
    print(node)
    node.add(1)
    print(node)
    node.add(2)
    print(node)
    node.add(0)
    print(node)
