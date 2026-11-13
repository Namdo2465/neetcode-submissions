import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.max_size = k
        for num in nums:
            if len(self.heap) == k:
                heapq.heappush(self.heap, num)
                heapq.heappop(self.heap)
            else:
                heapq.heappush(self.heap, num)
        


    def add(self, val: int) -> int:
        if len(self.heap) < self.max_size:
            heapq.heappush(self.heap, val)
        elif len(self.heap) == self.max_size:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        return self.heap[0]
        
