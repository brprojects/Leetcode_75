from collections import defaultdict

# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there 
# is only one way to travel between two different cities (this network form a tree). 
# Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

# Solution: Create a dictionary to store all the connections, then implement a stack that starting from city 0
# adds all connected nodes to the stack if they haven't been visited yet. Add to count if connection needs to be reveresed
def minReorder(n: int, connections: list[list[int]]) -> int:
    connected_dict = defaultdict(list)
    for i in range(len(connections)):
        connected_dict[connections[i][0]].append(connections[i])
        connected_dict[connections[i][1]].append(connections[i])
    
    seen = set()
    stack = [0]
    count = 0

    while stack:
        city = stack.pop()
        seen.add(city)
        for i in connected_dict[city]:
            if i[0] == city:
                if i[1] not in seen:
                    stack.append(i[1])
                    count += 1
            else:
                if i[0] not in seen:
                    stack.append(i[0])
    return count

print(minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))