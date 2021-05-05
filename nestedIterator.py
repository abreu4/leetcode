# https://leetcode.com/problems/flatten-nested-list-iterator/


class NestedIterator:
    
    def __init__(self, nestedList):
        self._stack = nestedList[::-1]
        
    def next(self):
        
        return self._stack.pop().getInteger()
                       
        
    def hasNext(self):
        
        while self._stack:
            if self._stack[-1].isInteger():
                return True
            self._stack.extend(self._stack.pop().getList()[::-1])

        return False


# Kudos to https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80142/8-line-Python-Solution