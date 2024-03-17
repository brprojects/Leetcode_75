def guess(n):
    if n > 6:
        return -1
    elif n < 6:
        return 1
    elif n == 6:
        return 0
    
# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
    
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# Solution: Binary search with 1 as minimum step
def guessNumber(n: int) -> int:
    step = max(1, n//4)
    ans = n//2
    while True:
        resp = guess(ans)
        if resp == 0:
            return ans
        else:
            ans += step*resp
            step = max(1, step//2)

# Solution: Two pointer
def guessNumber2(n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = l + (r - l)//2
            resp = guess(mid)
            if resp == -1:
                r = mid - 1
            elif resp == 1:
                l = mid + 1
            else:
                return mid
        return l

print(guessNumber(10))
print(guessNumber2(10))