# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# O(n) space
# O(nlogn) time
def kthSmallest2A(matrix, k):

    n = len(matrix)
    if k > n*n: return None

    A = []
    [A.extend(row) for row in matrix]

    return sorted(A)[k-1]

def kthSmallest2B(matrix, k):
	# TODO



M = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print(kthSmallest2(M, k))