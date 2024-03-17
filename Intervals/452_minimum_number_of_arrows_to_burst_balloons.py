# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented 
# as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches 
# between xstart and xend. You do not know the exact y-coordinates of the balloons. Arrows can be shot up directly 
# vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is 
# burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A 
# shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

# Solution: Sort intervals by start, then keep a pointer at the end. Iterating over intervals, if
# the interval overlaps and the end < end_pointer, update the end pointer to the smaller end value.
# Add one to the count if there is no overlap with end_pointer and update end_pointer.
def findMinArrowShots(points: list[list[int]]) -> int:
    points = sorted(points, key=lambda x: x[0])
    res = 0
    end_pointer = float('-inf')

    for start, end in points:
        if start > end_pointer:
            res += 1
            end_pointer = end
        elif end < end_pointer:
            end_pointer = end

    return res

print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))