# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Solution: Working backwards from third from top stair, update the cost of the stair to its cost plus the 
# min cost of the two stairs above it. Then do this until reaching the first and second stair. Answer is
# the min of those two stairs.
def minCostClimbingStairs(cost: list[int]) -> int:
    for i in range(len(cost)-3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])

    return min(cost[0], cost[1])

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))