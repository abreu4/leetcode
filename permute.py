# https://leetcode.com/problems/permutations/

def permute(nums):

	if len(nums) <= 1: return [nums]

	res = []

	for permutation in permute(nums[1:]):
		for i in range(len(permutation) + 1):
			
			res.append(pp[:i] + [nums[0]] + pp[i:])

	return res




print(permute([1,2,3]))