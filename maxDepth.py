# https://leetcode.com/problems/maximum-depth-of-binary-tree/

def maxDepth(self, root: TreeNode) -> int:
        
        if root is None: return 0
        
        depth = 1
        ld = lr = 0
        
        if root.left: ld = self.maxDepth(root.left)
        if root.right: lr = self.maxDepth(root.right)
            
        return depth + max(ld, lr)