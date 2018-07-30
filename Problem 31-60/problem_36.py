'''
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
'''
'''
Note:
https://www.geeksforgeeks.org/second-largest-element-in-binary-search-tree-bst/

The second largest element is second last element in inorder traversal and second
element in reverse inorder traversal. We traverse given Binary Search Tree in
reverse inorder and keep track of counts of nodes visited. Once the count becomes
2, we print the node.
'''
