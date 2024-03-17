# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# Solution: Create list containing altitudes at each point, then return max of the list
def largestAltitude(gain: list[int]) -> int:
    pre, max_altitude = 0, [0]
    for i in range(len(gain)):
        pre += gain[i]
        max_altitude.append(pre)
    return max(max_altitude)

print(largestAltitude([-5,1,5,0,-7]))