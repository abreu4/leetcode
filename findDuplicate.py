# https://leetcode.com/problems/find-the-duplicate-number/

def findDuplicate(nums):
        seen = set()
        for i in nums: 
            if i in seen: return i
            else: seen.add(i)

A = [1,2,3,4,1,6]
print(findDuplicate(A))

# TODO: Implement Floyd's tortoise and hare algorithm (linked list cycle detection)
# https://www.codingninjas.com/blog/2020/09/09/floyds-cycle-detection-algorithm/