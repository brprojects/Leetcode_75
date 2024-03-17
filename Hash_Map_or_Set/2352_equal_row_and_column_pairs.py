# Given an n x n integer matrix grid, return the number of pairs (ri, cj) 
# such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements 
# in the same order (i.e., an equal array).

# Solution: Create a dict with columns stored as tuples. Iterate through grid rows and check if they are in columns dict.
def equalPairs(grid: list[list[int]]) -> int:
    columns = dict()
    pairs = 0
    for i in range(len(grid[0])):
        if tuple(column[i] for column in grid) not in columns:
            columns[tuple(column[i] for column in grid)] = 1
        else:
            columns[tuple(column[i] for column in grid)] += 1
    print(columns)
    for i in grid:
        if tuple(i) in columns:
            pairs += columns[tuple(i)]
    return pairs

print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))