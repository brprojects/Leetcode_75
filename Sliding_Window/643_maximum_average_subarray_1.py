# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 

# Solution: Calculate sum for first k elements, then add the next element and subtract the first and repeat.
def findMaxAverage(nums: list[int], k: int) -> float:
    curr_sum = max_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k

print(findMaxAverage([2,5,4,3,2,5,7,8,4,21,4,31,5], 3))