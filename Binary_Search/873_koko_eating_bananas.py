import math
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours. Koko can decide her bananas-per-hour eating speed of k. 
# Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
# she eats all of them instead and will not eat any more bananas during this hour. Koko likes to eat slowly but still 
# wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Solution: Binary search from k = 1 to k = max(piles), calculating time and comparing to h at each step
def minEatingSpeed(piles: list[int], h: int) -> int:
    n = len(piles)
    piles.sort()
    l, r = 1, piles[-1]

    while l < r:
        mid = l+(r-l)//2
        time = 0
        for pile in piles:
            time += math.ceil(pile/mid)
        if time > h:
            l = mid + 1
        else:
            r = mid
    return l

print(minEatingSpeed([3,6,7,11], 8))