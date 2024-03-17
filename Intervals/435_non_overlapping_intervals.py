# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum 
# number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Solution: Sort intervals by start, then keep a pointer at the end. Iterating over intervals, if
# the interval overlaps update the end pointer to the smaller end value (ie remove interval with higher end value)
# and add one to the count.
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals = sorted(intervals, key=lambda x: x[0])
    res = 0
    end_pointer = float('-inf')

    for start, end in intervals:
        if start < end_pointer:
            res += 1
            if end < end_pointer:
                end_pointer = end
        else:
            end_pointer = end

    return res

print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))