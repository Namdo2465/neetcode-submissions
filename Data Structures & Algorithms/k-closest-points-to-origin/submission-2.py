import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x_coor, y_coor in points:
            dist = pow(x_coor, 2) + pow(y_coor, 2)
            heapq.heappush(heap, (dist, x_coor, y_coor))

        res = []
        for _ in range(k):
            dist, x_coor, y_coor = heapq.heappop(heap)
            res.append([x_coor, y_coor])
        
        return res

        

        