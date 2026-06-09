class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def recurse(stones):
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return stones[0]
            stones.sort()
            stone1 = stones.pop()
            stone2 = stones.pop()
            if stone1 > stone2:
                stones.append(stone1 -  stone2)
            return recurse(stones)
        return recurse(stones)
            

        