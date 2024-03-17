# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Solution: XOR (^) all the numbers in the list as a XOR a == 0
def singleNumber(nums: list[int]) -> int:
    res = 0
    for i in nums:
        res = res ^ i
    return res

print(singleNumber([4,1,2,1,2]))