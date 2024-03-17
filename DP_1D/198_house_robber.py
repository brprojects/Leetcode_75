# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money 
# stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems 
# connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money
# you can rob tonight without alerting the police.

# Solution: Working forward through list, find the max amount that you can steal whilst robbing the current house by adding
# the house's amount to the max of either the max of house two or three before it. Store max value for each house in a dict.
def rob(nums: list[int]) -> int:
    houses = len(nums)
    if houses <= 2:
        return max(nums)
    house_dict = {0:nums[0], 1:nums[1], 2:nums[2]+nums[0]}
    for i in range(3, houses):
        house_dict[i] = nums[i] + max(house_dict[i-2], house_dict[i-3])
    return max(house_dict[houses - 1], house_dict[houses - 2])

print(rob([1,2,3,1,6,2,3,6]))