# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
# is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for 
# which this is possible, keep answer[i] == 0 instead.

# Solution: Implement a monotonic stack which stores the indices of temperatures, then if the current temperature is larger than
# the temperature of the day on the top of the stack can pop it and work out the difference in days between them.
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            ind = stack.pop()
            result[ind] = i - ind
        stack.append(i)

    return result
