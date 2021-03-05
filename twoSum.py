# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):

        visited = {}
        
        for i, nr in enumerate(nums):

            if (target - nr) in visited:
                return [nums.index(target - nr), i]

            visited[nr] = True

        return False