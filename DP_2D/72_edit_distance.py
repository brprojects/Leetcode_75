# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Solution: create grid of word1 letters against word2 letters. dp[i][j] represents the longest common subsequence 
# of word1[0 ... i] & word2[0 ... j]. Make grid 1 row and column larger to avoid edge issues. Then go through loops shown.
def minDistance(word1: str, word2: str) -> int:
    len_word1, len_word2 = len(word1), len(word2)
    if len_word1 == 0 or len_word2 == 0:
        return max(len_word1, len_word2)
    if word1 == word2:
        return 0

    # If len_word1 or len_word2 == 0 then minimum distance is length of other word, this is shown in the zero index column and row
    dp = [[i] + [0] * (len_word1) for i in range(len_word2+1)]
    dp[0] = [i for i in range(len_word1+1)]
    
    for i in range(1, len_word2+1):
        for j in range(1, len_word1+1):
            # If the characters match, take the diagonal value, as no edit is needed
            if word2[i-1] == word1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # If the characters do not match, take the minimum of the value from the left, above and diagonal and add 1
                # Diagonal represents min distance after replacing character at position i-1 with character at j-1
                # Above represents min distance after inserting character at position j-1 into word2
                # Left represents min distance after deleting character at position i-1 of word1
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
    return dp[len_word2][len_word1]

print(minDistance('horse', 'ros'))