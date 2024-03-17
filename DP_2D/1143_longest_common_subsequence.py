# Given two strings text1 and text2, return the length of their longest common subsequence. If there 
# is no common subsequence, return 0. A subsequence of a string is a new string generated from the 
# original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Solution: create grid of text1 letters against text2 letters. dp[i][j] represents the longest common subsequence 
# of text1[0 ... i] & text2[0 ... j]. Make grid 1 row and column larger to avoid edge issues. Then go through loops shown.
def longestCommonSubsequence(text1: str, text2: str) -> int:
    len_text1, len_text2 = len(text1), len(text2)
    dp = [[0] * (len_text1+1) for _ in range(len_text2+1)]
    
    for i in range(1, len_text2+1):
        for j in range(1, len_text1+1):
            # If the characters match, take the diagonal value and add 1
            if text2[i-1] == text1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # If the characters do not match, take the maximum of the value from the left and above
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
    return dp[len_text2][len_text1]

print(longestCommonSubsequence("abcba", "abcbcba"))