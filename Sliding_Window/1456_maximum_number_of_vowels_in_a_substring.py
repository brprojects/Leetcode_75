# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Solution: Count vowels in first k characters, then add the next element and subtract the first and repeat.
def maxVowels(s: str, k: int) -> int:
    vowels = set("aeiou")
    curr_count = 0
    for i in vowels:
        curr_count += s[:k].count(i)
    max_count = curr_count
    for j in range(k, len(s)):
        if s[j] in vowels:
            curr_count += 1
        if s[j-k] in vowels:
            curr_count -= 1
        max_count = max(max_count, curr_count)
    return max_count

print(maxVowels('jifabriijtabii', 4))