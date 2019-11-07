from typing import Union, Tuple, Generic, TypeVar
from itertools import tee
from operator import lt

T = TypeVar("T")


class Node(Generic[T]):
    """
    Binary search tree implementation. Duplicates not allowed. Keys are values.
    """

    def __eq__(self, n: "Node") -> bool:
        return all(a.key == b.key for a, b in zip(self, n))

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
            else:
                return node
        return None

    def __contains__(self, key: T) -> bool:
        if self.find(key):
            return True
        return False

    def remove(self, key: T):
        node = self
        parent = None
        while node:
            if key == node.key:
                if node.left and node.right:
                    successor = next(node.right.__iter__())
                    self.key = successor.key
                    self.right.remove(successor.key)
                elif node.left:
                    if parent.right is node:
                        parent.right = node.left
                    elif parent.left is node:
                        parent.left = node.left
                elif node.right:
                    if parent.right is node:
                        parent.right = node.right
                    elif parent.left is node:
                        parent.left = node.right
                else:
                    if parent.right is node:
                        parent.right = None
                    elif parent.left is node:
                        parent.left = None
                break
            elif key < node.key:
                parent = node
                node = node.left
            else:
                parent = node
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
        a, b = tee(self)
        next(b, None)
        return all(lt(x.key, y.key) for x, y in zip(a, b))

    def __iter__(self):
        def f():
            if self.left:
                yield from self.left
            yield self
            if self.right:
                yield from self.right

        return f()

    def tuple(self):
        return (
            self.left.tuple() if self.left else None,
            self.key,
            self.right.tuple() if self.right else None,
        )

    def __repr__(self):
        return " ".join(str(x.key) for x in iter(self))
