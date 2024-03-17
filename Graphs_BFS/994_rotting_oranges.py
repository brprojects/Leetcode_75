# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Solution: Create a fresh set of oranges and subtract the rotting oranges from that set at each time
# End if no fresh oranges left or no rotting oranges
def orangesRotting(grid: list[list[int]]) -> int:
    row, col = len(grid), len(grid[0])
    rotting = {(i,j) for i in range(row) for j in range(col) if grid[i][j]==2}
    fresh = {(i,j) for i in range(row) for j in range(col) if grid[i][j]==1}
    timer = 0 
    
    while fresh:
        if not rotting: return -1
        rotting = {(i+di,j+dj) for i,j in rotting for di,dj in [(0,1),(1,0),(0,-1),(-1,0)] if (i+di,j+dj) in fresh}
        fresh -= rotting
        timer +=1
    return timer

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))