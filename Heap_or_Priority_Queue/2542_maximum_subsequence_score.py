import heapq

# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. 
# You must choose a subsequence of indices from nums1 of length k.

# For chosen indices i0, i1, ..., ik - 1, your score is defined as:

# The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
# Return the maximum possible score.

# Solution: Zip nums1 and nums2 and sort by decreasing nums2. Then go through the pairs calculating the ans, then removing the lowest
# value of nums1. Since pairs is sorted decreasing by nums2 can always know the current iteration of nums2 is the smallest.
# Use prefix sum to store sum of values.
def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    pairs = sorted(zip(nums1, nums2), key = lambda x:-x[1])
    heap = []
    ans, prefix = 0, 0

    for n1, n2 in pairs:
        heapq.heappush(heap, n1)
        prefix += n1
        if len(heap) == k:
            ans = max(ans, prefix * n2)
            prefix -= heapq.heappop(heap)
    return ans

print(maxScore([1,3,3,2], [2,1,3,4], 3))