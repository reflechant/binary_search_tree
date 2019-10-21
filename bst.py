from typing import Union, Tuple, Generic, TypeVar

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

    def __find(
        self, el: Union["Node", T], no_fail=False, find_parent=False
    ) -> Union["Node", None]:
        cur_node = self
        if isinstance(el, Node):
            if find_parent:
                eq = lambda n: n.left is el or n.right is el
            else:
                eq = lambda n: el is n
            lt = lambda n: el.val < n.val
            gt = lambda n: el.val > n.val
        else:
            if find_parent:
                eq = lambda n: el == n.right.val or el == n.left.val
            else:
                eq = lambda n: el == n.val
            lt = lambda n: el < n.val
            gt = lambda n: el > n.val
        while True:
            if eq(cur_node):
                return cur_node
            elif cur_node.left and lt(cur_node):
                cur_node = cur_node.left
            elif cur_node.right and gt(cur_node):
                cur_node = cur_node.right
            elif no_fail:
                return cur_node
            else:
                return None

    def find(self, val) -> Union["Node", None]:
        return self.__find(val)

    def find_nearest(self, val) -> "Node":
        return self.__find(val, no_fail=True)

    def find_parent(self, el: Union["Node", T]) -> "Node":
        return self.__find(el, find_parent=True)

    def remove(self, el: Union["Node", T]):
        p = self.__find(el, find_parent=True)
        if isinstance(el, Node):
            n = el
        else:
            n = p.left if p.left and p.left.val == el else p.right
        if n.left and n.right:
            pass
        elif n.left:
            pass
        elif n.right:
            pass
        else:
            pass

    def add(self, val: T) -> "Node":
        n = self.find_nearest(val)
        if val < n.val:
            n.left = Node(val)
        elif val > n.val:
            n.right = Node(val)
        return n

    def contains(self, val: T) -> bool:
        return True if self.__find(val) else False

    def is_valid_bst(self) -> bool:
        pass

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
