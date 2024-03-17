from functools import lru_cache

# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, 
# and the combinations may be returned in any order.

# Solution: Define end conditions for recursion which are either when we have a correct combination or
# when it's impossible to achieve a correct combination. The recurse through all possible combinations.
@lru_cache
def combinationSum3(k: int, n: int) -> list[list[int]]:
    ret = []

    def backtrack(start, cur_list, cur_sum):
        if cur_sum == n and len(cur_list) == k:
            ret.append(list(cur_list))
            return
        if len(cur_list) >= k or cur_sum > n:
            return
        for i in range(start, 9):
            backtrack(i+1, cur_list+[i+1], cur_sum+(i+1))

    backtrack(0, [], 0)
    return ret

print(combinationSum3(3, 9))