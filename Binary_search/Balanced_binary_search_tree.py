# write a function to create a balancesd binary search tree from sorted array/list of key-value pairs

"""
using recursive strategy;
- determine midpoint of the list, and turn it into root
- create left subtree
- create right subtree
- Return root nodes
"""

def balanced_BST(data, left= 0, right=None, parent=None):
    if right is None:
        right = len(data)-1
    if left > right:
        return None
    
    mid = (left + right) //2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left1 = balanced_BST(data, left, mid-1, root)
    root.right1 = balanced_BST(data, mid+1, right, root)
    return root
