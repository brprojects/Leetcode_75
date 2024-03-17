
# There are n cities. Some of them are connected, while some are not. 
# If city a is connected directly with city b, and city b is connected directly with city c, 
# then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city 
# are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Solution: Keep track of visited cities and visit all connected cities in one province using dfs,
# so any cities which haven't been visited must be in a different province
def findCircleNum(isConnected: list[list[int]]) -> int:
    n = len(isConnected)
    visited = set()
    count = 0

    def dfs(i):
        if i in visited:
            return
        visited.add(i)
        for j in range(n):
            if isConnected[i][j]:
                dfs(j)
    
    for i in range(n):
        if i not in visited:
            count += 1
            dfs(i)
    
    return count

print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))