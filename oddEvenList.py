# https://leetcode.com/problems/odd-even-linked-list/

from utilities.SinglyLinkedList import Node, linked_list_from_list

def oddEvenList(head):
    
    if not head: return None
    if not head.next: return head

    it = head.next.next
    odd = True

    h1 = t1 = head
    h2 = t2 = head.next

    while it:
        
        if odd:
            t1.next = it
            t1 = t1.next
            
        else:
            t2.next = it
            t2 = t2.next
            
        it = it.next
        odd = not odd
        
    t1.next = h2
    t2.next = None
    return h1


A = linked_list_from_list([1,2,3,4,5])
A = oddEvenList(A)
A.print_list()
