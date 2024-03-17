# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Solution: Two pointers where always move pointer at the smaller height. Calculate water stored at each step to see if it's max area
def maxArea(height: list[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

print(maxArea([1,4,6,2,4,8,2,5,7]))