class Node:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def printList(self):
        
        trail = self
        
        while trail.next:
            print(trail.val, end='-> ')
            trail = trail.next

        print(trail.val)