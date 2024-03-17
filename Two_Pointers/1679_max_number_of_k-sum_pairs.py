# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Solution: Uses dictionary. 'get(key, 0)' returns default value 0 if key is not found in dict.
def maxOperations(nums: list[int], k: int) -> int:
        operations = 0
        nums_dict = {}
        for i in nums:
            if nums_dict.get(k-i, 0) > 0:
                nums_dict[k-i] -= 1
                operations += 1
            else:
                nums_dict[i] = nums_dict.get(i, 0) + 1      
        return operations 

print(maxOperations([0,1,2,3,4,5,6],5))

# Solution: Use two pointer method and list sort
def maxOperations2(nums: list[int], k: int) -> int:
    ops = 0
    nums.sort()
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] + nums[right] == k:
            ops += 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] < k:
            left += 1
        else:
            right -= 1
    return ops

print(maxOperations2([0,1,2,3,4,5,6],5))