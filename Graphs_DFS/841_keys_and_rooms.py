# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
# Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. 
# Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
# return true if you can visit all the rooms, or false otherwise.

# Solution: Store rooms and their keys in a dict, then when a room is visited store its keys in a stack.
# When the stack is empty check every room has been visited
def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    rooms_dict = {}
    key_stack = []

    for i in range(1,len(rooms)):
        rooms_dict[i] = rooms[i]

    if len(rooms) != 0:
        for i in rooms[0]:
            key_stack.append(i)
        
    while key_stack != []:
        curKey = key_stack.pop()
        if curKey in rooms_dict:
            for i in rooms_dict[curKey]:
                key_stack.append(i)
            rooms_dict.pop(curKey)
    
    return rooms_dict == {}

print(canVisitAllRooms([[1],[2],[3],[]]))
print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))