# https://leetcode.com/problems/kth-largest-element-in-an-array/

def findKthLargest(nums, k):

	crescent_nums = sorted(nums)
	crescent_nums.reverse()

	return crescent_nums[k-1]

A = [3,2,1,5,6,4]
B = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(B, k))