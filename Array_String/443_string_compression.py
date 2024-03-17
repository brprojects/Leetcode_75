# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.
# e.g. ['a','a','b','b','b'] -> ['a','2','b','3']

# Solution: Use two-pointers method where chk pointer moves ahead when it is at the same letter as the wrt pointer. Wrt pointer
# catches up when the letters are different, editing list on the way
def compress(chars: list[str]) -> int:
    wrt_pointer, chk_pointer = 0, 0
    current_char = None
    current_len = 0
    
    while chk_pointer < len(chars):
        if chars[chk_pointer] != current_char:
            # a new character
            if current_len > 1:
                len_str = list(str(current_len))
                for lstr in len_str:
                    chars[wrt_pointer] = lstr
                    wrt_pointer += 1
            chars[wrt_pointer] = chars[chk_pointer]
            wrt_pointer += 1
            current_char = chars[chk_pointer]
            current_len = 1
        else:
            # the same character
            current_len += 1
        chk_pointer += 1
    
    if current_len > 1:
        len_str = list(str(current_len))
        for lstr in len_str:
            chars[wrt_pointer] = lstr
            wrt_pointer += 1
    print(chars[:wrt_pointer])
    return wrt_pointer

print(compress(['a','b','b','b','b','b','b','b','b','b','b','b','b','b','b','c']))
print(compress(['a','a','a','a','b','c','b','a','a','a']))

# Not in place compression
def compressed2(chars: list[str]) -> int:
    compressed = []
    counter = 1
    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            counter += 1
        else:
            compressed.append(chars[i-1])
            if counter != 1:
                compressed.extend(list(str(counter)))
                counter = 1
    compressed.append(chars[-1])
    if counter != 1:
        compressed.extend(list(str(counter)))
    print(compressed)
    return len(compressed)

# print(compressed2(['a','b','b','b','b','b','b','b','b','b','b','b','b','b','b','c']))