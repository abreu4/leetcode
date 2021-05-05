# https://leetcode.com/problems/unique-paths/

import time

# Dynamic programming
def uniquePathsA(m, n):        
    
    s = time.time()

    grid = [[1 for j in range(n)] for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    print(f"Time A {time.time() - s}")

    return grid[-1][-1]

# Hash (faster)
def uniquePathsB(m, n):

    s = time.time()

    paths = {}

    for i in range(m):
        for j in range(n):
            try: paths[(i, j)] = paths[(i-1, j)] + paths[(i, j-1)]
            except: paths[(i, j)] = 1

    print(f"Time B {time.time() - s}")

    return paths[(m-1, n-1)]

m = 3
n = 7

resultA = uniquePathsA(m, n)
resultB = uniquePathsB(m, n)

print(f"Result A: {resultA}")
print(f"Result B: {resultB}")