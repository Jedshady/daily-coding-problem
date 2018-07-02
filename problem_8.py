'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 '''
class Node(object):
    '''
    Tree Node
    If the tree rooted at this node is a unival tree, then 'is_unival' == True
    '''
    def __init__(self, val=None, left=None, right=None, is_unival=False):
        self.val = val
        self.left = left
        self.right = right
        self.is_unival = is_unival


def count_unival_subtree(node):
    '''
    Args:
        node(Node): The root node of a sub-tree

    Returns:
        int
    '''
    if node.left == node.right == None:
        node.is_unival = True
        return 1

    left = 0
    right = 0
    if node.left != None:
        left = count_unival_subtree(node.left)
    if node.right != None:
        right = count_unival_subtree(node.right)

    if node.left and node.right:    # node has both left and right
        if (node.left.is_unival and node.right.is_unival
            and node.val == node.left.val == node.right.val):
            node.is_unival = True
            return left + right + 1
        else:
            return left + right
    else:   # either left or right is missing
        if ((not node.left and node.val == node.right.val and node.right.is_unival)
            or (not node.right and node.val == node.left.val and node.left.is_unival)):
            node.is_unival = True
            return left + right + 1
        else:
            return left + right


def main():
    root = Node('0', Node('1'), Node('0', Node('1', Node('1'), Node('1')), Node('0')))
    print count_unival_subtree(root)


if __name__ == '__main__':
    main()
