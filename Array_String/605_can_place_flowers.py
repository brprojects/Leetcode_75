# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n 
# new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Solution: Greedily place flowers, subtracting from n until reaching 0
def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return False

print(canPlaceFlowers([1,0,0,0,1,0,0], 2))
print(canPlaceFlowers([1,0,0,0,1,0,0], 3))