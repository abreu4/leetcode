# https://leetcode.com/problems/reverse-linked-list/

def reverseList(head):
        
        if not head: return None
        
        current = head
        p = None
        
        while current:
            
            tmp = current.next
            current.next = p
            
            p = current
            current = tmp
            
        return p