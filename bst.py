from typing import Union, Tuple, Generic, TypeVar
from itertools import tee
from operator import lt

T = TypeVar("T")


class Node(Generic[T]):
    """
    Binary search tree implementation. Duplicates not allowed. Keys are values.
    """

    def __eq__(self, n: "Node") -> bool:
        return self.val == n.val and self.left is n.left and self.right is n.right

    def __init__(self, val: T, left: "Node" = None, right: "Node" = None):
        self.val = val
        self.left: Node = left
        self.right: Node = right

    def __find_parent_of_node(self, n: "Node") -> "Node":
        """
        Returns parent node of node n, considering self is tree root
        """
        node = self
        while True:
            if node.left is n or node.right is n:
                return node
            if node.left and n.val < node.val:
                node = node.left
            if node.right and n.val > node.val:
                node = node.right
            if not node.left and not node.right:
                return None

    def __find_parent_of_value(self, x: T) -> "Node":
        """
        Returns parent node of value x, considering self is tree root
        """
        node = self
        while True:
            if node.left:
                if x == node.left.val:
                    return node
                elif x < node.left.val:
                    node = node.left
            if node.right:
                if x == node.right.val:
                    return node
                elif x > node.right.val:
                    node = node.right
            if not node.left and not node.right:
                return None

    def __find(self, x: T, no_fail=False) -> Union["Node", None]:
        node = self
        while True:
            if x < node.val and node.left:
                node = node.left
            elif x > node.val and node.right:
                node = node.right
            elif x == node.val or no_fail:
                return node
            else:
                return None

    def find(self, x) -> Union["Node", None]:
        return self.__find(x)

    def find_nearest(self, x) -> "Node":
        return self.__find(x, no_fail=True)

    def find_parent(self, el: Union["Node", T]):
        if isinstance(el, Node):
            return self.__find_parent_of_node(el)
        else:
            return self.__find_parent_of_value(el)

    def __remove_value(self, x: T):
        p = self.__find_parent_of_value(x)
        if not p:
            return
        if x < p.val:
            self.__remove_node(p.left)
        else:
            self.__remove_node(p.right)

    def __remove_node(self, n: "Node"):
        p = self.__find_parent_of_node(n)
        if not p:
            return
        if n.left and n.right:
            pass
        elif n.left:
            pass
        elif n.right:
            pass
        else:
            if p.left is n:
                p.left = None
            else:
                p.right = None

    def remove(self, el: Union["Node", T]):
        if isinstance(el, Node):
            self.__remove_node(el)
        else:
            self.__remove_value(el)

    def add(self, x: T) -> "Node":
        n = self.find_nearest(x)
        if x < n.val:
            n.left = Node(x)
        elif x > n.val:
            n.right = Node(x)
        return n

    def contains(self, x: T) -> bool:
        return True if self.__find(x) else False

    def is_valid_bst(self) -> bool:
        a, b = tee(self.__iter__())
        next(b, None)
        return all(lt(x, y) for x, y in zip(a, b))

    def tuple(self) -> Tuple[T, tuple, tuple]:
        return (
            self.val,
            self.left.tuple() if self.left else None,
            self.right.tuple() if self.right else None,
        )

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
