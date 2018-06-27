'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the
tree into a string, and deserialize(s), which deserializes the string back into
the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node(object):
    '''
    Args:
        val(any)
        left(Node)
        right(Node)
    '''
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(tree_node):
    '''
    Use -1 to represent an empty leaf. Use ' ' to sperate different nodes.

    Args:
        tree_root(class Node): the root of the tree

    Returns:
        string: a serialized tree
    '''
    preorder_list = preorder_trav(tree_node)
    return ' '.join(str(x) for x in preorder_list)


def preorder_trav(node):
    '''
    Args:
        node(class Node): a node on which the traverse starts

    Returns:
        list: pre-order traverse
    '''
    tree_list = []
    if node is not None:
        tree_list.append(node.val)
        tree_list.extend(preorder_trav(node.left))
        tree_list.extend(preorder_trav(node.right))

    if node is None:
        tree_list.append('-1')
    return tree_list


def deserialize(tree_string):
    '''
    Args:
        tree_string(string): a serialized tree representation

    Returns:
        class Node: the root of a tree
    '''
    tree_list = tree_string.split(' ')
    tree = rebuild(tree_list)
    return tree


def rebuild(tree_list):
    '''
    Args:
        tree_list: a list of all nodes in a tree

    Returns:
        class Node: the root of a tree
    '''
    if len(tree_list) != 0:     # use == to compare value, 'is' to compare objects
        value = tree_list.pop(0)
        if value != '-1':       # use == or != to compare two strings
            node = Node(value)
            node.left = rebuild(tree_list)
            node.right = rebuild(tree_list)
        else:
            node = Node(None)
    return node


def main():
    '''
    unit test
    '''
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    # node = Node('root')
    print serialize(node)
    print deserialize(serialize(node)).val
    print deserialize(serialize(node)).left.val
    print deserialize(serialize(node)).left.left.val
    print deserialize(serialize(node)).right.val


if __name__ == '__main__':
    main()
