import heapq
class MedianFinder:

    def __init__(self):
        self.lo= []
        self.hi = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        top= -heapq.heappop(self.lo)
        heapq.heappush(self.hi, top)
        if len(self.hi)>len(self.lo):
            top = heapq.heappop(self.hi)
            heapq.heappush(self.lo, -top)


    def findMedian(self) -> float:
        if len(self.lo)> len(self.hi):
            return -self.lo[0]
        return (-self.lo[0]+ self.hi[0])/2
        