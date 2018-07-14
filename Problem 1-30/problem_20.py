'''
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting
node. The lists are non-cyclical.

For example, given A = 1 - > 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and
constant space.
'''
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def add_node(self, node=None):
        self.next = node
        return node


def find_intersection(A, B):
    '''
    Find intersection of two singly list
    Args:
        A(Node)
        B(Node)
    Returns:
        Node: intersection node
    '''
    while A.val != B.val:
        # if A runs to the end first, connect to B, and vice versa
        A = B if A.next == None else A.next
        B = A if B.next == None else B.next
    return A


def main():
    A = Node(1)
    B = Node(99)
    A.add_node(Node(3)).add_node(Node(7)).add_node(Node(8)).add_node(Node(10))
    B.add_node(Node(99)).add_node(Node(1)).add_node(Node(8)).add_node(Node(10))
    print find_intersection(A, B).val


if __name__ == '__main__':
    main()
