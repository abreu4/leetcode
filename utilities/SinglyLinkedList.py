class Node:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def print_list(self):
        
        trail = self
        
        while trail.next:
            print(trail.val, end='-> ')
            trail = trail.next

        print(trail.val)

def linked_list_from_list(l):

    head = Node(val = l[0])
    trail = head
    for i in range(1, len(l)):
        new = Node(val = l[i])
        trail.next = new
        trail = new

    return head