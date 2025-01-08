# write a function to determine if a binary tree is balanced
"""
strategy:
    1. ensure left subtree is balanced
    2. ensure right subtree is balanced
    3. ensure the difference between heights of left subtree and 
    right subtree is not more than 1
    4. Return: balanced if balanced and height 
"""

def is_balanced(node):
    if node is None:
        return True, 0
    
    balanced_left, height_left = is_balanced(node.left)
    balanced_right, height_right = is_balanced(node.right)
    balanced = balanced_left and balanced_right and abs(height_left-height_right) <= 1
    height = 1 + max(height_left, height_right)
    return balanced, height