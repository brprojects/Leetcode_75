# You are given a string s, which contains stars *.
# In one operation, you can:
#     Choose a star in s.
#     Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Solution: With a stack iterate through string and if character is a star pop from the stack, otherwise append character to stack.
def removeStars(s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else:    
                stack.append(i)
        return ''.join(stack)

print(removeStars("leet**cod*e"))