import heapq

# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. 
# Break the tie by the smallest index. For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, 
# we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2]. In the second hiring session, we will choose 1st worker 
# because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be 
# changed in the process.If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. 
# Break the tie by the smallest index.A worker can only be chosen once.

# Solution: Implement a heap for the left and right of the costs list to store candidates' costs. Take from whichever heap has the lowest
# value, then refill that heap. Need safeties for if not enough costs to keep both heaps filled.
def totalCost(costs: list[int], k: int, candidates: int) -> int:
    left, right = [], []
    l, r = 0, len(costs) - 1
    result = 0

    for _ in range(k):
        while len(left) < candidates and l <= r:
            heapq.heappush(left, costs[l])
            l += 1
        while len(right) < candidates and l <= r:
            heapq.heappush(right, costs[r])
            r -= 1
        
        v1 = left[0] if left else float('inf')
        v2 = right[0] if right else float('inf')

        if v1 <= v2:
            result += heapq.heappop(left)
        else:
            result += heapq.heappop(right)
    return result

print(totalCost([17,12,10,2,7,2,11,20,8], 3, 4))