# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
# without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Solution: Fast pointer works through t, whilst slow pointer works through s if the values are the same
def isSubsequence(s: str, t: str) -> bool:
        if s == "":
            return True
        slow = 0
        for fast in range(len(t)):
            if s[slow] == t[fast]:
                slow += 1
                if slow == len(s):
                    return True
        return False

print(isSubsequence('ace','ratwcfef'))
print(isSubsequence('axe','ratwcfef'))