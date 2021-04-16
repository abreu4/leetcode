# https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
        
    i = 0
    n = len(nums)

    while i < n:
        if not nums[i]:
        	nums.append(nums.pop(i))
        	n -= 1
        else: i += 1
 	
A = [0,0,1]
B = [0,1,0,3,12]
moveZeroes(B)
print(B)