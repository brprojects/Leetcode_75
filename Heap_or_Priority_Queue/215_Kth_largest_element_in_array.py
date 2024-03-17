import heapq

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Solution: Using a heap
def findKthLargest(nums: list[int], k: int) -> int:
    heapq.heapify(nums)
    for i in range(len(nums)-k):
        heapq.heappop(nums)
    return nums[0]

# Solution: Use QuickSelect (similar to QuickSort) 
def findKthLargest2(nums: list[int], k: int) -> int:

    def partitioning(nums, low, high):
        pivot = nums[low]
        i, j = low+1, high
        
        while i <= j:
            if nums[i] < pivot and pivot < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            if nums[i] >= pivot:
                i += 1
            if pivot >= nums[j]:
                j -= 1
        
        nums[low], nums[j] = nums[j], nums[low]
        return j

    low, high = 0, len(nums)-1
    pivotIndex = len(nums)

    while pivotIndex != k-1 :
        pivotIndex = partitioning(nums, low, high)
        if pivotIndex < k-1:
            low = pivotIndex + 1
        else:
            high = pivotIndex - 1

    return nums[pivotIndex]

print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest2([3,2,1,5,6,4], 2))