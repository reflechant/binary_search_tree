from bst import Node


def test_init():
    node = Node(0)
    assert isinstance(node, Node)
    assert node.val == 0
    assert node.left == None
    assert node.right == None


def test_add_duplicate():
    node = Node(1)
    node.add(node.val)
    assert node.val == 1
    assert node.left == None
    assert node.right == None


def test_add_left():
    node = Node(1)
    node.add(0)
    assert node.val == 1
    assert node.right == None
    assert node.left.val == 0
    assert node.left.right == None
    assert node.left.left == None


def test_add_right():
    node = Node(1)
    node.add(2)
    assert node.val == 1
    assert node.left == None
    assert node.right.val == 2
    assert node.right.right == None
    assert node.right.left == None
