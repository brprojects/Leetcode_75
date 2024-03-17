from collections import deque

# Create a class which counts the number of requests (ping) within 3000 milliseconds

# Solution: Implement a queue and at each ping pop the leading values of the queue if they're over 3000 seconds before the current ping.
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while t - 3000 > self.queue[0]:
            self.queue.popleft()
        return len(self.queue)
    
obj = RecentCounter()
print(obj.ping(5))
print(obj.ping(10))
print(obj.ping(2900))
print(obj.ping(3000))
print(obj.ping(3007))
print(obj.ping(3009))
print(obj.ping(4000))

