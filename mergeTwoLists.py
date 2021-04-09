# https://leetcode.com/problems/merge-two-sorted-lists/

from utilities.singly_linked_list_node import Node

def linkedListFromList(l):
    
    head = Node(val = l[0])
    trail = head
    for i in range(1, len(l)):
        new = Node(val = l[i])
        trail.next = new
        trail = new

    return head

def mergeTwoLists(l1, l2):
               
    if not l1 and not l2: return None
    if not l1: return l2
    if not l2: return l1
        
    head, current, node_left, node_right = None, None, None, None
            
    if l1.val < l2.val:
        head = l1
        current = l1
        node_left = l1.next
        node_right = l2
    else:
        head = l2
        current = l2
        node_left = l1
        node_right = l2.next
        
    while node_left and node_right:
        
        if node_left.val < node_right.val:
            current.next = node_left
            current = node_left
            node_left = node_left.next
            
        else:
            current.next = node_right
            current = node_right
            node_right = node_right.next

    if node_right: current.next = node_right
    elif node_left: current.next = node_left 
    
    return head

l1 = [1,2,4]
l2 = [1,3,4]

ll1, h1 = None, None
ll2, h2 = None, None

ll1 = linkedListFromList(l1)
ll2 = linkedListFromList(l2)

ll1.printList()
ll2.printList()

mergeTwoLists(ll1, ll2).printList()



