# A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, 
# find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the 
# peaks. You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly 
# greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.

# Solution: Because no neighbouring numbers are the same and nums[-1] = nums[n] = -∞, if we take the middle element and
# find one of its neighbouring elements is larger than it, we can create a new list which is half the size which also has 
# these properties. Repeating this process gives the result.
def findPeakElement(nums: list[int]) -> int:
    l, r = 0 , len(nums)-1
    while l < r:
        mid = l+(r-l)//2
        if nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid + 1
    return l

print(findPeakElement([1,2,1,3,5,6,4]))