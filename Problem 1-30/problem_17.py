'''
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory
subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1
contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext.

We are interested in finding the longest (number of characters) absolute path
to a file within our file system. For example, in the second example above,
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length
is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the
length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''

class Node(object):
    '''
    Node of a Directory N-ary Tree
    '''
    def __init__(self, val=None, level=None, parent=None, is_file=False):
        self.val = val
        self.level = level
        self.parent = parent
        self.subdir = list()    # Node's children as a list
        self.is_file =is_file

    def add_node(self, node=None):
        self.subdir.append(node)

    def get_parent(self):
        return self.parent


class Tree(object):
    '''
    A Directory N-ary Tree
    '''
    def __init__(self, root=None):
        self.root = Node('*', -1)


def build_tree(path_str):
    '''
    Build a directory n-ary tree
    Args:
        path_str(string): a string represented a fild system path
    Returns:
        Tree: a directory tree
    '''
    path_dir = path_str.split('\n')
    dir_tree = Tree()
    cur_level = -1
    cur_root = dir_tree.root

    for token in path_dir:
        tabs = 0
        while token[tabs] == '\t':
            tabs += 1

        if cur_level >= tabs:   # need to back track the parent node
            i = cur_level - tabs + 1
            while i != 0:
                cur_root = cur_root.get_parent()
                i -= 1

        if len(token.split('.')) > 1:   # is a file
            new_node = Node(token[tabs:], tabs, cur_root, True)
        else:   # not a file
            new_node = Node(token[tabs:], tabs, cur_root)

        cur_root.add_node(new_node)
        cur_level = tabs
        cur_root = new_node

    return dir_tree


def lgst_file_path(node):
    '''
    Given a tree node, find the longest absolute path to a file
    Args:
        node(Node): a tree node
    Returns:
        int: the length of the longest path
    '''
    if node.is_file:    # hit a leaf, and leaf is a file
        return len(node.val)
    if len(node.subdir) == 0:   # hit a leaf but a dir
        return 0

    max_len = 0
    for sub_node in node.subdir:
        max_len = max(max_len, lgst_file_path(sub_node))

    # node.level < 0 means this node is root
    length = max_len if node.level < 0 else max_len + len(node.val) + 1

    return length


def main():
    path_str = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
    path_str_2 = ('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext' +
                    '\ndir2\n\tsubdir1\n\tsubdir2\n\t\tsubsubdir1\n\t\t\tsubsubsubdir3\n\t\t\t\tfile3.ext')
    tree = build_tree(path_str_2)
    print lgst_file_path(tree.root)

if __name__ == '__main__':
    main()
