# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Solution: Have a left and right sum and as you iterate through the list subtract from right and add to left. If equal then return the index.
def pivotIndex(nums: list[int]) -> int:
    leftSum, rightSum = 0, sum(nums)
    for i in range(len(nums)):
        rightSum -= nums[i]
        if rightSum == leftSum:
            return i
        leftSum += nums[i]
    return -1

print(pivotIndex([1,7,3,6,5,6]))