# https://leetcode.com/problems/top-k-frequent-elements/

# Using hash table to keep track of element frequencies
# and min heap to extract 3 smallest elements
# O(3n) worst case time complexity (k = len(nums) = # unique elements)
def topKFrequent(nums, k):
    
    import heapq
    from collections import defaultdict
    
    priority = []
    result = []
    frequency = defaultdict(int)
    
    heapq.heapify(priority)
    
    for i in nums: frequency[i] += 1
    [heapq.heappush(priority, (-frequency[i], i)) for i in frequency]
    [result.append(heapq.heappop(priority)[1]) for i in range(k)]
        
    return result

A = [1,1,1,2,2,3]
B = [1,2,3,4,5,2]
k = 2
print(topKFrequent(A, k))


# TODO: A leetcode user mentioned a way to solve this in O(n) time
# Check https://leetcode.com/problems/top-k-frequent-elements/discuss/740374/Python-5-lines-O(n)-buckets-solution-explained