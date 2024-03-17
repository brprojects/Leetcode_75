from bisect import bisect_left
# You are given two positive integer arrays spells and potions, of length n and m respectively, 
# where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the 
# product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

# Solution: Sort potions then binary search
def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    successes = []
    potions.sort()
    m = len(potions)

    for spell in spells:
        l, r = 0, m
        while l < r:
            mid = l+(r-l)//2
            if potions[mid] < success/spell:
                l = mid + 1
            else:
                r = mid
        successes.append(m - l)

    return successes

# Solution: bisect_left finds the index where the specified value can be inserted into a sorted sequence.
# If the value is already present in the sequence, it returns the leftmost index where the value should be inserted.
def successfulPairs2(spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort()

    results = []
    for spell in spells:
        desired_potion = success / spell
        i = bisect_left(potions, desired_potion)
        results.append(len(potions) - i)
    return results

print(successfulPairs([5,1,3], [1,2,3,4,5], 7))
print(successfulPairs2([5,1,3], [1,2,3,4,5], 7))
