# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents 
# its direction (positive meaning right, negative meaning left). Each asteroid moves 
# at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, 
# the smaller one will explode. If both are the same size, both will explode. Two 
# asteroids moving in the same direction will never meet.

# Solution: For each asteroid, while there's an element in the stack it will collide with, then pop the correct asteroid, otherwise add asteroid to the stack
def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for i in asteroids:
        while stack and i < 0 and stack[-1] > 0:
            if abs(i) > abs(stack[-1]):
                stack.pop()
            elif abs(i) == abs(stack[-1]):
                stack.pop()
                break
            else:
                break
        else:
            stack.append(i)
    return stack

print(asteroidCollision([2,1,-1,-3]))
