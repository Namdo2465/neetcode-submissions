import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, - stone)
        
        while len(heap) > 1:
            first_stone = - heapq.heappop(heap)
            second_stone = - heapq.heappop(heap)
            if first_stone != second_stone:
                heapq.heappush(heap, - abs(first_stone - second_stone))
        
        if not heap:
            return 0
        return - heap[0]