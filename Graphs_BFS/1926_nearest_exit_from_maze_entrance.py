# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
# You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and 
# column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, 
# and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. 
# An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

# Solution: implement a queue that has empty sqaures added getting progressively further from the entrance, until
# one of the squares is an exit
def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    queue = [[entrance[0], entrance[1], 0]]
    maze[entrance[0]][entrance[1]] = "+"
    movement = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    y, x, dist = queue.pop(0)
    for i in movement:
        if y+i[0]>=0 and y+i[0]<=len(maze)-1 and x+i[1]>=0 and x+i[1]<=len(maze[0])-1 and maze[y+i[0]][x+i[1]] == ".":
            queue.append([y+i[0], x+i[1], dist+1])
            maze[y+i[0]][x+i[1]] = "+"
    
    while queue:
        y, x, dist = queue.pop(0)
        if (x == 0 or x == len(maze[0])-1 or y == 0 or y == len(maze)-1):
            return dist
        for i in movement:
            if maze[y+i[0]][x+i[1]] == ".":
                queue.append([y+i[0], x+i[1], dist+1])
                maze[y+i[0]][x+i[1]] = "+"
    return -1

print(nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))