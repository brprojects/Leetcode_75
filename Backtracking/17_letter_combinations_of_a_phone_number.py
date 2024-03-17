# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order. The mapping of digits to letters is just like on telephone buttons. 
# Note that 1 does not map to any letters.

# Solution: Iterate through each letter that the first remaining digit maps to, and recursively call the "backtrack" 
# function with the new combination and the remaining digits.
def letterCombinations(digits: str) -> list[str]:
    phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []

    def backtrack(combination, next_digits):
        if not next_digits:
            res.append(combination)
            return
        
        for letter in phone[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:])
    
    if digits:
        backtrack("", digits)
    return res

print(letterCombinations("356"))