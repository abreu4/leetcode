# https://leetcode.com/problems/subsets/

def subsets(nums):
        
    if not nums: return []

    def _subsets(nums):

        if len(nums) == 1: return [[nums[0]], []]

        result = []
        sss = _subsets(nums[1:])

        for s in sss:
            result.append([nums[0]] + s)
            result.append([] + s)

        return result

    return _subsets(nums)

nums1 = []
nums2 = [1,2,3,4]
print(subsets(nums2))