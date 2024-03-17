# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Solution: Using two pointers replace vowels as they are reached by the pointers
def reverseVowels(s: str) -> str:
    s = list(s)
    n = len(s)
    left = 0
    right = n-1
    vowels = set("aeiouAEIOU")
    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s)

print(reverseVowels('hElloO man'))