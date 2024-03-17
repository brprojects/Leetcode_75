# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Solution: Use prefix and postfix products to keep O(N)
def productExceptSelf(nums: list[int]) -> list[int]:
    products = [0] * len(nums) # This has much quicker runtime than append()
    pre = 1
    for i in range(len(nums)):
        pre *= nums[i]
        products[i] = pre
    post = 1
    for i in range(len(nums)-1, 0, -1):
        products[i] = post * products[i-1]
        post *= nums[i]
    products[0] = post
    return products

print(productExceptSelf([1,2,3,4,5,6]))