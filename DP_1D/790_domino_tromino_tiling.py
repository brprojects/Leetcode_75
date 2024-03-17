# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there 
# are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

# [   ] or ︹︹ or [   ][ ]      [   ] or [   ]
# [   ]    ︺︺    [ ][   ]      [ ]      [ ][   ]
# Solution: For each length, need to keep track of number of combinations resulting in completed edge (left above) or with an overhang (right above).
# Then use DP to work out number of combinations for larger values of n
def numTilings(n: int) -> int:
    tile = [[0, 0] for _ in range(n+2)]
    tile[1] = [1, 0]
    tile[2] = [2, 1]
    
    for i in range(3, n+1):
        tile[i][0] = tile[i-1][0] + tile[i-2][0] + 2 * tile[i-1][1]
        tile[i][1] = tile[i-2][0] + tile[i-1][1]
    
    return tile[n][0] % 1000000007

print(numTilings(15))