# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

# Solution: Find number of bits to flip to turn a or b into c, then add number of bits where a and b doesn't equal c
# XOR: ^, OR: |, AND: &, NOT: ~
def minFlips(a: int, b: int, c: int) -> int:
    
    # Count number of ones in binary representation of a number
    def count_ones(n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    
    own = (a | b) ^ c
    repeat = (a & b) & ~c
    return count_ones(own) + count_ones(repeat)

print(minFlips(10, 8, 7))
# 10 -> 1010
# 8 -> 1000
# 7 -> 0111