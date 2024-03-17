# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Solution: Two pointers where fast pointer iterates along list whilst slow pointer sweeps any zeros to the end of the list.
# Switch the values at pointers if fast value != 0 and slow value == 0
def moveZeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
        if nums[slow] != 0:
            slow += 1
    return nums

print(moveZeroes([0,7,9,6,0,0,8,7,0,8]))