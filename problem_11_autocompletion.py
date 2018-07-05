'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of
all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to
speed up queries.
'''
from collections import defaultdict

class Trie_Node(object):
    def __init__(self, char=None):
        self.char = char
        self.children = defaultdict(Trie_Node)
        self.end_of_word = False


def add(trie_root, word):
    cur_node = trie_root
    for char in word:
        if char in cur_node.children:
            cur_node = cur_node.children[char]
        else:
            new_node = Trie_Node(char)
            cur_node.children[char] = new_node
            cur_node = new_node
    cur_node.end_of_word = True


def main():
    root = Trie_Node('*')
    str_list = ['dog', 'deer', 'deal']
    for word in str_list:
        add(root, word)
    print root.children['d'].children['e'].char
    print root.children['d'].children['e'].children

if __name__ == '__main__':
    main()
