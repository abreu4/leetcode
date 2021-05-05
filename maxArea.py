# https://leetcode.com/problems/container-with-most-water/

# O(n²) time complexity
# (Times out when submitted)
def maxAreaA(height):

    max_area = 0
    previous = 0

    for i, _ in enumerate(height):
    
        if height[i] < previous: continue
        previous = height[i]

        for j, _ in enumerate(height[i+1:], i+1):

            current_height = height[j] if height[j] <= height[i] else height[i]
            
            max_area = max(max_area, current_height*(j-i))

    return max_area

# O(n) time complexity
# See https://leetcode.com/problems/container-with-most-water/
# Can optimize further by keeping track of how much the height must increment for each unit of width lost
# Only re-calculate if said height is found
def maxAreaB(height):
    
    max_area = 0
    i, j = 0, len(height) - 1

    while i < j:

        max_area = max(max_area, min(height[i], height[j]) * (j-i) )

        if height[i] < height[j]: i += 1
        else: j -= 1

    return max_area

A = [1,8,6,2,5,4,8,3,7]
print(maxAreaB(A))