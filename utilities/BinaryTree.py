class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def _print(root, space): 
  
    if (root == None) : 
        return
  
    space += 10
 
    _print(root.right, space)  

    print()  
    for i in range(10, space): 
        print(end = " ")  
    print(root.val)
  
    _print(root.left, space) 

def print_tree(head):
    _print(head, 0)


def tree_from_array(arr):

    def insert_level_order(arr, root, i, n):

        # Base case for recursion 
        if i < n and arr[i]:
      
            temp = TreeNode(val=arr[i])
            root = temp 
      
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n) 
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
        
        return root

    # build binary search tree from sorted array
    head = None
    head = insert_level_order(arr, head, 0, len(arr))
    return head
