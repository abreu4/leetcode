# https://leetcode.com/problems/game-of-life/

# O(2mn) time complexity
# O(mn) space complexity
# TODO: Use a list of lists intead of a hash map for slightly better time complexity
def gameOfLife(board):

    if not board: return None

    m = len(board)
    n = len(board[0])
    state = {}

    # Update states
    for i in range(m):
        for j in range(n):
            state[(i, j)] = board[i][j]

    # Update cells
    for i in range(m):
        for j in range(n):
            total = 0
            for k in (0,1):
                try: total += state[(i+k, j+1)] # board[i+k][j+1]
                except: pass
                try: total += state[(i-k, j-1)] # board[i-k][j-1]
                except: pass
                try: total += state[(i+1, j-k)] # board[i+1][j-k]
                except: pass
                try: total += state[(i-1, j+k)] # board[i-1][j+k]
                except: pass

            if total < 2: board[i][j] = 0
            if total <= 3 and board[i][j]: board[i][j] = 1
            elif total == 3 and not board[i][j]: board[i][j] = 1
            else: board[i][j] = 0

# TODO: investigate hashing the cell transformation for 
# each possible binary sequence.
# Since at any given cell there can only be 2^(n * 3) number of
# different combinations, this would in theory reduce the compute time
# of each cell's state. 


B = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife(B)
print(B)
                
                