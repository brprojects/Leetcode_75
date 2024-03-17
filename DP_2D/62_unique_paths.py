# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or 
# right at any point in time. Given the two integers m and n, return the number of possible unique paths that the 
# robot can take to reach the bottom-right corner.

# Solution: Use grid to store number of paths to current square. Start knowing all of first row and column = 1,
# then add values of squares above and to the left to get routes to current square.
def uniquePaths(m: int, n: int) -> int:
    grid = [[0] * n for _ in range(m)]
    grid[0] = [1 for _ in range(n)]
    for col in grid:
        col[0] = 1

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    
    return grid[m-1][n-1]

print(uniquePaths(5, 7))