from collections import defaultdict

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] 
# represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Solution: create a matrix using dictionaries and use dfs to search from start node of the query to try and reach the end node
def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0

        visited.add(start)
        for nextnode in graph[start]:
            if nextnode not in visited:
                visited.add(nextnode)
                temp = dfs(nextnode, end, visited)
                if temp != -1.0:
                    return temp * graph[start][nextnode]
        return -1.0

    graph = defaultdict(dict)
    for i in range(len(equations)):
        graph[equations[i][0]][equations[i][1]] = values[i]
        graph[equations[i][1]][equations[i][0]] = 1.0/values[i]
    
    solutions = []

    for dividend, divisor in queries:
        solutions.append(dfs(dividend, divisor, set()))
    
    return solutions

print(calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))