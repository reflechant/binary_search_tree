from typing import Union, Tuple, Generic, TypeVar
from itertools import tee
from operator import lt

T = TypeVar("T")


class Node(Generic[T]):
    """
    Binary search tree implementation. Duplicates not allowed. Keys are values.
    """

    def __eq__(self, n: "Node") -> bool:
        return all(map(lambda pair: pair[0] == pair[1], zip(self, n)))

    def __init__(self, key: T, left: "Node" = None, right: "Node" = None):
        self.key = key
        self.left: Node = left
        self.right: Node = right

    def find(self, key: T) -> Union["Node", None]:
        node = self
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            elif key == node.key:
                return node
        return None

    def __contains__(self, key: T) -> bool:
        if self.find(key):
            return True
        return False

    def __remove_node(self, node: "Node"):
        pass

    def remove(self, key: T):
        node = self
        while node:
            if key == node.key:
                # self.__remove_node(node)
                break
            elif key < node.key:
                node = node.left
            else:
                node = node.right

    def insert(self, key: T) -> "Node":
        node = self
        while node:
            if key == node.key:
                return None
            elif key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(key)
                    return node.left
            elif key > node.key:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(key)
                    return node.right

    def validate(self) -> bool:
        a, b = tee(self.__iter__())
        next(b, None)
        return all(lt(x, y) for x, y in zip(a, b))

    def __iter__(self):
        def f():
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

        return f()

    def __repr__(self):
        return " ".join(str(x) for x in iter(self))
