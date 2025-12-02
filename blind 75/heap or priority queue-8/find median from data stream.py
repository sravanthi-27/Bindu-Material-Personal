class MedianFinder:

    def __init__(self):
        self.queue = []

    def addNum(self, num: int) -> None:
        self.queue.append(num)
        

    def findMedian(self) -> float:
        if not self.queue:
            return None
        self.queue.sort()
        mid = len(self.queue)//2
        if len(self.queue)%2==0:
            return (self.queue[mid-1]+self.queue[mid])/2
        return self.queue[mid]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()