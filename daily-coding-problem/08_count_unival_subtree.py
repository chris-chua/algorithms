"""Google interview question

A unival tree (which stands for "universal value")
is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

 class Node(object):
    def __init__(self, left=None, right=None, is_unival=False):
         self.val = val
         self.left = left
         self.right = right
         self.is_unival = is_unival

def count_unival_subtree(node):
    if node.left == node.right == None:
        node.is_unival = True
        return 1
        
    left = 0
    right = 0

    if node.left:
        left = count_unival_subtree(node.left)
    if node.right:
        right = count_unival_subtree(node.right)
    
    if node.left and node.right:    # node has both left and right
        