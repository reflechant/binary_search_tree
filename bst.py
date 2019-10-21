from typing import Union, Tuple, Generic, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    """
    Binary search tree implementation. Duplicates not allowed. Keys are values.
    """

    def __eq__(self, n: 'Node') -> bool:
        return self.val == n.val and self.left is n.left and self.right is n.right

    def __init__(self, val: T, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left: Node = left
        self.right: Node = right

    def find_parent(self, n: 'Node') -> 'Node':
        """
        Returns parent node of n, considering self is tree root
        """
        cur_node = self
        while True:
            if cur_node.left is n or cur_node.right is n:
                return cur_node
            elif cur_node.left and n.val < cur_node.val:
                cur_node = cur_node.left
            elif cur_node.right and n.val > cur_node.val:
                cur_node = cur_node.right
            else:
                raise LookupError

    def __find(self, x: T, return_nearest=False) -> Union['Node', None]:
        cur_node = self
        while True:
            if x < cur_node.val and cur_node.left:
                cur_node = cur_node.left
            elif x > cur_node.val and cur_node.right:
                cur_node = cur_node.right
            elif x == cur_node.val or return_nearest:
                return cur_node
            else:
                return None

    def find(self, x) -> Union['Node', None]:
        return self.__find(x)

    def find_nearest(self, x) -> 'Node':
        return self.__find(x, return_nearest=True)

    def remove_value(self, x: T):
        n = self.find(x)
        if n:
            self.remove_node(n)

    def remove_node(self, n: 'Node'):
        p = self.find_parent(n)
        if n.left and n.right:
            pass
        elif n.left:
            pass
        elif n.right:
            pass
        else:
            pass

    def add(self, x: T) -> 'Node':
        n = self.find_nearest(x)
        if x < n.val:
            n.left = Node(x)
        elif x > n.val:
            n.right = Node(x)
        return n

    def contains(self, x: T) -> bool:
        return True if self.__find(x) else False

    def is_valid_bst(self) -> bool:
        pass

    def tuple(self) -> Tuple[T, tuple, tuple]:
        return self.val, self.left.tuple() if self.left else None, self.right.tuple() if self.right else None

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
