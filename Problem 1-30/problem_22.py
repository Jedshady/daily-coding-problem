'''
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].
'''
'''
Note:   Wordbreak from Leetcode
https://www.programcreek.com/2012/12/leetcode-solution-word-break/
https://www.programcreek.com/2014/03/leetcode-word-break-ii-java/

Deep copy a list in python:
https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
'''

class Node(object):
    def __init__(self, val=None, next_n=None):
        self.val = val
        self.next = next_n

def reconstruct(string, dict_set):
    '''
    Args:
        string(String)
        dict_set(Set)
    Returns:
        List
    '''
    ptr = [None] * (len(string) + 1)

    for i in xrange(len(string)):   # traverse each sub string
        for j in xrange(i, len(string) + 1):
            sub_string = string[i:j]
            if sub_string in dict_set:
                new_node = Node(sub_string)
                if not ptr[j]:
                    ptr[j] = new_node
                else:
                    add_at_tail(ptr[j], new_node)

    # testing:
    # ------------
    # for item in ptr:
    #     print ptr.index(item)
    #     while item:
    #         print item.val
    #         item = item.next

    res = list()    # final result
    curr = list()   # current words found
    dfs(ptr, res, curr, len(ptr) - 1)   # find out all combinations
    return res


def add_at_tail(head, node):
    '''
    Add at the end of the linked list
    Args:
        head(Node)
        node(Node)
    Returns:
        None
    '''
    while head.next:
        head = head.next
    head.next = node


def dfs(ptr, result, current, idx):
    '''
    Args:
        ptr(List)
        result(List)
        current(List)
        idx(int)
    Returns:
        None
    '''
    if idx == 0:    # get to the beginning, dfs ends, add current to result
        result.append(current) # reversed: current[::-1] or list(reversed(current))
        return

    if not ptr[idx]:    # hit a None
        return
    else:   # hit a word
        node = ptr[idx]
        while node:
            word = node.val
            # deepcopy: https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
            temp = current[:]
            temp.insert(0, word)     # normally append(word)
            dfs(ptr, result, temp, idx - len(word))
            node = node.next


def main():
    # dict_set = {'quick', 'brown', 'the', 'fox'}
    # string = 'thequickbrownfox'
    dict_set_2 ={'bed', 'bath', 'bedbath', 'and', 'beyond','dba'}
    string_2 = 'bedbathandbeyond'
    print reconstruct(string_2, dict_set_2)


if __name__ == '__main__':
    main()
