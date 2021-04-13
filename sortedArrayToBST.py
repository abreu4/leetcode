# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from utilities.BinaryTree import *

def sortedArrayToBST(nums):
        
    if not nums: return None 
    
    piv = len(nums)//2
    head = TreeNode(val=nums[piv])

    head.left = sortedArrayToBST(nums[:piv])
    head.right = sortedArrayToBST(nums[piv+1:])
    
    return head

head = sortedArrayToBST([-10,-3,0,5,9])
print_tree(head)


        