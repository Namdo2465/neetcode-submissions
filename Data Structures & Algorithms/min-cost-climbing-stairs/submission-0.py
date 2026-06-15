class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        n = len(cost)
        mincost = [0]*(n+1)
        mincost[0] = cost[0]
        mincost[1] = cost[1]
        for i in range(2,n):
            mincost[i] = min((mincost[i-1] + cost[i]), (mincost[i-2] + cost[i]))
        return min(mincost[n-1], mincost[n-2])
        