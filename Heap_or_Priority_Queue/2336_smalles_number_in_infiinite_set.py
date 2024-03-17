import heapq

# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

# Solution: Maintain the smallest number not yet popped and a heap of numbers added back
class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.added = []
        
    def popSmallest(self) -> int:
        if self.added:
            return heapq.heappop(self.added)
        else:
            result = self.smallest
            self.smallest += 1
            return result       

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.added:
            heapq.heappush(self.added, num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
obj.addBack(2)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
obj.addBack(1)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
