# https://leetcode.com/problems/binary-tree-level-order-traversal/

from utilities.BinaryTree import *

# Inspired by
# https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
def levelOrder(root):

    if not root: return

    result, q = [], [root]

    while q:

        result.append([node.val for node in q])

        tmp = []
        for n in q:
            tmp.extend([n.left, n.right])

        q = [n for n in tmp if n]

    return result


head = tree_from_array([3,9,20,None,None,15,7])
head2 = tree_from_array([1,2,None,3,None,4,None,5])

print_tree(head)
print(levelOrder(head))
