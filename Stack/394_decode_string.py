# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated 
# exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are 
# well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits 
# are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# Solution: Iterating through string, add elements until ']', then pop and generate a temp_string until '['.
# Then keep popping to get the number of repeats 'k' (could be multiple digits) and finally append temp_string k times to the stack.
def decodeString(s: str) -> str:
    stack = []
    for i in s:
        if i != ']':
            stack.append(i)
        else:
            temp_str = ''
            while stack[-1] != '[':
                temp_str = stack.pop() + temp_str
            stack.pop()
            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(temp_str * int(k))
    return ''.join(stack)

print(decodeString("2[ab3[c]]3[cd]ef"))