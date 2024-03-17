# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number 
# of 1's in the binary representation of i.

# Solution: For odd numbers the bit count increases by one from previous number, while for even numbers the bit count
# is the same as the bit count for half the number (ie shift all digits left by one and add a zero).
def countBits(n: int) -> list[int]:
    res = [0] * (n + 1)
    for i in range(1, n+1):
        if i % 2 == 1:
            res[i] = res[i-1] + 1
        else:
            res[i] = res[i//2]
    return res

print(countBits(10))