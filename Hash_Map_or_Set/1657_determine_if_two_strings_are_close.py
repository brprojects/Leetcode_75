# Two strings are considered close if you can attain one from the other using the following operations:
#   Operation 1: Swap any two existing characters.
#       For example, abcde -> aecdb
#   Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#       For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#   You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# Solution: Create two dicts, create lists out of their sorted values and compare
def closeStrings(word1: str, word2: str) -> bool:
    if set(word1) != set(word2):
        return False
    word1_dict = {}
    word2_dict = {}
    for i in word1:
        if i not in word1_dict:
            word1_dict[i] = 1
        else:
            word1_dict[i] += 1
    for i in word2:
        if i not in word2_dict:
            word2_dict[i] = 1
        else:
            word2_dict[i] += 1
    word1_values = sorted(word1_dict.values())
    word2_values = sorted(word2_dict.values())
    if word1_values == word2_values:
        return True
    else:
        return False
    
print(closeStrings("cabbba", "abbccc"))

from collections import Counter
# Using counters (lower runtime)
def closeStrings2(word1: str, word2: str) -> bool:
    if set(word1) != set(word2):
        return False
    word1_dict = Counter(word1)
    word2_dict = Counter(word2)
    word1_values = sorted(word1_dict.values())
    word2_values = sorted(word2_dict.values())
    if word1_values == word2_values:
        return True
    else:
        return False

print(closeStrings2("cabbba", "abbccc"))