# https://leetcode.com/problems/binary-tree-inorder-traversal/

from utilities.tree_node import TreeNode

def inorderTraversal(root):
                
        if not root: return []
        result = []

        if root.left: result += inorderTraversal(root.left)
        
        result.append(root.val)
            
        if root.right: result += inorderTraversal(root.right)

        return result


head = TreeNode(val=1)
head.right = TreeNode(val=2)
head.right.left = TreeNode(val = 3)

print(inorderTraversal(TreeNode(val=1)))
print(inorderTraversal(head))