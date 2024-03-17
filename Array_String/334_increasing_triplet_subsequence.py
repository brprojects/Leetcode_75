# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k 
# and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Solution: Iterate through nums, and place each element in the least position (first thought third) for which it qualifies, 
# should it qualify. If we find a third, we succeed (True), otherwise we fail (False).
def increasingTriplet(nums: list[int]) -> bool:
    smallest = next_smallest = float('inf')
    for i in nums:
        if i <= smallest:
            smallest = i
        elif i <= next_smallest:
            next_smallest = i
        else:
            return True
    return False

print(increasingTriplet([5,3,2,7,4,9]))
print(increasingTriplet([1,1,1,1,1,1]))