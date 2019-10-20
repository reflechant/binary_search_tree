from bst import Node


def test_init():
    node = Node(0)
    assert isinstance(node, Node)
    assert node.val == 0
    assert node.left == None
    assert node.right == None


def test_node_to_tuple():
    assert Node(0).tuple() == (0, None, None)
    assert Node(1,
                Node(0)).tuple() == (1,
                                     (0, None, None),
                                     None)
    assert Node(1,
                None,
                Node(2)).tuple() == (1,
                                     None,
                                     (2, None, None))
    assert Node(1,
                Node(0),
                Node(2)).tuple() == (1,
                                     (0, None, None),
                                     (2, None, None))


def test_node_repr():
    assert str(Node(0)) == "0"
    assert str(Node(1, Node(0), Node(2))) == "0-1-2"


def test_add_duplicate():
    node = Node(1)
    node.add(1)
    assert node == Node(1)


def test_add_left():
    node = Node(1)
    node.add(0)
    assert node.tuple() == (1, (0, None, None), None)


def test_add_right():
    node = Node(1)
    node.add(2)
    assert node.tuple() == Node(1, None, Node(2)).tuple()


def test_find():
    node = Node(1).add(2).add(3).add(-5).add(7)
    assert node
