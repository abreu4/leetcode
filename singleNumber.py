# https://leetcode.com/problems/single-number/

def singleNumber(nums):

	lookup = set()
	[lookup.remove(i) if i in lookup else lookup.add(i) for i in nums]

	return lookup.pop()

print(singleNumber([1,1,2,2,3,3,4]))