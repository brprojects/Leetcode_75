# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Solution: Append a letter from each word until the shorter word is finished
def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    for i in range(min(len(word1),len(word2))):
        merged.append(word1[i] + word2[i])        
    return (''.join(merged)+word1[i+1:]+word2[i+1:])

print(mergeAlternately('pass', 'man'))