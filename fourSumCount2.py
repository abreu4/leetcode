# https://leetcode.com/problems/4sum-ii/

# Time complexity O(n)
# Count all possible sums' occurrences in first 2 vectors
# If complementing sum is found on remaining two vectors, add count to total
def fourSumCount2(nums1, nums2, nums3, nums4):

    AB = {}
    total = 0

    for a in nums1:
        for b in nums2:
            try: AB[a+b] += 1
            except: AB[a+b] = 1
    
    for c in nums3:
        for d in nums4:
            try: total += AB[-c-d]
            except: pass

    return total

print(fourSumCount2([1,2], [-2,-1], [-1,2], [0,2]))