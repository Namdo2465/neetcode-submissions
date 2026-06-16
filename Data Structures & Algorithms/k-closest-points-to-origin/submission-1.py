from heapq import heapify, heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_arr = []
        for num in points:
            x_coor = num[0]
            y_coor = num[1]
            dist = x_coor**2 + y_coor**2
            dist_arr.append([dist, [x_coor, y_coor]])
        heapq.heapify(dist_arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(dist_arr)[1])
        return res
        
        