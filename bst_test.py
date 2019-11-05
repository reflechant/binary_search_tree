from bst import Node


def test_init():
    root = Node(0)
    assert isinstance(root, Node)
    assert root.key == 0
    assert root.left is None
    assert root.right is None


def test_node_repr():
    assert str(Node(0)) == "0"
    assert str(Node(1, Node(0), Node(2))) == "0 1 2"


def test_insert_duplicate():
    root = Node(1)
    root.insert(1)
    assert root == Node(1)


def test_insert_left():
    root = Node(1)
    root.insert(0)
    assert str(root) == "0 1"


def test_insert_right():
    root = Node(1)
    root.insert(2)
    assert str(root) == "1 2"


def test_in():
    root = Node(1)
    root.insert(2)
    root.insert(3)
    assert (0 in root) == False
    assert (1 in root) == True
    assert (3 in root) == True


def test_find():
    root = Node(1)
    root.insert(2)
    root.insert(-5)
    assert root.find(1) is root
    assert root.find(100) is None
    assert root.find(2) is root.right
    assert root.find(-5) is root.left


def test_remove():
    root = Node(1, Node(0), Node(2))
    root.remove(0)
    assert str(root) == "1 2"


def test_validate():
    root = Node(1, Node(2))
    assert not root.validate()
    root = Node(1, Node(0))
    assert root.validate()
    root = Node(1, None, Node(0))
    assert not root.validate()
    root = Node(1, None, Node(2))
    assert root.validate()
    root = Node(1, Node(0), Node(2))
    assert root.validate()
