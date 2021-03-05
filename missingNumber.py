# https://leetcode.com/problems/missing-number/

def missingNumber(nums):

        expected_sum = sum(x for x in range(len(nums)+1))
        current_sum = sum(nums) 

        return expected_sum - current_sum