# https://leetcode.com/problems/rotate-image/

def rotate(matrix):
        
    n = len(matrix[0])
    if n <= 1: return matrix
    if n != len(matrix): return matrix
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for x in matrix: x.reverse() 


I = [[1,2,3],[4,5,6],[7,8,9]]

print(f"Before: {I}")
rotate(I)
print(f"After {I}")