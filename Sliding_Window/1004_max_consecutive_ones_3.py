# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Solution: Use two pointer method and answer is difference of two pointers, reduce k if fast at 0, then if k < 0 advance slow, increasing k if slow at 0
def longestOnes(nums: list[int], k: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                k -= 1
            if k < 0:
                if nums[slow] == 0:
                    k += 1
                slow += 1
        return fast - slow + 1

print(longestOnes([0,1,1,0,0,0,1,1,0,1], 3))