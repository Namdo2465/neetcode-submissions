class MedianFinder:

    def __init__(self):
        self.num_heap = []
        

    def addNum(self, num: int) -> None:
        self.num_heap.append(num)

    def findMedian(self) -> float:
        self.num_heap.sort()
        length = len(self.num_heap)
        if length % 2 == 1:
            return self.num_heap[length//2]
        else:
            return (self.num_heap[length//2] + self.num_heap[(length-2)//2])/2
        
        