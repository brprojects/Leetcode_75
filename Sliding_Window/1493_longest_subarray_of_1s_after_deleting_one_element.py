# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Solution: Use two pointer method and answer is difference of two pointers, reduce k if fast at 0, then if k < 0 advance slow, increasing k if slow at 0
def longestSubarray(nums: list[int]) -> int:
    slow, k = 0, 1
    for fast in range(len(nums)):
        if nums[fast] == 0:
            k -= 1
        if k < 0:
            if nums[slow] == 0:
                k += 1
            slow += 1
    return fast - slow

print(longestSubarray([0,1,1,1,0,1,1,0,1]))