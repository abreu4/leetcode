# https://leetcode.com/problems/product-of-array-except-self/

import time
import random

# First approach
# O(2n) time complexity
def productExceptSelf(nums):
    
    start = time.time()

    if len(nums) <= 1: return nums
        
    prod = nums[0]
    zero_index = False
    result = [0]*len(nums)
    
    for i, nr in enumerate(nums[1:], 1):
        
        if not nr: 
            if zero_index: return result
            zero_index = i
            continue
        
        prod *= nr
        
    
    if zero_index: result[zero_index] = prod
    else:
        for j, nr in enumerate(nums):
            result[j] = int(prod/nr)

    print(time.time() - start)            
    return result

# Second approach
# Courtesy of L4pl0x
# See https://leetcode.com/problems/product-of-array-except-self/discuss/580519/Python-One-Pass-O(1)-Space-No-Division
# Iterating over array with 2 pointers
# When trailing pointer crosses element, result becomes everything behind it.
# Conversely, the same happens for the leading pointer.
# Hence index at i becomes product of all elements behind and ahead of it.
def productExceptSelf2(nums):

    result = [1]*len(nums)
    trail = 1
    lead = 1

    for i in range(len(nums)):
        result[i] *= trail
        result[-1-i] *= lead
        trail *= nums[i]
        lead *= nums[-1-i]

    return result


A = [random.randint(1,5) for _ in range(1,20)]
B = [1,2,3,4]