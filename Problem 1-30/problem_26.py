'''
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''
class Node(object):
    def __init__(self, val=None, next_n=None):
        self.val = val
        self.next = next_n

    def __str__(self):
        values = []
        while self:
            values.append(str(self.val))
            self = self.next
        return ' -> '.join(values)

    def add_node(self, node):
        self.next = node
        return node


def remove_k_last_elem(head, k):
    '''
    Use two pointers trick to access the kth last elem in one pass
    Args:
        head(Node): head of the linked list
        k(int)
    Returns:
        Node: head of the new linked list
    '''
    slow = fast = head
    for _ in xrange(k):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head


def main():
    curr = head = Node(0)
    for i in xrange(1, 10):
        new_node = Node(i)
        curr = curr.add_node(new_node)

    print head
    remove_k_last_elem(head, 4)
    print head


if __name__ == '__main__':
    main()
