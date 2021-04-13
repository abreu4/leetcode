# https://leetcode.com/problems/majority-element/

def majorityElement(nums):
        nums.sort()
        return nums[len(nums)//2]

A = [2,2,1,1,1,2,2]
print(majorityElement(A))
