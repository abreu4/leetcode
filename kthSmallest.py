# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from utilities.BinaryTree import *

# Wrapper
def kthSmallest(root, k, approach=1):
    if approach == 1: return kthSmallest1(root, k)
    if approach == 2: return kthSmallest2(root, k)

# Naive approach
# Computer full in order traversal iteratively
# Return kth result
def kthSmallest1(root, k):
    
    if root is None: return None

    result = []
    stack = []
    node = root

    while stack or node:
        
        if node:
            stack.append(node)
            node = node.left
        
        else:
            node = stack.pop()
            result.append(node.val)
            node = node.right
        
    return result[k-1]

# Optimized approach 1
# Stop iterative inorder traversal once kth min element has been found
def kthSmallest2(root, k):
            
    stack = []
    node = root
    ctr = 0
    
    while stack or node:

        if node:
            stack.append(node)
            node = node.left

        else:
            
            node = stack.pop()
            
            ctr += 1
            if ctr == k: return node.val
            
            node = node.right

    return None

head = tree_from_array([5,3,6,2,4,None,None,1])
print_tree(head)
print(kthSmallest(head, k=2))