from bst import Node


def test_init():
    root = Node(0)
    assert isinstance(root, Node)
    assert root.val == 0
    assert root.left is None
    assert root.right is None


def test_node_to_tuple():
    assert Node(0).tuple() == (0, None, None)
    assert Node(1, Node(0)).tuple() == (1, (0, None, None), None)
    assert Node(1, None, Node(2)).tuple() == (1, None, (2, None, None))
    assert Node(1, Node(0), Node(2)).tuple() == (1, (0, None, None), (2, None, None))


def test_node_repr():
    assert str(Node(0)) == "0"
    assert str(Node(1, Node(0), Node(2))) == "0-1-2"


def test_add_duplicate():
    root = Node(1)
    root.add(1)
    assert root == Node(1)


def test_add_left():
    root = Node(1)
    root.add(0)
    assert root.tuple() == (1, (0, None, None), None)


def test_add_right():
    root = Node(1)
    root.add(2)
    assert root.tuple() == Node(1, None, Node(2)).tuple()


def test_contains():
    root = Node(1)
    root.add(2)
    root.add(3)
    assert root.contains(0) == False
    assert root.contains(1) == True
    assert root.contains(3) == True


def test_find():
    root = Node(1)
    root.add(2)
    root.add(-5)
    assert root.find(1) is root
    assert root.find(100) is None
    assert root.find(2) is root.right
    assert root.find(-5) is root.left


def test_find_nearest():
    root = Node(5)
    assert root.__find_nearest(1) is root
    assert root.__find_nearest(100) is root


def test_find_parent():
    root = Node(5)
    assert root.find_parent(5) is None
    root.add(2)
    root.add(7)
    assert root.find_parent(root.left) is root
    assert root.find_parent(root.right) is root
    assert root.find_parent(2) is root
    assert root.find_parent(7) is root


def test_remove_value():
    root = Node(1, Node(0), Node(2))
    root.remove(0)
    assert root.tuple() == (1, None, (2, None, None))


def test_remove_node():
    root = Node(1)
    root.add(2)
    n = root.add(3)
    root.remove(n)
    assert root.tuple() == (1, None, (2, None, None))


def test_valid_bst():
    root = Node(1, Node(2))
    assert not root.is_valid_bst()
    root = Node(1, Node(0))
    assert root.is_valid_bst()
    root = Node(1, None, Node(0))
    assert not root.is_valid_bst()
    root = Node(1, None, Node(2))
    assert root.is_valid_bst()
    root = Node(1, Node(0), Node(2))
    assert root.is_valid_bst()
